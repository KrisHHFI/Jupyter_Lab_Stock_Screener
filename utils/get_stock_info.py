import yfinance as yf

from utils.format_market_cap import format_market_cap
from utils.truncate_two_decimals import truncate_two_decimals
from utils.yfinance_call_tracker import increment_yfinance_call_count


def get_stock_info(symbol, ticker=None, intraday_data=None):
    """Fetch stock info and latest prices. Returns a dictionary."""
    if ticker is None:
        increment_yfinance_call_count()
        ticker = yf.Ticker(symbol)

    increment_yfinance_call_count()
    info = ticker.info
    company_name = info.get("shortName", symbol)
    market_cap = format_market_cap(info.get("marketCap", "N/A"))
    pe_ratio = truncate_two_decimals(info.get("trailingPE", "N/A"))
    week52_high = truncate_two_decimals(info.get("fiftyTwoWeekHigh", "N/A"))
    week52_low = truncate_two_decimals(info.get("fiftyTwoWeekLow", "N/A"))

    qtrly_div_amt = info.get("lastDividendValue", "N/A")
    if qtrly_div_amt == "N/A":
        dividend_rate = info.get("dividendRate")
        if isinstance(dividend_rate, (int, float)):
            qtrly_div_amt = truncate_two_decimals(dividend_rate / 4)
    qtrly_div_amt = truncate_two_decimals(qtrly_div_amt)

    dividend = info.get("dividendRate", "N/A")
    if dividend == "N/A" and isinstance(qtrly_div_amt, (int, float)):
        dividend = truncate_two_decimals(qtrly_div_amt * 4)
    dividend = truncate_two_decimals(dividend)

    data = intraday_data
    if data is None:
        increment_yfinance_call_count()
        data = ticker.history(period="1d")
    if data.empty:
        raise ValueError(f"No data found for stock symbol '{symbol}'")

    if intraday_data is not None:
        open_price = truncate_two_decimals(data["Open"].iloc[0])
        high_price = truncate_two_decimals(data["High"].max())
        low_price = truncate_two_decimals(data["Low"].min())
        close_price = truncate_two_decimals(data["Close"].iloc[-1])
    else:
        open_price = truncate_two_decimals(data["Open"].iloc[-1])
        high_price = truncate_two_decimals(data["High"].iloc[-1])
        low_price = truncate_two_decimals(data["Low"].iloc[-1])
        close_price = truncate_two_decimals(data["Close"].iloc[-1])

    dividend_yield_pct = "N/A"
    if isinstance(dividend, (int, float)) and isinstance(close_price, (int, float)) and close_price != 0:
        dividend_yield_pct = truncate_two_decimals((dividend / close_price) * 100)

    return {
        "company_name": company_name,
        "symbol": symbol,
        "current_price": close_price,
        "open": open_price,
        "high": high_price,
        "low": low_price,
        "market_cap": market_cap,
        "pe_ratio": pe_ratio,
        "52_week_high": week52_high,
        "52_week_low": week52_low,
        "dividend": dividend,
        "dividend_yield_pct": dividend_yield_pct,
        "qtrly_div_amt": qtrly_div_amt,
    }
