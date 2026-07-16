import os
import requests


def get_candles(pair, count=50):

    api_key = os.getenv("TWELVE_DATA_API_KEY")

    if not api_key:
        print("❌ TWELVE_DATA_API_KEY not found")
        return []

    # EUR/USD format ঠিক রাখবে
    pair = pair.replace("_OTC", "")
    pair = pair.replace("-", "/")

    if "/" not in pair:
        pair = pair[:3] + "/" + pair[3:]

    url = "https://api.twelvedata.com/time_series"

    params = {
        "symbol": pair,
        "interval": "1min",
        "outputsize": count,
        "apikey": api_key
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        data = response.json()

        if data.get("code") == 429:
            print(f"⚠️ Rate limit reached for {pair}")
            return []

        if "values" not in data:
            print(f"❌ API Response for {pair}:", data)
            return []

        candles = []

        for item in reversed(data["values"]):

            candles.append({
                "open": float(item["open"]),
                "close": float(item["close"]),
                "high": float(item["high"]),
                "low": float(item["low"])
            })

        return candles

    except Exception as e:

        print("❌ Candle Error:", e)

        return []
