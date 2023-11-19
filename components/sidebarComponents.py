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
class ColorScheme:
    """A class representing the color scheme for the sidebar."""
    background_color: str
    text_color: str
    hover_color: str


@dataclass
class LayoutProperties:
    """A class representing the layout properties for the sidebar."""
    width: int
    orientation: str
    top: Optional[int] = None
    left: Optional[int] = None
    right: Optional[int] = None
    bottom: Optional[int] = None


@dataclass
class SidebarStyle:
    """
    A class representing the style configuration for the sidebar.

    Attributes:
        color_scheme (ColorScheme): The color scheme for the sidebar.
        layout_properties (LayoutProperties): The layout properties for the sidebar.
    """
    color_scheme: ColorScheme
    layout_properties: LayoutProperties


@dataclass
class SidebarComponents:
    """
    A class representing a customizable sidebar in HTML.

    Attributes:
        items (List[SidebarItem]): A list of SidebarItem instances representing items in the sidebar.
        style (SidebarStyle): The style configuration for the sidebar.
    """

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

    items: List[SidebarItem]
    style: SidebarStyle = field(default_factory=lambda: SidebarStyle(
        color_scheme=ColorScheme(
            background_color="#f5f5f5",
            text_color="#818181",
            hover_color="#f1f1f1"
        ),
        layout_properties=LayoutProperties(
            width=200,
            orientation="vertical"
        )
    ))

    def render_html(self):
        """
        Renders the HTML representation of the sidebar.

        Returns:
            str: HTML representation of the sidebar.
        """
        sidebar_html = f'''<div class="sidebar" style="width: {self.style.layout_properties.width}px;
                        background-color: {self.style.color_scheme.background_color};'''
        if self.style.layout_properties.top is not None:
            sidebar_html += f" top: {self.style.layout_properties.top}px;"
        if self.style.layout_properties.left is not None:
            sidebar_html += f" left: {self.style.layout_properties.left}px;"
        if self.style.layout_properties.right is not None:
            sidebar_html += f" right: {self.style.layout_properties.right}px;"
        if self.style.layout_properties.bottom is not None:
            sidebar_html += f" bottom: {self.style.layout_properties.bottom}px;"
        if self.style.layout_properties.orientation == "horizontal":
            sidebar_html += ' display: flex; flex-direction: row;">'
        else:
            sidebar_html += '">'

        for item in self.items:
            sidebar_html += f"""<a href="{item.url}"
                            style="color: {self.style.color_scheme.text_color};
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
            { "top: " + str(self.style.layout_properties.top) + "px;" if self.style.layout_properties.top is not None else "" }
            { "left: " + str(self.style.layout_properties.left) + "px;" if self.style.layout_properties.left is not None else "" }
            { "right: " + str(self.style.layout_properties.right) + "px;" if self.style.layout_properties.right is not None else "" }
            { "bottom: " + str(self.style.layout_properties.bottom) + "px;" if self.style.layout_properties.bottom is not None else "" }
            { "height: 100%;" if self.style.layout_properties.orientation == "vertical" else "height: auto;" }
            { "width: " + str(self.style.layout_properties.width) + "px;" if self.style.layout_properties.orientation == "vertical" else "width: 100%;" }
            { "flex-direction: column;" if self.style.layout_properties.orientation == "vertical" else "flex-direction: row;" }
            background-color: {self.style.color_scheme.background_color};
            { "overflow-x: hidden;" if self.style.layout_properties.orientation == "vertical" else "overflow-y: hidden;" }
            padding-top: 20px;
        }}

        .sidebar a {{
            color: {self.style.color_scheme.text_color};
        }}

        .sidebar a:hover {{
            color: {self.style.color_scheme.hover_color};
        }}
        """
        return sidebar_css
