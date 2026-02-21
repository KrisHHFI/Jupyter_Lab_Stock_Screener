from utils.formatting.truncate_two_decimals import truncate_two_decimals


def derive_dividend_values(info):
    qtrly_div_amt = info.get("lastDividendValue", "N/A")
    dividend_rate = info.get("dividendRate")

    if qtrly_div_amt == "N/A" and isinstance(dividend_rate, (int, float)):
        qtrly_div_amt = dividend_rate / 4

    qtrly_div_amt = truncate_two_decimals(qtrly_div_amt)

    dividend = info.get("dividendRate", "N/A")
    if dividend == "N/A" and isinstance(qtrly_div_amt, (int, float)):
        dividend = qtrly_div_amt * 4

    return truncate_two_decimals(dividend), qtrly_div_amt
