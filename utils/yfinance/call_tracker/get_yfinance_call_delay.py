from utils.yfinance.call_tracker import state


def get_yfinance_call_delay():
    """Return the configured delay between tracked yfinance calls."""
    return state._yfinance_call_delay_seconds
