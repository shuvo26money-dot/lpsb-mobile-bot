import time
from datetime import datetime, timedelta

from signal import generate_signal
from telegram import send_signal

print("🚀 LPSB MOBILE PRE SIGNAL BOT STARTED")

last_message = ""


while True:

    try:
        now = datetime.now()

        # পরের মিনিটের Entry Time
        next_minute = (now + timedelta(minutes=1)).replace(second=0, microsecond=0)

        message = generate_signal()

        if message != last_message:

            pre_message = f"""
🎯 LPSB PRE SIGNAL

{message}

⏰ Entry Time: {next_minute.strftime('%H:%M')}
⏳ Expiry: 1M

⚡ Prepare For Entry
"""

            send_signal(pre_message)
            last_message = message

        else:
            print("Duplicate skipped")


        # প্রতি 10 সেকেন্ডে check করবে
        time.sleep(10)


    except Exception as e:
        print("Error:", e)
        time.sleep(10)