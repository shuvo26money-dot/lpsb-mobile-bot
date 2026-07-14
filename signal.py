from datetime import datetime
from pairs import PAIRS
from market import get_market_signal
import random
import time

last_pair = ""
last_signal_time = 0

COOLDOWN = 60


def generate_signal():
    global last_pair, last_signal_time

    available = [p for p in PAIRS if p != last_pair]
    pair = random.choice(available)

    signal, rsi, ema, confidence = get_market_signal(pair)

    now = time.time()

    if now - last_signal_time < COOLDOWN:
        signal = "⏳ WAIT"

    if signal != "⏳ WAIT":
        last_pair = pair
        last_signal_time = now

    tm = datetime.now().strftime("%H:%M")

    if signal == "⏳ WAIT":

        status = "📊 Market Not Clear"

        if rsi >= 70:
            status = "⚠️ Overbought - Wait"

        elif rsi <= 30:
            status = "⚠️ Oversold - Wait"

        message = f"""🎯 LPSB MOBILE SIGNAL

💱 Pair: {pair}
⏰ Time: {tm}
⏳ Expiry: 1M

⏳ WAIT

📊 RSI: {rsi}
📈 EMA: {ema}

{status}

⚡ Strong Filter Mode
"""

    else:

        if confidence >= 90:
            stars = "⭐⭐⭐⭐⭐"

        elif confidence >= 80:
            stars = "⭐⭐⭐⭐"

        elif confidence >= 70:
            stars = "⭐⭐⭐"

        else:
            stars = "⭐⭐"

        message = f"""🎯 LPSB MOBILE SIGNAL

💱 Pair: {pair}
⏰ Time: {tm}
⏳ Expiry: 1M

{signal}

📊 RSI: {rsi}
📈 EMA: {ema}

🔥 Confidence: {confidence}%
{stars}

⚡ Strong Filter Mode
"""

    return message