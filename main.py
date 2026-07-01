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

    "09:00": "Big L.W. are coming today!",
    "09:10": "Big L.W. are coming today!",
    "09:20": "Big L.W. are coming today!",
    "09:30": "Big L.W. are coming today!",
    "09:40": "Big L.W. are coming today!",
    "09:50": "Big L.W. are coming today!",

    "10:00": "Big L.W. are coming today!",
    "10:10": "Big L.W. are coming today!",
    "10:20": "Big L.W. are coming today!",
    "10:30": "Big L.W. are coming today!",
    "10:40": "Big L.W. are coming today!",
    "10:50": "Big L.W. are coming today!",

    "11:00": "Big L.W. are coming today!",
    "11:10": "Big L.W. are coming today!",
    "11:20": "Big L.W. are coming today!",
    "11:30": "Big L.W. are coming today!",
    "11:40": "Big L.W. are coming today!",
    "11:50": "Big L.W. are coming today!",

    # ===== PAUSE 12:00 -> 13:00 =====

    "13:00": "Big L.W. are coming today!",
    "13:10": "Big L.W. are coming today!",
    "13:20": "Big L.W. are coming today!",
    "13:30": "Big L.W. are coming today!",
    "13:40": "Big L.W. are coming today!",
    "13:50": "Big L.W. are coming today!",

    "14:00": "Big L.W. are coming today!",
    "14:10": "Big L.W. are coming today!",
    "14:20": "Big L.W. are coming today!",
    "14:30": "Big L.W. are coming today!",
    "14:40": "Big L.W. are coming today!",
    "14:50": "Big L.W. are coming today!",

    "15:00": "Big L.W. are coming today!",
    "15:10": "Big L.W. are coming today!",
    "15:20": "Big L.W. are coming today!",
    "15:30": "Big L.W. are coming today!",
    "15:40": "Big L.W. are coming today!",
    "15:50": "Big L.W. are coming today!",

    # ===================== EVENING =====================

    "20:00": "Big L.W. are coming today!",
    "20:10": "Big L.W. are coming today!",
    "20:20": "Big L.W. are coming today!",
    "20:30": "Big L.W. are coming today!",
    "20:40": "Big L.W. are coming today!",
    "20:50": "Big L.W. are coming today!",

    "21:00": "Big L.W. are coming today!",
    "21:10": "Big L.W. are coming today!",
    "21:20": "Big L.W. are coming today!",
    "21:30": "Big L.W. are coming today!",
    "21:40": "Big L.W. are coming today!",
    "21:50": "Big L.W. are coming today!",

    "22:00": "Big L.W. are coming today!",
    "22:10": "Big L.W. are coming today!",
    "22:20": "Big L.W. are coming today!",
    "22:30": "Big L.W. are coming today!",
    "22:40": "Big L.W. are coming today!",
    "22:50": "Big L.W. are coming today!",
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
