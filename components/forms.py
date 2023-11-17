# forms.py

"""
This module defines classes for creating HTML forms with customizable fields and buttons.

Classes:
    Form: A class representing an HTML form with customizable fields and buttons.
    Button: A class representing an HTML button.
    LoginForm: A subclass of Form specifically designed for login forms.
"""

from frap.components.star import StarRating


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
