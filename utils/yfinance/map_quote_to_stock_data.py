from utils.formatting.format_market_cap import format_market_cap
from utils.formatting.truncate_two_decimals import truncate_two_decimals


def map_quote_to_stock_data(quote, rank):
    symbol = quote.get("symbol", "N/A")
    return {
        "rank": rank,
        "company_name": quote.get("shortName", symbol),
        "symbol": symbol,
        "current_price": truncate_two_decimals(quote.get("regularMarketPrice", "N/A")),
        "market_cap": format_market_cap(quote.get("marketCap", "N/A")),
        "pe_ratio": truncate_two_decimals(quote.get("trailingPE", "N/A")),
    }
