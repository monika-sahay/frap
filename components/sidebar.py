from frap.components.sidebarComponents import SidebarStyle, SidebarComponents


# Define a simplified interface for routes
def Sidebar(items, style_config):
    return SidebarComponents(items=items, style=SidebarStyle(**style_config))
