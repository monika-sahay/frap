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
from app.templates import render_template  # Import the render_template function from the app package
from app.responses import redirect  # Import the redirect function from the app package
from werkzeug.wrappers import Response


app = App(__name__)

# Define URL rules and endpoints using the add_url_rule method
app.add_url_rule('index', '/')
app.add_url_rule('login', '/login')
app.add_url_rule('message', '/message')


@app.route('/')
def handle_query(request):
    login_url = app.url_for('login')
    return Response(render_template('index.html'), content_type='text/html')

@app.route('/login', methods=['POST', 'GET'])
def login(request):
    username = request.form.get('username')
    password = request.form.get('pw')
    if username == 'monika' and password == 'moni':
        # Generate URL for the 'message' endpoint with a placeholder
        login_url = app.url_for('login')
        return redirect('/message')

    return Response(render_template('LoginPage.html'), content_type='text/html')

messageBoard = []

@app.route('/message', methods=['POST', 'GET'])
def message(request):
    if request.method == 'POST':
        messagestring = request.form.get('message')
        messageBoard.append(messagestring)
        # Generate URL for the 'message' endpoint with a placeholder
        message_url = app.url_for('message')
        return redirect(message_url)

    values = {'value': messageBoard}
    return Response(render_template('Messageboard.html', values=values), content_type='text/html')