# components.py
class CustomSlider:
    def __init__(self, label, min_value, max_value, default_value, step):
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
        self.label = label
        self.min_value = min_value
        self.max_value = max_value
        self.default_value = default_value
        self.step = step

    def render_html(self):
        """
        Generate HTML markup for the custom slider element.

        Returns:
        - str: A string containing HTML markup for the custom slider element.
        """
        html = f'''
            <label>{self.label}</label>
            <input type="range" id="{self.label}" name="{self.label}" 
                   min="{self.min_value}" max="{self.max_value}" 
                   value="{self.default_value}" step="{self.step}">
            <span id="{self.label}-value">{self.default_value}</span>
            <br>
        '''
        return html

    def render_js(self):
        """
        Generate JavaScript code for the custom slider element.

        Returns:
        - str: A string containing JavaScript code for updating the slider's value display.
        """
        js = f'''
            $(document).ready(function() {{
                $('input[type="range"]').on('input', function() {{
                    var label = $(this).attr('id');
                    var value = $(this).val();
                    $('#{self.label}-value').text(value);
                }});
            }});
        '''
        return js


class Form:
    def __init__(self, action, method='POST'):
        self.action = action
        self.method = method
        self.fields = []
        self.buttons = []
        self.custom_components = []

    def add_field(self, label, name, input_type='text'):
        field = {'label': label, 'name': name, 'type': input_type}
        self.fields.append(field)

    def add_button(self, label, button_type='submit'):
        button = Button(label, button_type)
        self.buttons.append(button)

    def add_custom_component(self, custom_html):
        self.custom_components.append(custom_html)

    def render_html(self):
        html = f'''
            <form action="{self.action}" method="{self.method}" class="dynamic-form">
        '''
        for field in self.fields:
            label = field['label']
            name = field['name']
            input_type = field['type']
            input_id = f'form-{name}'
            html += f'''
                <div class="form-group">
                    <label for="{input_id}">{label}:</label>
                    <input type="{input_type}" name="{name}" id="{input_id}" class="form-control">
                </div>
            '''

        for custom_component in self.custom_components:
            html += custom_component

        for button in self.buttons:
            button_html = button.render_html()
            html += button_html

        html += '''
                </form>
        '''
        return html

    def render_css(self, width='50%', margin_top='50px', left='auto', right='auto', top='auto', bottom='auto', z_index='auto', overlap=False):
        """
        Generate CSS styles for the dynamic form.

        Parameters:
        - width (str): The width of the form.
        - margin_top (str): The top margin of the form.
        - left (str): The CSS 'left' property for the form.
        - right (str): The CSS 'right' property for the form.
        - top (str): The CSS 'top' property for the form.
        - bottom (str): The CSS 'bottom' property for the form.
        - z_index (str): The CSS 'z-index' property for the form.
        - overlap (bool): Whether the form should overlap other elements.

        Returns:
        - str: A string containing CSS styles for the dynamic form.
        """
        overlap_value = 'hidden' if overlap else 'visible'
        css = f'''
            /* Custom styles for the dynamic form */
            .dynamic-form {{
                width: {width};
                margin: auto;
                padding: 20px;
                border: 1px solid #ccc;
                border-radius: 5px;
                margin-top: {margin_top};
                position: absolute;
                left: {left};
                right: {right};
                top: {top};
                bottom: {bottom};
                z-index: {z_index};
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
        '''
        return css

class Button:
    def __init__(self, label, button_type='submit'):
        self.label = label
        self.button_type = button_type

    def render_html(self):
        html = f'''
            <button type="{self.button_type}" class="btn btn-primary">{self.label}</button>
        '''
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
                label = element.get('label', '')
                name = element.get('name', '')
                input_type = element.get('type', 'text')
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
        custom_css = '''
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
        '''
        # Combine the base form styles with custom styles
        base_css = super().render_css()
        # base_css = ''
        return f"{base_css}\n{custom_css}"  # Combine the base and custom CSS


class StarRating:
    def __init__(self, name, num_stars):
        self.name = name
        self.num_stars = num_stars

    def render_html(self):
        star_elements = ''.join(
            f'''
            <input type="radio" name="{self.name}" id="{self.name}-{self.num_stars - i}" value="{self.num_stars - i}"/>
            <label for="{self.name}-{self.num_stars - i}"></label>
            '''
            for i in range(self.num_stars)
        )

        css = '''
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
        '''

        html = f'''
            {css}
            <div class="star-rating">
                {star_elements}
            </div>
        '''
        return html


