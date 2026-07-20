from datetime import datetime
from pairs import PAIRS
from market import get_market_signal

import time


last_pair = ""
last_signal_time = 0

COOLDOWN = 300


def generate_signal():

    global last_pair
    global last_signal_time


    best_signal = None
    best_score = -1


    # সব pair check করবে
    for pair in PAIRS:

        try:

            signal, rsi, ema20, confidence = (
                get_market_signal(pair)
            )


            # শুধু valid signal consider করবে
            if signal in [
                "🟢 CALL",
                "🔴 PUT"
            ]:

                score = confidence


                if score > best_score:

                    best_score = score

                    best_signal = (
                        pair,
                        signal,
                        rsi,
                        ema20,
                        confidence
                    )


        except Exception as e:

            print(
                f"❌ Error checking "
                f"{pair}: {e}"
            )


    # কোনো strong setup না থাকলে
    if best_signal is None:

        return """🎯 LPSB MOBILE SIGNAL

⏳ WAIT

📊 No strong multi-filter setup

🛡️ EMA + RSI + Candle + Volatility

⚠️ Market not clear
"""


    pair, signal, rsi, ema20, confidence = (
        best_signal
    )


    now = time.time()


    # একই pair-এর cooldown
    if (

        pair == last_pair

        and now - last_signal_time
        < COOLDOWN

    ):

        return """🎯 LPSB MOBILE SIGNAL

⏳ WAIT

🛡️ Same pair cooldown

⚡ Waiting for a fresh setup
"""


    last_pair = pair

    last_signal_time = now


    tm = datetime.now().strftime(
        "%H:%M"
    )


    message = f"""🎯 LPSB MOBILE SIGNAL

💱 Pair: {pair}

⏰ Time: {tm}

⏳ Expiry: 1M

🚨 {signal}

📊 RSI: {rsi}

📈 EMA20: {ema20}

🔥 Score: {confidence}%

🛡️ Multi-Filter Confirmed

✅ EMA Trend
✅ RSI
✅ Candle Direction
✅ Volatility

⚠️ Demo test before real trade
"""


    return message
