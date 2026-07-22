from datetime import datetime
from market import get_market_signal
from pairs import PAIRS
import time

COOLDOWN = 300

last_pair = ""
last_time = 0


def generate_signal():

    global last_pair, last_time

    best = None
    best_score = 0

    for pair in PAIRS:

        try:

            signal, rsi, ema20, confidence = get_market_signal(pair)

            if signal == "⏳ WAIT":
                continue

            if confidence > best_score:

                best_score = confidence

                best = (
                    pair,
                    signal,
                    rsi,
                    ema20,
                    confidence
                )

        except Exception as e:

            print(f"❌ {pair}: {e}")

    if best is None:
        return None

    pair, signal, rsi, ema20, confidence = best

    now = time.time()

    if pair == last_pair and now - last_time < COOLDOWN:
        return None

    last_pair = pair
    last_time = now

    return f"""🎯 LPSB PRO SIGNAL

💱 Pair: {pair}

⏰ Time: {datetime.now().strftime("%H:%M")}

⏳ Expiry: 1 Minute

{signal}

📊 RSI : {rsi}

📈 EMA20 : {ema20}

🔥 Confidence : {confidence}%

⚠️ Test on Demo First
"""
