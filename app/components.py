# components.py
"""
Custom HTML and CSS components for building web interfaces.

This module defines several classes for creating customizable HTML and CSS components,
including forms, buttons, sliders, star ratings, sidebars, and navigation bars.

Classes:
    - CustomSlider: Represents a customizable slider element.
    - Form: Represents an HTML form with customizable fields and buttons.
    - Button: Represents an HTML button.
    - LoginForm: Represents a login form derived from the Form class.
    - StarRating: Represents a star rating component.
    - Sidebar: Represents a customizable sidebar in HTML.
    - Navbar: Represents a simple HTML/CSS navbar.
    - FeedbackForm: Represents a feedback form derived from the Form class.
"""


class CustomSlider:
    """
    A class representing a custom slider element.

    Attributes:
        label (str): The label or description for the slider.
        min_value (int): The minimum value of the slider.
        max_value (int): The maximum value of the slider.
        default_value (int): The initial or default value of the slider.
        step (int): The step size for incrementing or decrementing the slider value.
    """
    def __init__(self, slider_config):
        """
        Initialize a CustomSlider instance.

        Parameters:
        - label (str): The label or description for the slider.
        - min_value (int): The minimum value of the slider.
        - max_value (int): The maximum value of the slider.
        - default_value (int): The initial or default value of the slider.
        - step (int): The step size for incrementing or decrementing the
            slider value.
        """
        self.label = slider_config["label"]
        self.min_value = slider_config["min_value"]
        self.max_value = slider_config["max_value"]
        self.default_value = slider_config["default_value"]
        self.step = slider_config["step"]

    def render_html(self):
        """
        Generate HTML markup for the custom slider element.

        Returns:
        - str: A string containing HTML markup for the custom slider element.
        """
        html = f"""
            <label>{self.label}</label>
            <input type="range" id="{self.label}" name="{self.label}"
                   min="{self.min_value}" max="{self.max_value}"
                   value="{self.default_value}" step="{self.step}">
            <span id="{self.label}-value">{self.default_value}</span>
            <br>
        """
        return html

    def render_js(self):
        """
        Generate JavaScript code for the custom slider element.

        Returns:
        - str: A string containing JavaScript code for updating the slider's value display.
        """
        js = f"""
            $(document).ready(function() {{
                $('input[type="range"]').on('input', function() {{
                    var label = $(this).attr('id');
                    var value = $(this).val();
                    $('#{self.label}-value').text(value);
                }});
            }});
        """
        return js


