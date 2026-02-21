from IPython.display import display


def display_styled_table(df):
    """Display a bordered, notebook-friendly styled table."""
    styled = (
        df.style.hide(axis="index")
        .set_properties(**{"text-align": "left", "padding": "6px"})
        .set_table_styles(
            [
                {"selector": "table", "props": "border-collapse: collapse; width: 100%;"},
                {
                    "selector": "th",
                    "props": "border: 1px solid #888; background-color: #ffffff; color: #000000; text-align: left; padding: 6px;",
                },
                {"selector": "td", "props": "border: 1px solid #888; padding: 6px;"},
            ]
        )
    )
    display(styled)
