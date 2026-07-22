from candle import get_candles

EMA_FAST = 20
EMA_SLOW = 50
RSI_PERIOD = 14


def calculate_ema(candles, period):
    closes = [c["close"] for c in candles]

    if len(closes) < period:
        return 0

    ema = sum(closes[:period]) / period
    multiplier = 2 / (period + 1)

    for price in closes[period:]:
        ema = (price - ema) * multiplier + ema

    return round(ema, 5)


def calculate_rsi(candles, period=14):
    closes = [c["close"] for c in candles]

    if len(closes) < period + 1:
        return 50

    gains = []
    losses = []

    for i in range(1, len(closes)):
        change = closes[i] - closes[i - 1]

        if change > 0:
            gains.append(change)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(abs(change))

    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period

    if avg_loss == 0:
        return 100

    rs = avg_gain / avg_loss
    return round(100 - (100 / (1 + rs)), 2)


def bullish(c):
    return c["close"] > c["open"]


def bearish(c):
    return c["close"] < c["open"]


def get_market_signal(pair):

    candles = get_candles(pair)

    if len(candles) < 60:
        return "⏳ WAIT", 0, 0, 0

    ema20 = calculate_ema(candles, EMA_FAST)
    ema50 = calculate_ema(candles, EMA_SLOW)
    rsi = calculate_rsi(candles)

    last = candles[-1]
    prev = candles[-2]

    # CALL
    if (
        ema20 > ema50
        and bullish(last)
        and bullish(prev)
        and 45 <= rsi <= 65
    ):
        return "🟢 CALL", rsi, ema20, 90

    # PUT
    if (
        ema20 < ema50
        and bearish(last)
        and bearish(prev)
        and 35 <= rsi <= 55
    ):
        return "🔴 PUT", rsi, ema20, 90

    return "⏳ WAIT", rsi, ema20, 0
