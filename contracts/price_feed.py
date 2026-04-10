from genlayer import *

class PriceFeed(gl.Contract):
    """
    GenLayer Price Feed Library
    A comprehensive crypto price feed library for Intelligent Contracts.
    Fetches real-time cryptocurrency data from CoinGecko — no API keys required.
    """

    def __init__(self):
        pass

    @gl.public.view
    def get_price(self, coin: str) -> str:
        """Fetch the current USD price of any cryptocurrency."""
        data = gl.get_webpage(
            f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
        )
        return gl.exec_prompt(
            f"Extract ONLY the current USD price of {coin} from this data. "
            f"Return just the number with dollar sign, nothing else: {data}"
        )

    @gl.public.view
    def get_market_cap(self, coin: str) -> str:
        """Fetch the current market cap of any cryptocurrency in USD."""
        data = gl.get_webpage(
            f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd&include_market_cap=true"
        )
        return gl.exec_prompt(
            f"Extract ONLY the market cap of {coin} in USD from this data. "
            f"Return it in a readable format like $1.2 billion, nothing else: {data}"
        )

    @gl.public.view
    def get_24h_change(self, coin: str) -> str:
        """Fetch the 24-hour price change percentage of any cryptocurrency."""
        data = gl.get_webpage(
            f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd&include_24hr_change=true"
        )
        return gl.exec_prompt(
            f"Extract ONLY the 24-hour price change percentage of {coin} from this data. "
            f"Return just the percentage with + or - sign, nothing else: {data}"
        )

    @gl.public.view
    def get_full_summary(self, coin: str) -> str:
        """Get a complete market summary for any cryptocurrency."""
        data = gl.get_webpage(
            f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
            f"&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true"
        )
        return gl.exec_prompt(
            f"From this data for {coin}, provide a clean summary including: "
            f"current USD price, market cap, 24-hour trading volume, and 24-hour price change. "
            f"Format it neatly on separate lines: {data}"
        )

    @gl.public.view
    def compare_prices(self, coin1: str, coin2: str) -> str:
        """Compare current prices and 24h changes between two cryptocurrencies."""
        data1 = gl.get_webpage(
            f"https://api.coingecko.com/api/v3/simple/price?ids={coin1}&vs_currencies=usd&include_24hr_change=true"
        )
        data2 = gl.get_webpage(
            f"https://api.coingecko.com/api/v3/simple/price?ids={coin2}&vs_currencies=usd&include_24hr_change=true"
        )
        return gl.exec_prompt(
            f"Compare {coin1} and {coin2} using this data. "
            f"{coin1} data: {data1}. {coin2} data: {data2}. "
            f"Return a brief side-by-side comparison of price and 24h change for both coins."
        )

    @gl.public.view
    def is_bullish(self, coin: str) -> str:
        """Determine if a cryptocurrency is currently trending bullish or bearish."""
        data = gl.get_webpage(
            f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd&include_24hr_change=true"
        )
        return gl.exec_prompt(
            f"Based on the 24-hour price change of {coin} in this data, "
            f"is it currently bullish or bearish? "
            f"Answer with only Bullish or Bearish followed by one short reason: {data}"
        )

    @gl.public.view
    def get_price_in_multiple_currencies(self, coin: str) -> str:
        """Fetch the price of a cryptocurrency in USD, EUR, and GBP."""
        data = gl.get_webpage(
            f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd,eur,gbp"
        )
        return gl.exec_prompt(
            f"From this data, extract the price of {coin} in USD, EUR, and GBP. "
            f"Format each on a new line like: USD: $X, EUR: €X, GBP: £X. Nothing else: {data}"
        )

    @gl.public.view
    def get_top_coins_summary(self) -> str:
        """Get a quick price summary of the top 5 cryptocurrencies."""
        data = gl.get_webpage(
            "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,binancecoin,solana,cardano"
            "&vs_currencies=usd&include_24hr_change=true"
        )
        return gl.exec_prompt(
            f"From this data, list the current USD price and 24h change for each of these coins: "
            f"Bitcoin, Ethereum, BNB, Solana, Cardano. Format each on a new line: {data}"
        )
