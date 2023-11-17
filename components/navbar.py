# navbar.py

"""
This module defines a class for creating a simple HTML/CSS navbar.

Classes:
    Navbar: A class representing a simple HTML/CSS navbar.
"""


class Navbar:
    """
A class representing a simple HTML/CSS navbar.

    Attributes:
        items (list): A list of dictionaries, each representing an item in the navbar.
        background_color (str): Background color of the navbar in hexadecimal format.
        text_color (str): Text color of the items in the navbar in hexadecimal format.
        hover_color (str): Color of the item when hovered in hexadecimal format.
    """

    def __init__(
        self, items, background_color="#333", text_color="#fff", hover_color="#4CAF50"
    ):
        """
        Initializes the Navbar instance with provided parameters.

        Args:
            items (list): A list of dictionaries, each representing an item in the navbar.
            background_color (str, optional): Background color of the navbar. Defaults to "#333".
            text_color (str, optional): Text color of the items in the navbar. Defaults to "#fff".
            hover_color (str, optional): Color of the item when hovered. Defaults to "#4CAF50".
        """
        self.items = items
        self.background_color = background_color
        self.text_color = text_color
        self.hover_color = hover_color

    def render_html(self):
        """
        Renders the HTML representation of the navbar.

        Returns:
            str: HTML representation of the navbar.
        """
        navbar_html = f'<div class="navbar" style="background-color: {self.background_color};">'
        for item in self.items:
            navbar_html += f"""<a href="{item["url"]}"
                            style="color: {self.text_color};
                            padding: 14px 16px;
                            text-decoration: none;">{item["label"]}</a>"""
        navbar_html += "</div>"
        return navbar_html

    def render_css(self):
        """
        Renders the CSS representation of the navbar.

        Returns:
            str: CSS representation of the navbar.
        """
        navbar_css = f"""
            .navbar {{
                overflow: hidden;
            }}

            .navbar a {{
                float: left;
                display: block;
                color: {self.text_color};
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
            }}

            .navbar a:hover {{
                background-color: {self.hover_color};
                color: black;
            }}
        """
        return navbar_css
