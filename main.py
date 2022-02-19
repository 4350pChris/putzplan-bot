from src.db.config import models
import src.db.models.user
import src.db.models.room
from src.app import app
from asyncio import run
import logging
import os
# model imports are needed to register the classes

if __name__ == "__main__":
    try:
        run(models.create_all())
    except Exception as e:
        logging.error(e)
        exit(1)

    app.start(port=int(os.environ.get("PORT", 3000)))
