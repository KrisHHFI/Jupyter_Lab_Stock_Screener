import yfinance as yf

from utils.formatting.format_market_cap import format_market_cap
from utils.formatting.truncate_two_decimals import truncate_two_decimals
from utils.yfinance.call_tracker.log_yfinance_call import log_yfinance_call


def enrich_with_info(stock_data, quote):
    symbol = stock_data["symbol"]
    if symbol == "N/A":
        return stock_data

    ticker = yf.Ticker(symbol)
    log_yfinance_call(f"yf.Ticker('{symbol}').info")
    info = ticker.info

    stock_data["company_name"] = info.get("shortName", stock_data["company_name"])
    stock_data["current_price"] = truncate_two_decimals(
        info.get("currentPrice", quote.get("regularMarketPrice", "N/A"))
    )
    stock_data["market_cap"] = format_market_cap(info.get("marketCap", quote.get("marketCap", "N/A")))
    stock_data["pe_ratio"] = truncate_two_decimals(info.get("trailingPE", quote.get("trailingPE", "N/A")))
    return stock_data
