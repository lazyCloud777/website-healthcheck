import os
import requests

URL = "https://nubxxxs.com/"

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def notify(message):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": message,
        },
        timeout=10,
    )

try:
    response = requests.get(URL, timeout=10)

    if response.status_code != 200:
        notify(
            f"⚠️ サイト異常\n"
            f"{URL}\n"
            f"Status: {response.status_code}"
        )

except Exception as e:
    notify(
        f"🚨 接続できません\n"
        f"{URL}\n"
        f"{e}"
    )