import yfinance as yf

from utils.const.filters import INDUSTRY_FILTER, MIN_MARKET_CAP_FILTER, REGION_FILTER


def build_fast_food_query(min_market_cap=MIN_MARKET_CAP_FILTER):
    return yf.EquityQuery(
        "and",
        [
            yf.EquityQuery("eq", ["region", REGION_FILTER]),
            yf.EquityQuery("eq", ["industry", INDUSTRY_FILTER]),
            yf.EquityQuery("gte", ["intradaymarketcap", min_market_cap]),
        ],
    )
