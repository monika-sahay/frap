# Usage

## Routing

Frap provides a straightforward way to define routes for your web application. You can map URLs to specific functions using decorators.

### Defining Routes

To define a route, use the `@app.route()` decorator. For example:

```python
from app.app import App

app = App(__name__)

@app.route('/')
def index(request):
    return Response("Hello, World!")

```
In this example, the / URL is mapped to the index function. When a user accesses the root URL, they will see "Hello, World!" as the response.

### Handling HTTP Methods
You can specify which HTTP methods a route should respond to by providing a list of methods to the decorator:

```
@app.route('/login', methods=['GET', 'POST'])
def login(request):
    # Your login logic here
```
In this case, the login route will respond to both GET and POST requests.

### Templates
Frap integrates with the Jinja2 templating engine, allowing you to render dynamic HTML content for your web pages.

### Rendering Templates
To render a template, use the render_template function from app.templates:

```
from app.templates import render_template

@app.route('/')
def index(request):
    data = {'name': 'John'}
    content = render_template('index.html', data=data)
    return Response(content, content_type='text/html')

```
In this example, we pass a dictionary data to the index.html template, which can be used to display dynamic content.

### URL Mapping
Frap simplifies URL management with the add_url_rule method and the url_for function.

Adding URL Rules
Use add_url_rule to associate an endpoint name with a URL pattern:

```
app.add_url_rule('about', '/about-us')
This creates an endpoint named 'about' mapped to the '/about-us' URL.
```
### Generating URLs
The url_for function generates URLs based on endpoint names and values:

```
url = app.url_for('about')
```
Now you can use url to link to the 'about' page.

### HTTP Responses
Frap allows you to create various HTTP responses, including redirects.

Redirects
To redirect users to another page, use the redirect function:

```
from app.responses import redirect

@app.route('/old-url')
def old_url(request):
    return redirect('/new-url')
```
In this example, accessing '/old-url' will redirect users to '/new-url'.