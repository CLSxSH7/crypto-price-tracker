import requests


def get_crypto_prices():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',  # Currency | change as needed | ex: brl, usd, eur, etc...
        'order': 'market_cap_desc',  # Sort by market capitalization | asc or desc
        'per_page': 10,  # Number of cryptos to be displayed | change as needed
        'sparkline': False,  # Price change charts
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        for i, crypto in enumerate(data, start=1):
            name = crypto['name']
            price = crypto['current_price']
            print(f"{i}. {name}: ${price}")
    else:
        print("Failed to fetch crypto prices.")


if __name__ == "__main__":
    get_crypto_prices()
