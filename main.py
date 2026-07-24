import time
from signal import generate_signal
from telegram import send_message

print("🚀 LPSB PRO BOT STARTED")

while True:
    try:
        message = generate_signal()

        if message:
            print(message)
            send_message(message)
        else:
            print("⏳ No strong setup")

    except Exception as e:
        print(f"❌ Error: {e}")

    time.sleep(120)
