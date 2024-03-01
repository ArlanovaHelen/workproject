import os

import requests


def send_message(text, chat_id=None):
    # Send telegram request
    token = os.environ.get("TELEGRAM_API_TOKEN")
    default_chat_id = "727733241"

    response = requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={"chat_id": chat_id or default_chat_id, "text": text},
    )

    print(response.status_code)
    print(response.json())
