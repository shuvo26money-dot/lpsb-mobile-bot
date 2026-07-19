from datetime import datetime
from pairs import PAIRS
from market import get_market_signal

import random
import time


last_pair = ""
last_signal_time = 0

COOLDOWN = 60


def generate_signal():

    global last_pair
    global last_signal_time


    # আগের pair বাদ
    available = [
        p for p in PAIRS
        if p != last_pair
    ]


    if not available:

        available = PAIRS


    pair = random.choice(
        available
    )


    # Market data
    signal, rsi, ema20, confidence = (
        get_market_signal(pair)
    )


    # Data না এলে
    if rsi == 0 and ema20 == 0:

        print(
            f"⚠️ No market data for {pair}"
        )

        return None


    now = time.time()


    # Cooldown
    if (
        now - last_signal_time
        < COOLDOWN
    ):

        signal = "⏳ WAIT"


    # 85% বা তার বেশি হলেই signal
    if (
        signal in [
            "🟢 CALL",
            "🔴 PUT"
        ]
        and confidence >= 85
    ):

        last_pair = pair

        last_signal_time = now


    else:

        signal = "⏳ WAIT"


    tm = datetime.now().strftime(
        "%H:%M"
    )


    # WAIT
    if signal == "⏳ WAIT":

        status = (
            "📊 Market Not Clear"
        )


        if rsi >= 70:

            status = (
                "⚠️ Overbought - Wait"
            )


        elif rsi <= 30:

            status = (
                "⚠️ Oversold - Wait"
            )


        message = f"""🎯 LPSB MOBILE SIGNAL

💱 Pair: {pair}

⏰ Time: {tm}

⏳ Expiry: 1M

⏳ WAIT

📊 RSI: {rsi}

📈 EMA20: {ema20}

🔥 Confidence: {confidence}%

{status}

⚡ Filter Mode
"""


    # CALL / PUT
    else:

        message = f"""🎯 LPSB MOBILE SIGNAL

💱 Pair: {pair}

⏰ Time: {tm}

⏳ Expiry: 1M

🚨 {signal}

📊 RSI: {rsi}

📈 EMA20: {ema20}

🔥 Confidence: {confidence}%

⚡ Filter Mode
"""


    return message
