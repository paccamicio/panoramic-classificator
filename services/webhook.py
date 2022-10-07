from datetime import datetime
from textwrap import shorten
from os import getenv
from requests import post
from dotenv import load_dotenv


def dispatch_discord_webhook(title, description, client_=""):
    load_dotenv()

    path = getenv('DISCORD_WEBHOOK_IMG_CLASSIFICATION')

    if not path:
        return print('no webhook URL into .env file')

    if len(description) > 2048:
        shorten(description, width=2048)

    payload = {
        "content": str(datetime.now()),
        "embeds": [
            {
                "title": str(client_)+" "+str(title),
                "description": str(description),
                "color": "7506394"
            }
        ]
    }

    post(path, json=payload)
