import yfinance as yf

from utils.yfinance.derive_dividend_values import derive_dividend_values
from utils.yfinance.extract_prices import extract_prices
from utils.formatting.format_market_cap import format_market_cap
from utils.formatting.truncate_two_decimals import truncate_two_decimals
from utils.yfinance.call_tracker.log_yfinance_call import log_yfinance_call


def get_stock_info(symbol, ticker=None, intraday_data=None):
    """Fetch stock info and latest prices. Returns a dictionary."""
    if ticker is None:
        log_yfinance_call(f"yf.Ticker('{symbol}')")
        ticker = yf.Ticker(symbol)

    log_yfinance_call(f"yf.Ticker('{symbol}').info")
    info = ticker.info
    company_name = info.get("shortName", symbol)
    market_cap = format_market_cap(info.get("marketCap", "N/A"))
    pe_ratio = truncate_two_decimals(info.get("trailingPE", "N/A"))
    week52_high = truncate_two_decimals(info.get("fiftyTwoWeekHigh", "N/A"))
    week52_low = truncate_two_decimals(info.get("fiftyTwoWeekLow", "N/A"))
    dividend, qtrly_div_amt = derive_dividend_values(info)

    data = intraday_data
    if data is None:
        log_yfinance_call(f"yf.Ticker('{symbol}').history(period='1d')")
        data = ticker.history(period="1d")

    if data.empty:
        raise ValueError(f"No data found for stock symbol '{symbol}'")

    prices = extract_prices(data, intraday_data_provided=intraday_data is not None)
    close_price = prices["current_price"]

    dividend_yield_pct = "N/A"
    if isinstance(dividend, (int, float)) and isinstance(close_price, (int, float)) and close_price != 0:
        dividend_yield_pct = truncate_two_decimals((dividend / close_price) * 100)

    return {
        "company_name": company_name,
        "symbol": symbol,
        **prices,
        "market_cap": market_cap,
        "pe_ratio": pe_ratio,
        "52_week_high": week52_high,
        "52_week_low": week52_low,
        "dividend": dividend,
        "dividend_yield_pct": dividend_yield_pct,
        "qtrly_div_amt": qtrly_div_amt,
    }
