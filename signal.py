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

    # আগের Pair বাদ
    available = [p for p in PAIRS if p != last_pair]

    if not available:
        available = PAIRS

    pair = random.choice(available)

    # market.py থেকে dictionary নেবে
    data = get_market_signal(pair)

    signal = data.get("signal", "WAIT")
    rsi = data.get("rsi", 0)
    ema20 = data.get("ema20", 0)
    ema50 = data.get("ema50", 0)
    confidence = data.get("confidence", 0)
    reason = data.get("reason", "Market Not Clear")

    now = time.time()

    # 60 সেকেন্ড cooldown
    if now - last_signal_time < COOLDOWN:
        signal = "WAIT"

    # Strong signal হলে last pair/time update
    if signal in ["CALL", "PUT"] and confidence >= 90:
        last_pair = pair
        last_signal_time = now

    tm = datetime.now().strftime("%H:%M")

    # WAIT message
    if signal == "WAIT":

        message = f"""🎯 LPSB MOBILE SIGNAL

💱 Pair: {pair}
⏰ Time: {tm}
⏳ Expiry: 1M

⏳ WAIT

📊 RSI: {rsi}
📈 EMA20: {ema20}
📉 EMA50: {ema50}

⚠️ {reason}

⚡ Strong Filter Mode
"""

    # CALL / PUT message
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

🚨 {signal}

📊 RSI: {rsi}
📈 EMA20: {ema20}
📉 EMA50: {ema50}

🔥 Confidence: {confidence}%
{stars}

⚡ {reason}
⚡ Strong Filter Mode
"""

    return message