class Form:
    """
    A class representing an HTML form with customizable fields and buttons.

    Attributes:
        action (str): The action attribute of the form specifying where to send the form-data when the form is submitted.
        method (str): The HTTP method to be used when sending form-data.
        fields (list): A list of dictionaries, each representing a field in the form.
        buttons (list): A list of Button instances representing buttons in the form.
        custom_components (list): A list of custom HTML components to be included in the form.
    """

    def __init__(self, action, method="POST"):
        """
        Initializes the Form instance with the provided parameters.

        Args:
            action (str): The action attribute of the form specifying
            where to send the form-data when the form is submitted.
            method (str, optional): The HTTP method to be used
            when sending form-data. Defaults to "POST".
        """
        self.action = action
        self.method = method
        self.fields = []
        self.buttons = []
        self.custom_components = []

    def add_field(self, label, name, input_type="text"):
        """
        Adds a field to the form.

        Args:
            label (str): The label for the field.
            name (str): The name attribute of the input field.
            input_type (str, optional): The type of the input field. Defaults to "text".
        """
        field = {"label": label, "name": name, "type": input_type}
        self.fields.append(field)

    def add_button(self, label, button_type="submit"):
        """
        Adds a button to the form.

        Args:
            label (str): The label for the button.
            button_type (str, optional): The type of the button. Defaults to "submit".
        """
        button = Button(label, button_type)
        self.buttons.append(button)

    def add_custom_component(self, custom_html):
        """
        Adds custom HTML components to the form.

        Args:
            custom_html (str): Custom HTML component to be included in the form.
        """
        self.custom_components.append(custom_html)

    def render_html(self):
        """
        Renders the HTML representation of the form.

        Returns:
            str: HTML representation of the form.
        """
        html = f"""
            <form action="{self.action}" method="{self.method}" class="dynamic-form">
        """
        for field in self.fields:
            label = field["label"]
            name = field["name"]
            input_type = field["type"]
            input_id = f"form-{name}"
            html += f"""
                <div class="form-group">
                    <label for="{input_id}">{label}:</label>
                    <input type="{input_type}" name="{name}" id="{input_id}" class="form-control">
                </div>
            """

        for custom_component in self.custom_components:
            html += custom_component

        for button in self.buttons:
            button_html = button.render_html()
            html += button_html

        html += """
                </form>
        """
        return html

    def render_css(self, style_properties=None):
        """
        Generate CSS styles for the dynamic form.

        Parameters:
        - style_properties (dict): A dictionary containing CSS style properties for the form.

        Returns:
        - str: A string containing CSS styles for the dynamic form.
        """
        default_style = {
            "width": "50%",
            "margin_top": "50px",
            "left": "auto",
            "right": "auto",
            "top": "auto",
            "bottom": "auto",
            "z_index": "auto",
            "overlap": False,
        }

        if style_properties is not None:
            # Update the default style with user-provided values
            default_style.update(style_properties)
        overlap_value = "hidden" if default_style["overlap"] else "visible"
        css = f"""
            /* Custom styles for the dynamic form */
            .dynamic-form {{
                width: {default_style["width"]};
                margin: auto;
                padding: 20px;
                border: 1px solid #ccc;
                border-radius: 5px;
                margin-top: {default_style["margin_top"]};
                position: absolute;
                left: {default_style["left"]};
                right: {default_style["right"]};
                top: {default_style["top"]};
                bottom: {default_style["bottom"]};
                z-index: {default_style["z_index"]};
                visibility: {overlap_value};
                background-color: #f2f2f2;
            }}

            .dynamic-form .form-group {{
                margin-bottom: 15px;
            }}

            .dynamic-form label {{
                display: block;
                font-weight: bold;
            }}

            .dynamic-form .form-control {{
                width: 90%;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 3px;
            }}

            .dynamic-form button {{
                display: inline-block;
                padding: 10px 20px;
                margin-top: 10px;
                background-color: #007bff;
                color: #fff;
                border: none;
                border-radius: 3px;
                cursor: pointer;
            }}

            /* Add more custom styles as needed */
        """
        return css


# pylint: disable=too-few-public-methods
class Button:
    """
    A class representing an HTML button.

    Attributes:
        label (str): The label or text displayed on the button.
        button_type (str): The type of the button.
    """

    def __init__(self, label, button_type="submit"):
        """
        Initializes the Button instance with the provided parameters.

        Args:
            label (str): The label or text displayed on the button.
            button_type (str, optional): The type of the button. Defaults to "submit".
        """
        self.label = label
        self.button_type = button_type

    def render_html(self):
        """
        Renders the HTML representation of the button.

        Returns:
            str: HTML representation of the button.
        """
        html = f"""
            <button type="{self.button_type}" class="btn btn-primary">{self.label}</button>
        """
        return html


class LoginForm(Form):
    def __init__(self, login_url, form_elements=None):
        """
        Initialize a login form instance.

        Parameters:
        - login_url (str): The URL to which the form should submit.
        """
        super().__init__(login_url)
        if form_elements:
            for element in form_elements:
                label = element.get("label", "")
                name = element.get("name", "")
                input_type = element.get("type", "text")
                self.add_field(label, name, input_type)

        self.add_button("Submit")

    def render_html(self):
        """
        Generate HTML markup for the login form.

        Returns:
        - str: A string containing HTML markup for the login form.
        """
        # You can add custom HTML here if needed, e.g., additional styling
        return super().render_html()

    def render_css(self):
        """
        Generate CSS styles for the login form.

        Returns:
        - str: A string containing CSS styles for the login form.
        """
        # Define custom CSS styles specific to the login form
        custom_css = """
            /* Custom styles for the login form */
            .login-form {
                background-color: #f5f5f5;
                padding: 20px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }

            .login-form .form-group {
                margin-bottom: 15px;
            }

            .login-form label {
                font-weight: bold;
            }

            .login-form .form-control {
                width: 70%;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 3px;
            }

            .login-form .btn-primary {
                background-color: #007bff;
                color: #fff;
                padding: 10px 20px;
                border: none;
                border-radius: 3px;
                cursor: pointer;
            }

            /* Add more custom styles as needed */
        """
        # Combine the base form styles with custom styles
        base_css = super().render_css()
        # base_css = ''
        return f"{base_css}\n{custom_css}"  # Combine the base and custom CSS


