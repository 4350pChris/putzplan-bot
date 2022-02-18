from slack_bolt.async_app import AsyncApp
import logging
import os
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.DEBUG)
app = AsyncApp()


async def fetch_users(context, next):
    try:
        # TODO: hier DB zeug zum fetchen
        users = ["U016NV71SP4"]
    except Exception:
        users = []
    finally:
        context["initial_users"] = users
        next()


def create_home_view(context, next):
    context["home_view"] = {
        "type": "home",
        "blocks": [
            {
                "type": "input",
                "dispatch_action": True,
                "element": {
                    "type": "multi_users_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select users",
                        "emoji": True
                    },
                    "action_id": "putzplan-select-action",
                    "initial_users": context["initial_users"],
                },
                "label": {
                    "type": "plain_text",
                    "text": "Leute im Putzplan",
                    "emoji": True
                }
            }
        ]
    }
    next()


@app.event(event="app_home_opened", middleware=[fetch_users, create_home_view])
async def update_home_tab(event, client, logger, context):
    # TODO: get users from DB
    try:
        # views.publish is the method that your app uses to push a view to the Home tab
        await client.views_publish(
            # the user that opened your app's app home
            user_id=event["user"],
            # the view object that appears in the app home
            view=context["home_view"]
        )

    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")


@app.action("putzplan-select-action")
async def updatePutzplan(ack, payload, client, logger):
    await ack()
    users = logger.info(payload["selected_users"])
    # TODO: save in DB


if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
