from slack_bolt.async_app import AsyncApp
import logging
from .db.models.user import User

logging.basicConfig(level=logging.INFO)
app = AsyncApp()


async def fetch_users(context, next):
    try:
        # TODO: hier DB zeug zum fetchen
        db_users = await User.objects.all()
        users = [u.user_id for u in db_users]
    except Exception:
        users = []
    finally:
        context["initial_users"] = users
        await next()


async def create_home_view(context, next):
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
    await next()


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


@app.action({"action_id": "putzplan-select-action"}, middleware=[fetch_users])
async def update_putzplan(ack, action, context, logger):
    await ack()
    current_users = context["initial_users"]
    selected_users = action["selected_users"]
    users_added = [u for u in selected_users if u not in current_users]
    users_removed = [u for u in current_users if u not in selected_users]

    await User.objects.filter(user_id__in=users_removed).delete()

    for user_id in users_added:
        try:
            await User.objects.create(user_id=user_id)
        except Exception as e:
            logger.error(e)
