import pandas as pd

from utils.formatting.truncate_two_decimals import truncate_two_decimals
from utils.printing.display_styled_table import display_styled_table
from utils.printing.print_header import print_header


def print_stock_info(stock_data):
    """Print ranked screener result information in a clean, readable format."""
    print_header("Stock Screener", main_header=True)

    print_header("Filters")

    display_styled_table(
        pd.DataFrame(
            [
                ["Filter Region", stock_data["region_filter"]],
                ["Filter Industry", stock_data["industry_filter"]],
                ["Filter Min Market Cap", stock_data["min_market_cap_filter"]],
            ],
            columns=["Metric", "Value"],
        )
    )

    print_header("Sorting")
    display_styled_table(
        pd.DataFrame(
            [
                ["Sorted By", stock_data["sorting_field"]],
                ["Direction", stock_data["sorting_direction"]],
            ],
            columns=["Metric", "Value"],
        )
    )

    print_header("Results")

    ranked_table = pd.DataFrame(
        [
            [
                item["rank"],
                item["symbol"],
                item["company_name"],
                truncate_two_decimals(item["pe_ratio"]),
                item["market_cap"],
                truncate_two_decimals(item["current_price"]),
            ]
            for item in stock_data["stocks"]
        ],
        columns=["Rank", "Symbol", "Company", "P/E Ratio", "Market Cap", "Current Price"],
    )
    display_styled_table(ranked_table)
