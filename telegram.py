import requests
import os

BOT_TOKEN = os.getenv("8708926224:AAHaFvki2l0k_dXi8KZH5HQ6BEY4-C3Uezg")
CHAT_ID = os.getenv("7458276195")


def send_message(text):
    if not BOT_TOKEN or not CHAT_ID:
        print("❌ BOT_TOKEN বা CHAT_ID পাওয়া যায়নি")
        return False

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": text
    }

    try:
        r = requests.post(url, data=data, timeout=10)

        if r.status_code == 200:
            print("✅ Telegram message sent")
            return True
        else:
            print(r.text)
            return False

    except Exception as e:
        print(f"❌ Telegram Error: {e}")
        return False
