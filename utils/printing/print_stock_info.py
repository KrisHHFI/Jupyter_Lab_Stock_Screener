import pandas as pd

from utils.printing.print_header import print_header


def print_stock_info(stock_data):
    """Print ranked screener result information in a clean, readable format."""
    print_header("Stock Screener", main_header=True)

    print_header("Filters")

    print(
        pd.DataFrame(
            [
                ["Filter Region", stock_data["region_filter"]],
                ["Filter Industry", stock_data["industry_filter"]],
                ["Filter Min Market Cap", stock_data["min_market_cap_filter"]],
            ],
            columns=["Metric", "Value"],
        ).to_string(index=False)
    )
    print()

    print_header("Sorting")
    print(
        pd.DataFrame(
            [
                ["Sorted By", stock_data["sorting_field"]],
                ["Direction", stock_data["sorting_direction"]],
            ],
            columns=["Metric", "Value"],
        ).to_string(index=False)
    )
    print()

    print_header("Results")

    ranked_table = pd.DataFrame(
        [
            [
                item["rank"],
                item["symbol"],
                item["company_name"],
                item["pe_ratio"],
                item["market_cap"],
                item["current_price"],
            ]
            for item in stock_data["stocks"]
        ],
        columns=["Rank", "Symbol", "Company", "P/E Ratio", "Market Cap", "Current Price"],
    )
    print(ranked_table.to_string(index=False))
