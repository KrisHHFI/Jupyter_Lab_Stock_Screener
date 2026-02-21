import math


def truncate_two_decimals(value):
    """Truncate a number to 2 decimal places without rounding."""
    try:
        return math.trunc(float(value) * 100) / 100
    except (TypeError, ValueError):
        return value
