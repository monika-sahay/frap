from wsgiref.simple_server import make_server
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from app.app import app

# Create a WSGI dispatcher that combines multiple apps
# dispatcher = DispatcherMiddleware(app)

if __name__ == "__main__":
    dispatcher = DispatcherMiddleware(app)
    httpd = make_server("", 4000, dispatcher)
    print("Serving on port 4000...")
    httpd.serve_forever()
