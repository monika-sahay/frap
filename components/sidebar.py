# sidebar.py

"""
This module defines classes for creating a customizable HTML sidebar.

Classes:
    SidebarItem: A class representing an item in the sidebar.
    SidebarStyle: A class representing the style configuration for the sidebar.
    BaseSidebar: A base class representing a customizable sidebar in HTML.
    Sidebar: A class representing a customizable sidebar in HTML, inheriting from BaseSidebar.
"""


from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class SidebarItem:
    """
    A class representing an item in the sidebar.

    Attributes:
        url (str): The URL associated with the sidebar item.
        label (str): The label or text displayed for the sidebar item.
    """
    url: str
    label: str


@dataclass
class SidebarStyle:
    """
    A class representing the style configuration for the sidebar.

    Attributes:
        width (int): The width of the sidebar in pixels.
        background_color (str): Background color of the sidebar in hexadecimal format.
        text_color (str): Text color of the items in the sidebar in hexadecimal format.
        hover_color (str): Color of the item when hovered in hexadecimal format.
        orientation (str): The orientation of the sidebar, either 'vertical' or 'horizontal'.
        top (Optional[int]): The CSS 'top' property for the sidebar. None if not set.
        left (Optional[int]): The CSS 'left' property for the sidebar. None if not set.
        right (Optional[int]): The CSS 'right' property for the sidebar. None if not set.
        bottom (Optional[int]): The CSS 'bottom' property for the sidebar. None if not set.
    """
    width: int
    background_color: str
    text_color: str
    hover_color: str
    orientation: str
    top: Optional[int] = None
    left: Optional[int] = None
    right: Optional[int] = None
    bottom: Optional[int] = None


@dataclass
class BaseSidebar:
    """
    A base class representing a customizable sidebar in HTML.

    Attributes:
        items (List[SidebarItem]): A list of SidebarItem instances representing items in the sidebar.
        style (SidebarStyle): The style configuration for the sidebar.
    """
    items: List['SidebarItem']
    style: SidebarStyle = field(default_factory=lambda: SidebarStyle(width=200,
                                                                     background_color="#f5f5f5",
                                                                     text_color="#818181",
                                                                     hover_color="#f1f1f1",
                                                                     orientation="vertical"))


@dataclass
class Sidebar(BaseSidebar):
    """
    A class representing a customizable sidebar in HTML.

    Attributes:
        items (List[dict]): A list of dictionaries, each representing an item in the sidebar.
    """

    def render_html(self):
        """
        Renders the HTML representation of the sidebar.

        Returns:
            str: HTML representation of the sidebar.
        """
        sidebar_html = f'''<div class="sidebar" style="width: {self.style.width}px;
                        background-color: {self.style.background_color};'''
        if self.style.top is not None:
            sidebar_html += f" top: {self.style.top}px;"
        if self.style.left is not None:
            sidebar_html += f" left: {self.style.left}px;"
        if self.style.right is not None:
            sidebar_html += f" right: {self.style.right}px;"
        if self.style.bottom is not None:
            sidebar_html += f" bottom: {self.style.bottom}px;"
        if self.style.orientation == "horizontal":
            sidebar_html += ' display: flex; flex-direction: row;">'
        else:
            sidebar_html += '">'

        for item in self.items:
            sidebar_html += f"""<a href="{item.url}"
                            style="color: {self.style.text_color};
                            display: block;
                            text-decoration: none;
                            padding: 6px 8px 6px 16px;">{item.label}</a>"""
        sidebar_html += "</div>"
        return sidebar_html

    def render_css(self):
        """
        Generate CSS styles for the sidebar.

        Returns:
            str: A string containing CSS styles for the sidebar.
        """
        sidebar_css = f"""
        .sidebar {{
            position: fixed;
            { "top: " + str(self.style.top) + "px;" if self.style.top is not None else "" }
            { "left: " + str(self.style.left) + "px;" if self.style.left is not None else "" }
            { "right: " + str(self.style.right) + "px;" if self.style.right is not None else "" }
            { "bottom: " + str(self.style.bottom) + "px;" if self.style.bottom is not None else "" }
            { "height: 100%;" if self.style.orientation == "vertical" else "height: auto;" }
            { "width: " + str(self.style.width) + "px;" if self.style.orientation == "vertical" else "width: 100%;" }
            { "flex-direction: column;" if self.style.orientation == "vertical" else "flex-direction: row;" }
            background-color: {self.style.background_color};
            { "overflow-x: hidden;" if self.style.orientation == "vertical" else "overflow-y: hidden;" }
            padding-top: 20px;
        }}

        .sidebar a {{
            color: {self.style.text_color};
        }}

        .sidebar a:hover {{
            color: {self.style.hover_color};
        }}
        """
        return sidebar_css
