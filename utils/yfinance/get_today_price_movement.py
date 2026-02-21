import yfinance as yf

from utils.yfinance.call_tracker.log_yfinance_call import log_yfinance_call


def get_today_price_movement(symbol, ticker=None, return_full_data=False):
    """Fetch intraday close prices for the current trading day."""
    if ticker is None:
        log_yfinance_call(f"yf.Ticker('{symbol}')")
        ticker = yf.Ticker(symbol)

    log_yfinance_call(f"yf.Ticker('{symbol}').history(period='1d', interval='5m')")
    intraday = ticker.history(period="1d", interval="5m")
    if intraday.empty:
        raise ValueError(f"No intraday data found for stock symbol '{symbol}'")

    intraday = intraday.dropna(subset=["Close"])
    if intraday.empty:
        raise ValueError(f"No intraday close prices found for stock symbol '{symbol}'")

    if return_full_data:
        return intraday

    return intraday["Close"]
