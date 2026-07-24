import os
import requests

API_KEY = os.getenv("TWELVE_DATA_API_KEY")


def get_candles(pair, count=100):
    if not API_KEY:
        print("❌ TWELVE_DATA_API_KEY not found")
        return []

    symbol = pair.replace("_OTC", "").replace("-", "/")

    url = (
        f"https://api.twelvedata.com/time_series"
        f"?symbol={symbol}"
        f"&interval=1min"
        f"&outputsize={count}"
        f"&apikey={API_KEY}"
    )

    try:
        r = requests.get(url, timeout=10)
        data = r.json()

        # Debug
        print("📊 Symbol:", symbol)
        print("📥 API Response:", data)
        print("📈 Candles:", len(data.get("values", [])))

        if "values" not in data:
            print(f"❌ API Error: {data}")
            return []

        candles = []

        for c in reversed(data["values"]):
            candles.append({
                "open": float(c["open"]),
                "high": float(c["high"]),
                "low": float(c["low"]),
                "close": float(c["close"])
            })

        return candles

    except Exception as e:
        print(f"❌ Candle Error: {e}")
        return []
