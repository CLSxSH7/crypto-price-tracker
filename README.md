# Crypto Price Tracker

This Python script fetches the latest prices of cryptocurrencies using the CoinGecko API and displays them in the console.

## Dependencies

- Python 3
- requests library

You can install the dependencies using pip:

```bash
pip install requests
```

## Usage

To use this script, simply run it from the command line:

```bash
python crypto.py
```

The script will fetch the prices of the top cryptocurrencies and display them in the console.

You can customize the behavior of the script by modifying the parameters in the `get_crypto_prices` function:

- `vs_currency`: The currency to display the prices in ('usd', 'eur', 'brl', etc)
- `order`: The order in which the cryptocurrencies are sorted ('market_cap_desc' for market capitalization descending, 'market_cap_asc' for market capitalization ascending)
- `per_page`: The number of cryptocurrencies to display
- `sparkline`: Whether to include sparkline charts showing price change

## Example Output

1. Bitcoin: $57000
2. Ethereum: $2000
3. Dogecoin: $400
...
