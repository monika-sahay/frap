from frap.components.sidebarcomponents import SidebarStyle, SidebarComponents


# Define a simplified interface for routes
def sidebar(items, style_config):
    return SidebarComponents(items=items, style=SidebarStyle(**style_config))
