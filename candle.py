import requests

API_KEY ="5d038a9ab14a48938d3c7bd6ec434955"


def get_candles(pair, count=50):

    symbol = pair

    url = (
        f"https://api.twelvedata.com/time_series"
        f"?symbol={symbol}"
        f"&interval=1min"
        f"&outputsize={count}"
        f"&apikey={API_KEY}"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if "values" not in data:
            print("API Response:", data)
            return []

        candles = []

        for item in data["values"][::-1]:
            candles.append({
                "open": float(item["open"]),
                "close": float(item["close"]),
                "high": float(item["high"]),
                "low": float(item["low"])
            })

        return candles

    except Exception as e:
        print("Candle Error:", e)
        return []