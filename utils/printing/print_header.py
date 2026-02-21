def print_header(title):
    """Print a consistent section header."""
    text = title.upper()
    border = "=" * (len(text) + 4)
    print()
    print(f"  {text}")
    print(border)