class Sidebar:
    def __init__(self, items, width=200, background_color="#f5f5f5", text_color="#818181", hover_color="#f1f1f1", orientation="vertical", top=None, left=None, right=None, bottom=None):
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
        sidebar_html = f'<div class="sidebar" style="width: {self.width}px; background-color: {self.background_color};'
        if self.top is not None:
            sidebar_html += f' top: {self.top}px;'
        if self.left is not None:
            sidebar_html += f' left: {self.left}px;'
        if self.right is not None:
            sidebar_html += f' right: {self.right}px;'
        if self.bottom is not None:
            sidebar_html += f' bottom: {self.bottom}px;'
        if self.orientation == "horizontal":
            sidebar_html += ' display: flex; flex-direction: row;">'
        else:
            sidebar_html += '">'

        for item in self.items:
            sidebar_html += f'<a href="{item["url"]}" style="color: {self.text_color}; display: block; text-decoration: none; padding: 6px 8px 6px 16px;">{item["label"]}</a>'
        sidebar_html += '</div>'
        return sidebar_html

    def render_css(self):
        sidebar_css = f'''
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
        '''
        return sidebar_css
    

class Navbar:
    def __init__(self, items, background_color="#333", text_color="#fff", hover_color="#4CAF50"):
        self.items = items
        self.background_color = background_color
        self.text_color = text_color
        self.hover_color = hover_color

    def render_html(self):
        navbar_html = '<div class="navbar" style="background-color: {};">'.format(self.background_color)
        for item in self.items:
            navbar_html += '<a href="{}" style="color: {}; padding: 14px 16px; text-decoration: none;">{}</a>'.format(item["url"], self.text_color, item["label"])
        navbar_html += '</div>'
        return navbar_html

    def render_css(self):
        navbar_css = f'''
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
        '''
        return navbar_css
# class Sidebar:
#     def __init__(self, items, width=200, background_color="#f5f5f5", text_color="#818181", hover_color="#f1f1f1", orientation="vertical"):
#         self.items = items
#         self.width = width
#         self.background_color = background_color
#         self.text_color = text_color
#         self.hover_color = hover_color
#         self.orientation = orientation

#     def render_html(self):
#         sidebar_html = f'<div class="sidebar" style="width: {self.width}px; background-color: {self.background_color};'
#         if self.orientation == "horizontal":
#             sidebar_html += ' display: flex; flex-direction: row;">'
#         else:
#             sidebar_html += '">'

#         for item in self.items:
#             sidebar_html += f'<a href="{item["url"]}" style="color: {self.text_color}; display: block; text-decoration: none; padding: 6px 8px 6px 16px;">{item["label"]}</a>'
#         sidebar_html += '</div>'
#         return sidebar_html

#     def render_css(self):
#         sidebar_css = f'''
#         .sidebar {{
#             position: fixed;
#             top: 0;
#             { "height: 100%;" if self.orientation == "vertical" else "height: auto;" }
#             { "width: " + str(self.width) + "px;" if self.orientation == "vertical" else "width: 100%;" }
#             { "flex-direction: column;" if self.orientation == "vertical" else "flex-direction: row;" }
#             background-color: {self.background_color};
#             { "overflow-x: hidden;" if self.orientation == "vertical" else "overflow-y: hidden;" }
#             padding-top: 0px;
#         }}

#         .sidebar a {{
#             color: {self.text_color};
#         }}

#         .sidebar a:hover {{
#             color: {self.hover_color};
#         }}
#         '''
#         return sidebar_css
# class Sidebar:
#     def __init__(self, items, width=200, background_color="#f3f3f3", text_color="#818181", hover_color="#f1f1f1"):
#         self.items = items
#         self.width = width
#         self.background_color = background_color
#         self.text_color = text_color
#         self.hover_color = hover_color

#     def render_html(self):
#         sidebar_html = '<div class="sidebar">'
#         for item in self.items:
#             sidebar_html += f'<a href="{item["url"]}">{item["label"]}</a>'
#         sidebar_html += '</div>'
#         return sidebar_html

#     def render_css(self):
#         sidebar_css = f'''
#         .sidebar {{
#             height: 100%;
#             width: {self.width}px;
#             position: fixed;
#             top: 0;
#             left: 0;
#             background-color: {self.background_color};
#             overflow-x: hidden;
#             padding-top: 20px;
#         }}

#         .sidebar a {{
#             padding: 6px 8px 6px 16px;
#             text-decoration: none;
#             font-size: 25px;
#             color: {self.text_color};
#             display: block;
#         }}

#         .sidebar a:hover {{
#             color: {self.hover_color};
#         }}
#         '''
#         return sidebar_css
    

class FeedbackForm(Form):
    def __init__(self, action, method='POST'):
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
        # Combine the HTML markup of the feedback form with the custom components and submit button
        html = super().render_html()

        # Create a StarRating component with 5 stars
        star_rating = StarRating("stars", 5)
    
        # Add the star rating component as a custom component
        self.add_custom_component(star_rating.render_html())
        print(html)

        return html