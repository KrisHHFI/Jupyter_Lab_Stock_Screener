import pandas as pd


def print_stock_info(stock_data):
    """Print stock information in a clean, readable format."""
    title = f"{stock_data['company_name']} ({stock_data['symbol']})"
    print("=" * len(title))
    print(title.upper())
    print("=" * len(title))

    table_rows = [
        ["Current Price", stock_data["current_price"]],
        ["Open", stock_data["open"]],
        ["High", stock_data["high"]],
        ["Low", stock_data["low"]],
        ["Market Cap", stock_data["market_cap"]],
        ["P/E Ratio", stock_data["pe_ratio"]],
        ["52 Week High", stock_data["52_week_high"]],
        ["52 Week Low", stock_data["52_week_low"]],
        ["Dividend", stock_data["dividend"]],
        ["Dividend Yield %", stock_data["dividend_yield_pct"]],
        ["Qtrly Div Amt", stock_data["qtrly_div_amt"]],
    ]

    stock_table = pd.DataFrame(table_rows, columns=["Metric", "Value"])
    print(stock_table.to_string(index=False))
