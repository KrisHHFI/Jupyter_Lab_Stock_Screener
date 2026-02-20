_yfinance_call_count = 0


def reset_yfinance_call_count():
    """Reset tracked yfinance call count for a fresh run."""
    global _yfinance_call_count
    _yfinance_call_count = 0


def increment_yfinance_call_count():
    """Increment and return the tracked yfinance call count."""
    global _yfinance_call_count
    _yfinance_call_count += 1
    return _yfinance_call_count


def get_yfinance_call_count():
    """Return current tracked yfinance call count."""
    return _yfinance_call_count
