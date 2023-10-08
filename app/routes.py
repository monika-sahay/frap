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