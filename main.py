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

    "09:00": "3 840 961.79 EUR  are expected from Loto 6/49 lottery",
    "09:10": "1150 RON are expected from Italia Win for Life lottery",
    "09:20": "5500 RON are expected from Ungaria Putto lottery",
    "09:30": "1330 RON are expected from Polonia Kaskada 12/24 lottery",
    "09:40": "3 840 961.79 EUR  are expected from Loto 6/49 lottery",
    "09:50": "1150 RON are expected from Italia Win for Life lottery",

    "10:00": "5500 RON are expected from Ungaria Putto lottery",
    "10:10": "1330 RON are expected from Polonia Kaskada 12/24 lottery",
    "10:20": "3 840 961.79 EUR  are expected from Loto 6/49 lottery",
    "10:30": "1150 RON are expected from Italia Win for Life lottery",
    "10:40": "5500 RON are expected from Ungaria Putto lottery",
    "10:50": "1330 RON are expected from Polonia Kaskada 12/24 lottery",

    "11:00": "3 840 961.79 EUR  are expected from Loto 6/49 lottery",
    "11:10": "1150 RON are expected from Italia Win for Life lottery",
    "11:20": "5500 RON are expected from Ungaria Putto lottery",
    "11:30": "1330 RON are expected from Polonia Kaskada 12/24 lottery",
    "11:40": "3 840 961.79 EUR  are expected from Loto 6/49 lottery",
    "11:50": "1150 RON are expected from Italia Win for Life lottery",

    # ===== PAUSE 12:00 -> 13:00 =====

    "13:00": "5500 RON are expected from Ungaria Putto lottery",
    "13:10": "1330 RON are expected from Polonia Kaskada 12/24 lottery",
    "13:20": "3 840 961.79 EUR  are expected from Loto 6/49 lottery",
    "13:30": "1150 RON are expected from Italia Win for Life lottery",
    "13:40": "5500 RON are expected from Ungaria Putto lottery",
    "13:50": "1330 RON are expected from Polonia Kaskada 12/24 lottery",

    "14:00": "3 840 961.79 EUR  are expected from Loto 6/49 lottery",
    "14:10": "1150 RON are expected from Italia Win for Life lottery",
    "14:20": "5500 RON are expected from Ungaria Putto lottery",
    "14:30": "1330 RON are expected from Polonia Kaskada 12/24 lottery",
    "14:40": "3 840 961.79 EUR  are expected from Loto 6/49 lottery",
    "14:50": "1150 RON are expected from Italia Win for Life lottery",

    "15:00": "5500 RON are expected from Ungaria Putto lottery",
    "15:10": "1330 RON are expected from Polonia Kaskada 12/24 lottery",
    "15:20": "3 840 961.79 EUR  are expected from Loto 6/49 lottery",
    "15:30": "1150 RON are expected from Italia Win for Life lottery",
    "15:40": "5500 RON are expected from Ungaria Putto lottery",
    "15:50": "1330 RON are expected from Polonia Kaskada 12/24 lottery",

    # ===================== EVENING =====================

    "20:00": "3 840 961.79 EUR  are expected from Loto 6/49 lottery",
    "20:10": "1150 RON are expected from Italia Win for Life lottery",
    "20:20": "5500 RON are expected from Ungaria Putto lottery",
    "20:30": "1330 RON are expected from Polonia Kaskada 12/24 lottery",
    "20:40": "3 840 961.79 EUR  are expected from Loto 6/49 lottery",
    "20:50": "1150 RON are expected from Italia Win for Life lottery",

    "21:00": "5500 RON are expected from Ungaria Putto lottery",
    "21:10": "1330 RON are expected from Polonia Kaskada 12/24 lottery",
    "21:20": "3 840 961.79 EUR  are expected from Loto 6/49 lottery",
    "21:30": "1150 RON are expected from Italia Win for Life lottery",
    "21:40": "5500 RON are expected from Ungaria Putto lottery",
    "21:50": "1330 RON are expected from Polonia Kaskada 12/24 lottery",

    "22:00": "3 840 961.79 EUR  are expected from Loto 6/49 lottery",
    "22:10": "1150 RON are expected from Italia Win for Life lottery",
    "22:20": "5500 RON are expected from Ungaria Putto lottery",
    "22:30": "1330 RON are expected from Polonia Kaskada 12/24 lottery",
    "22:40": "3 840 961.79 EUR  are expected from Loto 6/49 lottery",
    "22:50": "1150 RON are expected from Italia Win for Life lottery",
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
