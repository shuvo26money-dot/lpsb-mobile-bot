import time

from signal import generate_signal
from telegram_bot import send_message


print("🚀 LPSB PRO BOT STARTED")

while True:

    try:

        message = generate_signal()

        if message:

            print(message)

            send_message(message)

        else:

            print("⏳ No strong setup...")

    except Exception as e:

        print(f"❌ Bot Error: {e}")

    # প্রতি 18000 সেকেন্ডে একবার চেক করবে
    time.sleep(18000)
