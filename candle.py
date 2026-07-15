import os
import requests


def get_candles(pair, count=50):

    api_key = os.getenv("TWELVE_DATA_API_KEY")

    if not api_key:
        print("❌ TWELVE_DATA_API_KEY not found")
        return []

    if "_" in pair:
        pair = pair.split("_")[0]

    symbol = f"{pair[:3]}/{pair[3:]}"

    url = "https://api.twelvedata.com/time_series"

    params = {
        "symbol": symbol,
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

        if "values" not in data:
            print("❌ API Response:", data)
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
