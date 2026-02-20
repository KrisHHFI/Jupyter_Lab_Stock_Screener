# BasicStockData3 — Agent Notes

## Project Overview
This project is a modular Python + Jupyter workflow for viewing stock information and charting today's intraday price movement.

Main flow:
- Cell 1 in `main.ipynb` runs the app flow.
- Data is fetched from Yahoo Finance via `yfinance`.
- Text output and chart rendering are handled by separate function modules.

## Coding Rules
- Keep the code modular.
- Each function should be in its own file.
- Notebook cells should stay thin and primarily orchestrate imports + function calls.
- Prefer clear, descriptive file names that match the function they contain.
- Every utility/function file must be declared in this AGENTS.md file.
- Whenever a file is added, removed, or renamed, update all relevant AGENTS.md sections immediately (Current Function File Pattern, Folder Structure, and File Responsibilities).

## Current Function File Pattern
Examples in this project:
- `utils/get_stock_info.py`
- `utils/get_today_price_movement.py`
- `utils/print_stock_info.py`
- `utils/print_data_collected.py`
- `utils/plot_today_price_movement.py`
- `utils/format_market_cap.py`
- `utils/truncate_two_decimals.py`
- `utils/yfinance_call_tracker.py`

## Folder Structure
```text
BasicStockData3/
├── main.ipynb
├── AGENTS.md
└── utils/
	├── __init__.py
	├── get_stock_info.py
	├── get_today_price_movement.py
	├── print_stock_info.py
	├── print_data_collected.py
	├── plot_today_price_movement.py
	├── format_market_cap.py
	├── truncate_two_decimals.py
	└── yfinance_call_tracker.py
```

## File Responsibilities
- `main.ipynb`: Thin orchestration only (imports + top-level calls).
- `utils/get_stock_info.py`: Fetches current stock fundamentals and price snapshot.
- `utils/get_today_price_movement.py`: Fetches intraday close series and applies exchange-local timezone conversion.
- `utils/print_stock_info.py`: Console/text presentation of stock summary fields.
- `utils/print_data_collected.py`: Prints the data collection timestamp for display after chart rendering.
- `utils/plot_today_price_movement.py`: Chart rendering and axis formatting rules.
- `utils/format_market_cap.py`: Market cap human-readable formatting helper.
- `utils/truncate_two_decimals.py`: Numeric truncation helper used across modules.
- `utils/yfinance_call_tracker.py`: Tracks yfinance API-call usage count for each notebook run.
