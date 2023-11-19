"""
Routes Configuration and URL Handling

This module defines the routing configuration and URL handling for the Frap web framework.
It includes route definitions, URL rules, and request handlers for different endpoints.

Usage:
    To create new routes or define URL rules, use the `app.add_url_rule` method.
    You can also specify route handlers for different URL patterns using the `@app.route` decorator.

Example:
    To create a new route, use `app.add_url_rule(endpoint, url_pattern)`, where `endpoint`
    is a unique identifier for the route, and `url_pattern` is the URL pattern that maps to the route.
    For example, `app.add_url_rule('index', '/')` maps the 'index' endpoint to the root URL '/'.

    To define a route handler, use the `@app.route(url_pattern, methods)` decorator, where
    `url_pattern` is the URL pattern for the route, and `methods` is a list of HTTP methods
    that the route should handle. For example:

    @app.route('/login', methods=['POST', 'GET'])
    def login(request):
        # Route handler logic here

Routes:
    - '/' (Root): Handles requests to the root URL.
    - '/login': Handles requests to the login page.
    - '/message': Handles requests to the message board page.

Functions:
    - handle_query(request): Route handler for the root URL ('/').
    - login(request): Route handler for the login page ('/login').
    - message(request): Route handler for the message board page ('/message').

Dependencies:
    - app.app: Importing the App class from the app package.
    - app.templates: Importing the render_template function from the app package.
    - app.responses: Importing the redirect function from the app package.
    - werkzeug.wrappers: Importing the Response class for generating HTTP responses.

"""

# routes.py
from werkzeug.wrappers import Response
from frap.app.app import App  # Import the App class from the app package
from frap.app.templates import render_template  # Import the render_template function from the app package
from frap.app.responses import redirect  # Import the redirect function from the app package
from frap.components.sidebar import Sidebar
from frap.components.navbar import Navbar
from frap.components.forms import LoginForm, Form
from frap.components.star import StarRating
from frap.components.slider import CustomSlider

# from werkzeug.utils import redirect

app = App(__name__)

# Define URL rules and endpoints using the add_url_rule method
app.add_url_rule("index", "/")
app.add_url_rule("login", "/login")
app.add_url_rule("message", "/message")
app.add_url_rule("submit", "/submit")


# feedback_form = FeedbackForm('/submit_feedback')
feedback_form = Form(action="/submit_feedback")

# Add fields to the form
feedback_form.add_field("Name", "name", "text")
feedback_form.add_field("Email", "email", "email")

# Create a StarRating component
star_rating = StarRating("stars", 5)

# Add the star rating component as a custom component
feedback_form.add_custom_component(star_rating.render_html())

# Add a submit button to the form
feedback_form.add_button("Submit")


@app.route("/")
def handle_query():
    """
    Handle the query request.

    Args:
    - request: The request object.

    Returns:
    - Response: The response containing the rendered template.
    """
    slider_config = {
        "label": "Slider",
        "min_value": 0,
        "max_value": 100,
        "default_value": 50,
        "step": 1, }
    slider_component = CustomSlider(slider_config)
    star = StarRating("rating", 5)
    custom_slider_html = slider_component.render_html()
    custom_slider_js = slider_component.render_js()
    login_url = app.url_for("login")
    return Response(
        render_template(
            "index.html",
            custom_slider_html=custom_slider_html,
            custom_slider_js=custom_slider_js,
            login_url=login_url,
            feedback_form=feedback_form,
            star=star,
        ),
        content_type="text/html",
    )


@app.route("/login", methods=["POST", "GET"])
def login(request):
    """
    Handle the login request.

    Args:
    - request: The request object.

    Returns:
    - Response: The response containing the rendered template.
    """
    form_elements = [
        {"label": "Username", "name": "username", "type": "text"},
        {"label": "Password", "name": "pw", "type": "password"},
    ]
    login_form = LoginForm("/login", form_elements)
    navbar_items = [
        {"url": "/", "label": "Home"},
        {"url": "/about", "label": "About"},
        {"url": "/contact", "label": "Contact"},
    ]
    navbar = Navbar(
        navbar_items, background_color="#333", text_color="#fff", hover_color="#4CAF50"
    )
    sidebar_instance = Sidebar(
        items=[
            {"url": "/home", "label": "Home"},
            {"url": "/about", "label": "About"}
            ],
        style_config={
            "color_scheme": {
                "background_color": "#ccc",
                "text_color": "#333",
                "hover_color": "#999"
                },
            "layout_properties": {
                "width": 250,
                "orientation": "horizontal",
                "top": 20,
                "left": 10
                }
            }
        )

    if request.method == "POST":
        login_data = request.form
        username = login_data.get("username")
        password = login_data.get("pw")
        if username == "monika" and password == "moni":
            return redirect("/message")
    return Response(
        render_template(
            "LoginPage.html",
            login_form=login_form,
            sidebar_vertical=sidebar_instance,
            navbar=navbar,
        ),
        content_type="text/html",
    )


messageBoard = []


@app.route("/message", methods=["POST", "GET"])
def message(request):
    """
    Handle the message request.

    Args:
    - request: The request object.

    Returns:
    - Response: The response containing the rendered template.
    """
    my_form = Form(action="/message", method="POST")
    # Add form fields
    my_form.add_field(label="Name", name="name", input_type="text")
    my_form.add_field(label="Email", name="email", input_type="email")
    my_form.add_field(label="Password", name="password", input_type="password")

    if request.method == "POST":
        messagestring = request.form.get("message")
        messageBoard.append(messagestring)
        # Generate URL for the 'message' endpoint with a placeholder
        message_url = app.url_for("message")
        return redirect(message_url)

    # Render the HTML markup for the form
    # if request.method == 'POST':
    #     messagestring = request.form.get('message')
    #     messageBoard.append(messagestring)
    #     print(messageBoard)
    #     # Generate URL for the 'message' endpoint with a placeholder
    #     message_url = app.url_for('message')
    #     return redirect(message_url)

    values = {"value": messageBoard}
    return Response(
        render_template("Messageboard.html", values=values, my_form=my_form),
        content_type="text/html",
    )


@app.route("/submit", methods=["POST"])
def submit(request):
    """
    Handle the submit request.

    Args:
    - request: The request object.

    Returns:
    - Response: The response containing the response text.
    """
    slider_value = request.form.get("Slider")
    print(slider_value)
    # Process the slider value here
    response_text = f"Slider Value: {slider_value}"

    # Create a Response object with the response text
    response = Response(response_text, content_type="text/plain", status=200)

    return response


@app.route("/submit_feedback", methods=["POST"])
def submit_feedback(request):
    """
    Handle the submit feedback request.

    Args:
    - request: The request object.

    Returns:
    - Response: The response containing the rendered template.
    """
    if request.method == "POST":
        # Retrieve form field values
        name = request.form.get("name")
        print(name)
        email = request.form.get("email")
        print(email)
        feedback = request.form.get("feedback")
        print(feedback)
        rating = request.form.get("stars")
        print(rating)  # Retrieve the star rating value

        # Process the form data (e.g., save to a database, send an email)
        # ...

        # Redirect to a thank you page or back to the form
    return Response(
        render_template("index.html", feedback_form=feedback_form),
        content_type="text/html",
    )
