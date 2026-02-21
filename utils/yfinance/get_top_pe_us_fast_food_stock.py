import yfinance as yf

from utils.const.filters import INDUSTRY_LABEL, MIN_MARKET_CAP_FILTER, REGION_FILTER, SCREEN_SIZE_FILTER, TOP_N_FILTER
from utils.const.sorting import SORT_ASCENDING, SORT_FIELD_KEY, SORTING_DIRECTION, SORTING_FIELD
from utils.formatting.format_market_cap import format_market_cap
from utils.yfinance.build_fast_food_query import build_fast_food_query
from utils.yfinance.enrich_with_info import enrich_with_info
from utils.yfinance.map_quote_to_stock_data import map_quote_to_stock_data
from utils.yfinance.call_tracker.log_yfinance_call import log_yfinance_call


def get_top_pe_us_fast_food_stock(
    min_market_cap=MIN_MARKET_CAP_FILTER,
    top_n=TOP_N_FILTER,
    screen_size=SCREEN_SIZE_FILTER,
    verify_with_info=False,
):
    """Return top-N highest P/E US restaurants stocks with medium+ market cap."""
    query = build_fast_food_query(min_market_cap)

    log_yfinance_call("yf.screen(query=US + Restaurants + min market cap)")
    result = yf.screen(
        query,
        size=max(screen_size, top_n),
        sortField=SORT_FIELD_KEY,
        sortAsc=SORT_ASCENDING,
    )

    quotes = result.get("quotes", [])
    if not quotes:
        raise ValueError("No matching stocks found for the selected filters.")

    ranked_stocks = [
        enrich_with_info(map_quote_to_stock_data(quote, rank=idx), quote)
        if verify_with_info
        else map_quote_to_stock_data(quote, rank=idx)
        for idx, quote in enumerate(quotes[:top_n], start=1)
    ]

    return {
        "top_n": top_n,
        "region_filter": REGION_FILTER.upper(),
        "industry_filter": INDUSTRY_LABEL,
        "min_market_cap_filter": format_market_cap(min_market_cap),
        "sorting_field": SORTING_FIELD,
        "sorting_direction": SORTING_DIRECTION,
        "stocks": ranked_stocks,
    }
