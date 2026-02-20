from datetime import datetime

import pandas as pd


def print_data_collected(collected_at=None, yfinance_call_count=None):
    """Print usage + data collection table two lines below prior output."""
    timestamp = collected_at or datetime.now()
    print("\n\n", end="")

    usage_rows = [
        ["yfinance calls made", yfinance_call_count if yfinance_call_count is not None else "N/A"],
        ["Data collected on", timestamp.strftime("%Y-%m-%d %H:%M:%S")],
    ]
    usage_table = pd.DataFrame(usage_rows, columns=["Metric", "Value"])
    print(usage_table.to_string(index=False))
