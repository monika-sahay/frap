# templates.py
from jinja2 import Environment, FileSystemLoader
import os

# Define the template directory path
template_dir = os.path.join(os.path.dirname(__file__), '../templates')
env = Environment(loader=FileSystemLoader(template_dir))

def render_template(page, **kwargs):
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