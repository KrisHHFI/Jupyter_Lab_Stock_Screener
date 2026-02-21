from utils.formatting.truncate_two_decimals import truncate_two_decimals


def extract_prices(data, intraday_data_provided):
    if intraday_data_provided:
        open_price = data["Open"].iloc[0]
        high_price = data["High"].max()
        low_price = data["Low"].min()
        close_price = data["Close"].iloc[-1]
    else:
        latest = data.iloc[-1]
        open_price = latest["Open"]
        high_price = latest["High"]
        low_price = latest["Low"]
        close_price = latest["Close"]

    return {
        "open": truncate_two_decimals(open_price),
        "high": truncate_two_decimals(high_price),
        "low": truncate_two_decimals(low_price),
        "current_price": truncate_two_decimals(close_price),
    }
