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
    # ===================== MORNING / AFTERNOON =====================
    # Runs from 09:00 -> 11:50
    # Pause 12:00 -> 13:00
    # Continues 13:00 -> 15:50

    "09:00": "You Won 3 061 966.91 EUR at Loto 6/49",
    "09:10": "You Won 2700 RON at Canada Atlantic Bucko lottery",
    "09:20": "You Won 1800 RON at SUA Florida Fantasy lottery",
    "09:30": "You Won 1150 RON at Italia Win for Life lottery",
    "09:40": "You Won 1140 RON at SUA Wisconsin Badger lottery",
    "09:50": "You Won 5500 RON at Ungaria Putto lottery",

    "10:00": "You Won 1200 RON at SUA Colorado Cash",
    "10:10": "You Won 3 061 966.91 EUR at Loto 6/49",
    "10:20": "You Won 2700 RON at Canada Atlantic Bucko lottery",
    "10:30": "You Won 1800 RON at SUA Florida Fantasy lottery",
    "10:40": "You Won 1150 RON at Italia Win for Life lottery",
    "10:50": "You Won 1140 RON at SUA Wisconsin Badger lottery",

    "11:00": "You Won 5500 RON at Ungaria Putto lottery",
    "11:10": "You Won 1200 RON at SUA Colorado Cash",
    "11:20": "You Won 3 061 966.91 EUR at Loto 6/49",
    "11:30": "You Won 2700 RON at Canada Atlantic Bucko lottery",
    "11:40": "You Won 1800 RON at SUA Florida Fantasy lottery",
    "11:50": "You Won 1150 RON at Italia Win for Life lottery",

    # ===== PAUSE 12:00 -> 13:00 =====

    "13:00": "You Won 1140 RON at SUA Wisconsin Badger lottery",
    "13:10": "You Won 5500 RON at Ungaria Putto lottery",
    "13:20": "You Won 1200 RON at SUA Colorado Cash",
    "13:30": "You Won 3 061 966.91 EUR at Loto 6/49",
    "13:40": "You Won 2700 RON at Canada Atlantic Bucko lottery",
    "13:50": "You Won 1800 RON at SUA Florida Fantasy lottery",

    "14:00": "You Won 1150 RON at Italia Win for Life lottery",
    "14:10": "You Won 1140 RON at SUA Wisconsin Badger lottery",
    "14:20": "You Won 5500 RON at Ungaria Putto lottery",
    "14:30": "You Won 1200 RON at SUA Colorado Cash",
    "14:40": "You Won 3 061 966.91 EUR at Loto 6/49",
    "14:50": "You Won 2700 RON at Canada Atlantic Bucko lottery",

    "15:00": "You Won 1800 RON at SUA Florida Fantasy lottery",
    "15:10": "You Won 1150 RON at Italia Win for Life lottery",
    "15:20": "You Won 1140 RON at SUA Wisconsin Badger lottery",
    "15:30": "You Won 5500 RON at Ungaria Putto lottery",
    "15:40": "You Won 1200 RON at SUA Colorado Cash",
    "15:50": "You Won 3 061 966.91 EUR at Loto 6/49",

    # ===================== EVENING =====================
    # Runs from 20:00 -> 22:50

    "20:00": "You Won 2700 RON at Canada Atlantic Bucko lottery",
    "20:10": "You Won 1800 RON at SUA Florida Fantasy lottery",
    "20:20": "You Won 1150 RON at Italia Win for Life lottery",
    "20:30": "You Won 1140 RON at SUA Wisconsin Badger lottery",
    "20:40": "You Won 5500 RON at Ungaria Putto lottery",
    "20:50": "You Won 1200 RON at SUA Colorado Cash",

    "21:00": "You Won 3 061 966.91 EUR at Loto 6/49",
    "21:10": "You Won 2700 RON at Canada Atlantic Bucko lottery",
    "21:20": "You Won 1800 RON at SUA Florida Fantasy lottery",
    "21:30": "You Won 1150 RON at Italia Win for Life lottery",
    "21:40": "You Won 1140 RON at SUA Wisconsin Badger lottery",
    "21:50": "You Won 5500 RON at Ungaria Putto lottery",

    "22:00": "You Won 1200 RON at SUA Colorado Cash",
    "22:10": "You Won 3 061 966.91 EUR at Loto 6/49",
    "22:20": "You Won 2700 RON at Canada Atlantic Bucko lottery",
    "22:30": "You Won 1800 RON at SUA Florida Fantasy lottery",
    "22:40": "You Won 1150 RON at Italia Win for Life lottery",
    "22:50": "You Won 1140 RON at SUA Wisconsin Badger lottery",
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
