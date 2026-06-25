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

    "09:00": "WLTH",
    "09:10": "WLTH",
    "09:20": "WLTH",
    "09:30": "WLTH",
    "09:40": "WLTH",
    "09:50": "WLTH",

    "10:00": "WLTH",
    "10:10": "WLTH",
    "10:20": "WLTH",
    "10:30": "WLTH",
    "10:40": "WLTH",
    "10:50": "WLTH",

    "11:00": "WLTH",
    "11:10": "WLTH",
    "11:20": "WLTH",
    "11:30": "WLTH",
    "11:40": "WLTH",
    "11:50": "WLTH",

    # ===== PAUSE 12:00 -> 13:00 =====

    "13:00": "WLTH",
    "13:10": "WLTH",
    "13:20": "WLTH",
    "13:30": "WLTH",
    "13:40": "WLTH",
    "13:50": "WLTH",

    "14:00": "WLTH",
    "14:10": "WLTH",
    "14:20": "WLTH",
    "14:30": "WLTH",
    "14:40": "WLTH",
    "14:50": "WLTH",

    "15:00": "WLTH",
    "15:10": "WLTH",
    "15:20": "WLTH",
    "15:30": "WLTH",
    "15:40": "WLTH",
    "15:50": "WLTH",

    # ===================== EVENING =====================

    "20:00": "WLTH",
    "20:10": "WLTH",
    "20:20": "WLTH",
    "20:30": "WLTH",
    "20:40": "WLTH",
    "20:50": "WLTH",

    "21:00": "WLTH",
    "21:10": "WLTH",
    "21:20": "WLTH",
    "21:30": "WLTH",
    "21:40": "WLTH",
    "21:50": "WLTH",

    "22:00": "WLTH",
    "22:10": "WLTH",
    "22:20": "WLTH",
    "22:30": "WLTH",
    "22:40": "WLTH",
    "22:50": "WLTH",
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
