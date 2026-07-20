import time

from datetime import datetime, timedelta

from signal import generate_signal

from telegram import send_signal


print("🚀 LPSB MOBILE PRE SIGNAL BOT STARTED")


last_message = ""


while True:

    try:

        now = datetime.now()

        # Signal এখন পাঠাবে,
        # Entry হবে 2 মিনিট পরে
        entry_time = (
            now + timedelta(minutes=2)
        ).replace(
            second=0,
            microsecond=0
        )


        message = generate_signal()


        if message and message != last_message:

            pre_message = f"""
🎯 LPSB PRE SIGNAL

{message}

⏰ Entry Time: {entry_time.strftime('%H:%M')}

⏳ Expiry: 1M

⚡ Prepare For Entry
"""


            send_signal(pre_message)

            last_message = message

            print(
                f"✅ Signal sent at "
                f"{datetime.now().strftime('%H:%M:%S')}"
            )


        else:

            print(
                "⏭ Duplicate skipped"
            )


        # প্রতি 120 সেকেন্ডে check
        time.sleep(120)


    except Exception as e:

        print(
            f"❌ Error: {e}"
        )

        time.sleep(120)
