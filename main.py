import time
from datetime import datetime, timedelta

from signal import generate_signal
from telegram import send_signal


print("🚀 LPSB MOBILE PRE SIGNAL BOT STARTED")


# শেষ পাঠানো signal মনে রাখবে
last_message = ""


while True:

    try:

        # বর্তমান সময়
        now = datetime.now()

        # পরের মিনিটের Entry Time
        next_minute = (
            now + timedelta(minutes=1)
        ).replace(
            second=0,
            microsecond=0
        )


        # Signal তৈরি
        message = generate_signal()


        # Signal পাওয়া গেলে
        if message:

            # একই signal আবার পাঠাবে না
            if message != last_message:

                pre_message = f"""
🎯 LPSB PRE SIGNAL

{message}

⏰ Entry Time: {next_minute.strftime('%H:%M')}
⏳ Expiry: 1M

⚡ Prepare For Entry
"""


                # Telegram-এ পাঠাবে
                send_signal(pre_message)


                # শেষ signal save করবে
                last_message = message


                print(
                    f"✅ Signal sent at "
                    f"{datetime.now().strftime('%H:%M:%S')}"
                )


            else:

                print(
                    f"⏭ Duplicate skipped "
                    f"at {datetime.now().strftime('%H:%M:%S')}"
                )


        else:

            print(
                f"⏳ No valid signal "
                f"at {datetime.now().strftime('%H:%M:%S')}"
            )


        # Twelve Data API limit বাঁচাতে
        # 60 সেকেন্ড অপেক্ষা করবে
        time.sleep(60)


    except Exception as e:

        print(
            f"❌ Error: {e}"
        )


        # Error হলে 60 সেকেন্ড অপেক্ষা করবে
        # তারপর আবার চেষ্টা করবে
        time.sleep(60)
