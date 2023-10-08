# run.py
from server.threaded_server import run_threaded
from app.routes import app  # Import your app instance

if __name__ == '__main__':
    host = '0.0.0.0'  # Set your desired host
    port = 4000  # Set your desired port
    run_threaded(app, host, port)



# run.py
# from app.routes import app  # Import the 'app' instance from routes.py
# from werkzeug.middleware.dispatcher import DispatcherMiddleware
# from werkzeug.serving import make_server



# if __name__ == '__main__':
#     def run(address='0.0.0.0', port = 8000, dispacther=None):
#         httpd = make_server(address, port, app, dispacther)
#         print(f"Serving on {address}:{port}")
#         httpd.serve_forever()
#     # dispatcher = DispatcherMiddleware(app)
#     # def run_server():
#     #     httpd = make_server('', 4000, dispatcher)
#     #     print(f"Serving on port 4000...")
#     #     httpd.serve_forever()
#     # dispatcher = DispatcherMiddleware(app)
#     run()
    # server_thread = threading.Thread(target=app.run)

    # Start the server thread
    # server_thread.start()




# from app.app import App
# from app.templates import render_template
# from app.responses import redirect
# from werkzeug.wrappers import Response

# app = App()

# @app.route('/')
# def handle_query(request):
#     return Response(render_template('index.html'), content_type='text/html')

# @app.route('/login', methods=['POST', 'GET'])
# def login(request):
#     username = request.form.get('username')
#     password = request.form.get('pw')
#     if username == 'monika' and password == 'moni':
#         return redirect('/message')
#     return Response(render_template('LoginPage.html'), content_type='text/html')

# messageBoard = []

# @app.route('/message', methods=['POST', 'GET'])
# def message(request):
#     print(request)
#     message = request.form.get('message')
#     messageBoard.append(message)
#     return Response(render_template('Messageboard.html'), content_type='text/html')


# if __name__ == '__main__':
#     app.run()