class StarRating:
    def __init__(self, name, num_stars):
        self.name = name
        self.num_stars = num_stars

    def render_html(self):
        star_elements = "".join(
            f"""
            <input type="radio" name="{self.name}" id="{self.name}-{self.num_stars - i}" value="{self.num_stars - i}"/>
            <label for="{self.name}-{self.num_stars - i}"></label>
            """
            for i in range(self.num_stars)
        )

        css = """
        <style>
            .star-rating {
                display: flex;
                align-items: center;
                width: 160px;
                flex-direction: row-reverse;
                justify-content: space-between;
                margin: 0px auto;
                position: relative;
            }
            /* hide the inputs */
            .star-rating input {
                display: none;
            }
            /* set properties of all labels */
            .star-rating > label {
                width: 30px;
                height: 30px;
                font-family: Arial;
                font-size: 30px;
                transition: 0.2s ease;
                color: orange;
            }
            /* give label a hover state */
            .star-rating label:hover {
                color: #ff69b4;
                transition: 0.2s ease;
            }
            .star-rating label:active::before {
                transform:scale(1.1);
            }

            /* set shape of unselected label */
                .star-rating label::before {
                content: '\\2606';
                position: absolute;
                top: 0px;
                line-height: 26px;
            }
            /* set full star shape for checked label and those that come after it */
            .star-rating input:checked ~ label:before {
            content:'\\2605';
            }

            @-moz-document url-prefix() {
            .star-rating input:checked ~ label:before {
            font-size: 36px;
            line-height: 21px;
            }
            }
        </style>
        """

        html = f"""
            {css}
            <div class="star-rating">
                {star_elements}
            </div>
        """
        return html


