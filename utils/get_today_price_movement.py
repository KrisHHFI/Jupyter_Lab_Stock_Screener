import yfinance as yf

from utils.yfinance_call_tracker import increment_yfinance_call_count


def get_today_price_movement(symbol, ticker=None, return_full_data=False):
    """Fetch intraday close prices for the current trading day."""
    if ticker is None:
        increment_yfinance_call_count()
        ticker = yf.Ticker(symbol)

    increment_yfinance_call_count()
    intraday = ticker.history(period="1d", interval="5m")
    if intraday.empty:
        raise ValueError(f"No intraday data found for stock symbol '{symbol}'")

    intraday = intraday.dropna(subset=["Close"])
    if intraday.empty:
        raise ValueError(f"No intraday close prices found for stock symbol '{symbol}'")

    if return_full_data:
        return intraday

    return intraday["Close"]
