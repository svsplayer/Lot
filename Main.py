import requests
import time
from datetime import datetime
import os
import pytz

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not TOKEN or not CHAT_ID:
    print("Missing TOKEN or CHAT_ID!")
    exit()

tz = pytz.timezone("Europe/Bucharest")

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        r = requests.post(
            url,
            data={"chat_id": CHAT_ID, "text": msg},
            timeout=10
        )
        if r.status_code != 200:
            print("Telegram error:", r.text)
    except Exception as e:
        print("Send failed:", e)


SCHEDULE = {
    "09:10": "You Won 2 400 000 EUR at Loto 6/49",
    "10:10": "You Won 2 400 000 EUR at Loto 6/49",
    "11:10": "You Won 2 400 000 EUR at Loto 6/49",
    "13:10": "You Won 2 400 000 EUR at Loto 6/49",
    "15:10": "You Won 2 400 000 EUR at Loto 6/49",

    "09:25": "You Won 2700 RON at Canada Atlantic Bucko lottery",
    "10:25": "You Won 2700 RON at Canada Atlantic Bucko lottery",
    "11:25": "You Won 2700 RON at Canada Atlantic Bucko lottery",
    "13:25": "You Won 2700 RON at Canada Atlantic Bucko lottery",
    "15:25": "You Won 2700 RON at Canada Atlantic Bucko lottery",

    "09:35": "You Won 1800 RON at SUA Florida Fantasy lottery",
    "10:35": "You Won 1800 RON at SUA Florida Fantasy lottery",
    "11:35": "You Won 1800 RON at SUA Florida Fantasy lottery",
    "13:35": "You Won 1800 RON at SUA Florida Fantasy lottery",
    "15:35": "You Won 1800 RON at SUA Florida Fantasy lottery",

    "09:45": "You Won 1150 RON at Italia Win for Life lottery",
    "10:45": "You Won 1150 RON at Italia Win for Life lottery",
    "11:45": "You Won 1150 RON at Italia Win for Life lottery",
    "13:45": "You Won 1150 RON at Italia Win for Life lottery",
    "15:45": "You Won 1150 RON at Italia Win for Life lottery",

    "09:52": "You Won 1140 RON at SUA Wisconsin Badger lottery",
    "10:52": "You Won 1140 RON at SUA Wisconsin Badger lottery",
    "11:52": "You Won 1140 RON at SUA Wisconsin Badger lottery",
    "13:52": "You Won 1140 RON at SUA Wisconsin Badger lottery",
    "15:52": "You Won 1140 RON at SUA Wisconsin Badger lottery",
    "23:15": "You Won 1140 RON at SUA Wisconsin Badger lottery",
}

already_sent = set()

print("Bot running...")

while True:
    now = datetime.now(tz).strftime("%H:%M")

    if now in SCHEDULE and now not in already_sent:
        send(SCHEDULE[now])
        already_sent.add(now)

    if now == "00:00":
        already_sent.clear()

    time.sleep(5)