class Sidebar:
    """
    A class representing a customizable sidebar in HTML.

    Attributes:
        items (list): A list of dictionaries, each representing an item in the sidebar.
        width (int): The width of the sidebar in pixels.
        background_color (str): Background color of the sidebar in hexadecimal format.
        text_color (str): Text color of the items in the sidebar in hexadecimal format.
        hover_color (str): Color of the item when hovered in hexadecimal format.
        orientation (str): The orientation of the sidebar, either 'vertical' or 'horizontal'.
        top (int or None): The CSS 'top' property for the sidebar. None if not set.
        left (int or None): The CSS 'left' property for the sidebar. None if not set.
        right (int or None): The CSS 'right' property for the sidebar. None if not set.
        bottom (int or None): The CSS 'bottom' property for the sidebar. None if not set.
    """

    def __init__(
        self,
        items,
        width=200,
        background_color="#f5f5f5",
        text_color="#818181",
        hover_color="#f1f1f1",
        orientation="vertical",
        top=None,
        left=None,
        right=None,
        bottom=None,
    ):
        """
        Initializes the Sidebar instance with the provided parameters.

        Args:
            items (list): A list of dictionaries, each representing an item in the sidebar.
            width (int, optional): The width of the sidebar in pixels. Defaults to 200.
            background_color (str, optional): Background color of the sidebar. Defaults to "#f5f5f5".
            text_color (str, optional): Text color of the items in the sidebar. Defaults to "#818181".
            hover_color (str, optional): Color of the item when hovered. Defaults to "#f1f1f1".
            orientation (str, optional): The orientation of the sidebar. Defaults to "vertical".
            top (int or None, optional): The CSS 'top' property for the sidebar. Defaults to None.
            left (int or None, optional): The CSS 'left' property for the sidebar. Defaults to None.
            right (int or None, optional): The CSS 'right' property for the sidebar. Defaults to None.
            bottom (int or None, optional): The CSS 'bottom' property for the sidebar. Defaults to None.
        """
        self.items = items
        self.width = width
        self.background_color = background_color
        self.text_color = text_color
        self.hover_color = hover_color
        self.orientation = orientation
        self.top = top
        self.left = left
        self.right = right
        self.bottom = bottom

    def render_html(self):
        """
        Renders the HTML representation of the sidebar.

        Returns:
            str: HTML representation of the sidebar.
        """
        sidebar_html = f'<div class="sidebar" style="width: {self.width}px; background-color: {self.background_color};'
        if self.top is not None:
            sidebar_html += f" top: {self.top}px;"
        if self.left is not None:
            sidebar_html += f" left: {self.left}px;"
        if self.right is not None:
            sidebar_html += f" right: {self.right}px;"
        if self.bottom is not None:
            sidebar_html += f" bottom: {self.bottom}px;"
        if self.orientation == "horizontal":
            sidebar_html += ' display: flex; flex-direction: row;">'
        else:
            sidebar_html += '">'

        for item in self.items:
            sidebar_html += f"""<a href="{item["url"]}"
                            style="color: {self.text_color};
                            display: block;
                            text-decoration: none;
                            padding: 6px 8px 6px 16px;">{item["label"]}</a>"""
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
            { "top: " + str(self.top) + "px;" if self.top is not None else "" }
            { "left: " + str(self.left) + "px;" if self.left is not None else "" }
            { "right: " + str(self.right) + "px;" if self.right is not None else "" }
            { "bottom: " + str(self.bottom) + "px;" if self.bottom is not None else "" }
            { "height: 100%;" if self.orientation == "vertical" else "height: auto;" }
            { "width: " + str(self.width) + "px;" if self.orientation == "vertical" else "width: 100%;" }
            { "flex-direction: column;" if self.orientation == "vertical" else "flex-direction: row;" }
            background-color: {self.background_color};
            { "overflow-x: hidden;" if self.orientation == "vertical" else "overflow-y: hidden;" }
            padding-top: 20px;
        }}

        .sidebar a {{
            color: {self.text_color};
        }}

        .sidebar a:hover {{
            color: {self.hover_color};
        }}
        """
        return sidebar_css


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
        navbar_html = '<div class="navbar" style="background-color: {};">'.format(
            self.background_color
        )
        for item in self.items:
            navbar_html += """<a href="{}"
                            style="color: {};
                            padding: 14px 16px;
                            text-decoration: none;">{}</a>""".format(
                item["url"], self.text_color, item["label"]
            )
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


class FeedbackForm(Form):
    """
    A class representing a feedback form, derived from the Form class.

    Attributes:
        action (str): The URL to which the form should submit.
        method (str): The HTTP method to be used for form submission.
    """

    def __init__(self, action, method="POST"):
        """
        Initialize a FeedbackForm instance.

        Parameters:
        - action (str): The URL to which the form should submit.
        - method (str): The HTTP method to be used for form submission
            (default is 'POST').
        """
        super().__init__(action, method)
        # Add form fields to the feedback form
        self.add_field("Name", "name", "text")
        self.add_field("Email", "email", "email")

        # Create a StarRating component
        star_rating = StarRating("stars", 5)

        # Add the star rating component as a custom component
        self.add_custom_component(star_rating.render_html())

        self.add_button("Submit")  # Add a submit button

    def render_html(self):
        """
        Generate HTML markup for the feedback form.

        Returns:
        - str: A string containing HTML markup for the feedback form.
        """
        # Combine the HTML markup of the feedback form with
        # the custom components and submit button
        html = super().render_html()

        # Create a StarRating component with 5 stars
        star_rating = StarRating("stars", 5)

        # Add the star rating component as a custom component
        self.add_custom_component(star_rating.render_html())
        print(html)

        return html
