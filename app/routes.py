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
from app.app import App  # Import the App class from the app package
from app.templates import (
    render_template,
)  # Import the render_template function from the app package
from app.responses import redirect  # Import the redirect function from the app package
from werkzeug.wrappers import Response
from app.components import CustomSlider, LoginForm, Form, StarRating, Sidebar, Navbar

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
def handle_query(request):
    slider_component = CustomSlider("Slider", 0, 100, 50, 1)
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
    form_elements = [
        {"label": "Username", "name": "username", "type": "text"},
        {"label": "Password", "name": "pw", "type": "password"},
    ]
    login_form = LoginForm("/login", form_elements)
    sidebar_items = [
        {"url": "/", "label": "Home"},
        {"url": "/about", "label": "About"},
        {"url": "/contact", "label": "Contact"},
    ]
    navbar_items = [
        {"url": "/", "label": "Home"},
        {"url": "/about", "label": "About"},
        {"url": "/contact", "label": "Contact"},
    ]
    navbar = Navbar(
        navbar_items, background_color="#333", text_color="#fff", hover_color="#4CAF50"
    )
    # sidebar = Sidebar(sidebar_items, width=200, background_color="#f3f3f3", text_color="#818181", hover_color="#f1f1f1")
    # sidebar = Sidebar(sidebar_items, width=1280, background_color="#f5f5f5", text_color="#007bff", hover_color="#b0b0b0", orientation="horizontal")
    # vertical_sidebar = Sidebar(sidebar_items)
    # sidebar_horizontal = Sidebar(sidebar_items, width=1250, background_color="#f5f5f5", text_color="#818181", hover_color="#f1f1f1", orientation="horizontal", top=0, left=0, right=None, bottom=None)
    sidebar_vertical = Sidebar(
        sidebar_items,
        width=200,
        background_color="#f3f3f3",
        text_color="#818181",
        hover_color="#f1f1f1",
        orientation="vertical",
        top=50,
        left=0,
        right=None,
        bottom=None,
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
            sidebar_vertical=sidebar_vertical,
            navbar=navbar,
        ),
        content_type="text/html",
    )


messageBoard = []


@app.route("/message", methods=["POST", "GET"])
def message(request):
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
    slider_value = request.form.get("Slider")
    print(slider_value)
    # Process the slider value here
    response_text = f"Slider Value: {slider_value}"

    # Create a Response object with the response text
    response = Response(response_text, content_type="text/plain", status=200)

    return response


@app.route("/submit_feedback", methods=["POST"])
def submit_feedback(request):
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
