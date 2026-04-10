# Example: Single Coin Price Report
# Deploy contracts/price_feed.py on GenLayer Studio first.
#
# FUNCTION: get_price(coin)
# INPUT:    "bitcoin"
# OUTPUT:   "$67,432"
#
# FUNCTION: get_24h_change(coin)
# INPUT:    "ethereum"
# OUTPUT:   "+3.42%"
#
# FUNCTION: get_market_cap(coin)
# INPUT:    "solana"
# OUTPUT:   "$78.4 billion"
#
# FUNCTION: is_bullish(coin)
# INPUT:    "bitcoin"
# OUTPUT:   "Bullish — 24h price change shows a gain of 3.2% in the last day"
#
# FUNCTION: get_price_in_multiple_currencies(coin)
# INPUT:    "bitcoin"
# OUTPUT:
#   USD: $67,432
#   EUR: €62,180
#   GBP: £53,200
