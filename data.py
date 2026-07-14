import requests


def get_price_data(pair):

    try:
        # Forex price demo API structure
        url = f"https://api.exchangerate.host/latest?base={pair[:3]}&symbols={pair[3:]}"

        r = requests.get(url, timeout=10)

        if r.status_code == 200:
            data = r.json()

            return data

    except Exception as e:
        print("Data Error:", e)

    return None