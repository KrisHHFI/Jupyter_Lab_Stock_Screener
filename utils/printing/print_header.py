def print_header(title, main_header=False):
    """Print a section header; optionally use main header style."""
    text = title.upper()
    border = "=" * (len(text) + 4)
    print()
    if main_header:
        print(border)
    print(f"  {text}")
    print(border)
