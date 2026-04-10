# GenLayer Price Feed

A reusable crypto price feed library for GenLayer Intelligent Contracts to fetch
real-time prices, market caps, trading volumes, and 24-hour trends for any
cryptocurrency — no API keys required.

## Features

- Current USD price for any cryptocurrency
- Market cap in readable format
- 24-hour price change percentage
- Price in multiple currencies (USD, EUR, GBP)
- Bullish/bearish trend detection
- Full market summary for any coin
- Side-by-side comparison of two coins
- Top 5 coins market overview

## Contract Functions

| Function | Input | Output |
|----------|-------|--------|
| `get_price(coin)` | Coin ID | Current USD price |
| `get_market_cap(coin)` | Coin ID | Market cap in USD |
| `get_24h_change(coin)` | Coin ID | 24h % change |
| `get_price_in_multiple_currencies(coin)` | Coin ID | Price in USD, EUR, GBP |
| `is_bullish(coin)` | Coin ID | Bullish/Bearish + reason |
| `get_full_summary(coin)` | Coin ID | Full market summary |
| `compare_prices(coin1, coin2)` | Two coin IDs | Side-by-side comparison |
| `get_top_coins_summary()` | None | Top 5 coins overview |

## How to Deploy

1. Open [GenLayer Studio](https://studio.genlayer.com)
2. Create a new contract
3. Paste the contents of `contracts/price_feed.py`
4. Click **Deploy**
5. Call any function with a CoinGecko coin ID

## Example Outputs

**get_full_summary("bitcoin")**
```
Price: $67,432
Market Cap: $1.32 trillion
24h Volume: $38.4 billion
24h Change: +3.42%
```

**compare_prices("bitcoin", "ethereum")**
```
Bitcoin: $67,432 | 24h Change: +3.42%
Ethereum: $3,521 | 24h Change: +2.18%
Bitcoin outperformed Ethereum in the last 24 hours.
```

**get_top_coins_summary()**
```
Bitcoin (BTC): $67,432 | +3.42%
Ethereum (ETH): $3,521 | +2.18%
BNB: $412 | -0.54%
Solana (SOL): $178 | +5.21%
Cardano (ADA): $0.48 | +0.80%
```

## Repository Structure

```
genlayer-price-feed/
├── contracts/
│   └── price_feed.py          # Main Intelligent Contract
├── examples/
│   ├── single_coin_report.py  # Single coin examples
│   ├── coin_comparison.py     # Comparison examples
│   └── market_overview.py     # Market overview examples
├── utils/
│   └── supported_coins.py     # Reference coin list
├── LICENSE
└── README.md
```

## Built With

- [GenLayer](https://genlayer.com) — AI-powered blockchain
- [CoinGecko](https://coingecko.com) — Free crypto market data API

## License

MIT
