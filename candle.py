import os
import requests


def get_candles(pair, count=100):

    api_key = os.getenv(
        "TWELVE_DATA_API_KEY"
    )


    if not api_key:

        print(
            "❌ TWELVE_DATA_API_KEY not found"
        )

        return []


    # Pair format ঠিক করা
    pair = pair.replace(
        "_OTC",
        ""
    )

    pair = pair.replace(
        "-",
        "/"
    )


    if "/" not in pair:

        pair = (
            pair[:3]
            + "/"
            + pair[3:]
        )


    url = (
        "https://api.twelvedata.com/"
        "time_series"
    )


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


        if response.status_code != 200:

            print(
                "❌ HTTP Error:",
                response.status_code
            )

            return []


        data = response.json()


        if data.get("code") == 429:

            print(
                f"⚠️ Rate limit reached "
                f"for {pair}"
            )

            return []


        if "values" not in data:

            print(
                f"❌ API Response "
                f"for {pair}:",
                data
            )

            return []


        candles = []


        for item in reversed(
            data["values"]
        ):


            try:

                candle = {

                    "open": float(
                        item["open"]
                    ),

                    "close": float(
                        item["close"]
                    ),

                    "high": float(
                        item["high"]
                    ),

                    "low": float(
                        item["low"]
                    )

                }


                candles.append(
                    candle
                )


            except:

                continue


        if len(candles) < 60:

            print(
                f"⚠️ Not enough candles "
                f"for {pair}: "
                f"{len(candles)}"
            )

            return []


        return candles


    except requests.exceptions.Timeout:

        print(
            "❌ API Timeout"
        )

        return []


    except Exception as e:

        print(
            "❌ Candle Error:",
            e
        )

        return []
