"""
Template Rendering and Environment Setup

This module handles template rendering for the Frap web framework and sets up the template environment.
It provides functions to render HTML templates with dynamic data.

Usage:
    To render a template, use the `render_template(page, **kwargs)` function, where `page` is the name of the
    template file to render, and `kwargs` are keyword arguments containing data to be passed to the template.

Example:
    To render an 'index.html' template with dynamic data, use:

    render_template('index.html', title='Welcome', content='Hello, Frap!')

Functions:
    - render_template(page, **kwargs): Renders an HTML template with dynamic data and returns the rendered content.

Dependencies:
    - jinja2: Templating engine for rendering HTML templates.
    - os: Provides access to file system operations for defining the template directory path.

"""
# templates.py
from jinja2 import Environment, FileSystemLoader
import os

# Define the template directory path
template_dir = os.path.join(os.path.dirname(__file__), '../templates')
env = Environment(loader=FileSystemLoader(template_dir))

def render_template(page, **kwargs):
    """
    Render an HTML template with dynamic data.

    Args:
        page (str): The name of the template file to render.
        **kwargs: Keyword arguments containing data to be passed to the template.

    Returns:
        str: The rendered HTML content as a string.
    """
    template = env.get_template(page)
    return template.render(**kwargs)



if __name__ == '__main__':
    contents = os.listdir(template_dir)

    for item in contents:
        item_path = os.path.join(template_dir, item)
        if os.path.isfile(item_path):
            print(f"File: {item}")
        elif os.path.isdir(item_path):
            print(f"Directory: {item}")