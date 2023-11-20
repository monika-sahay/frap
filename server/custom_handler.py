# custom_handler.py
"""
This module provides a custom request handler for an HTTP server.
"""


import http.server
from http.server import HTTPServer
from io import BytesIO
import sys
from werkzeug.wrappers import Request


class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    """
    Custom request handler for an HTTP server.

    This class extends SimpleHTTPRequestHandler to handle GET and POST requests
    by forwarding them to an instance of a WSGI application.

    Attributes:
        app_instance: An instance of the WSGI application to handle the requests.
    """

    def __init__(self, app_instance, *args, **kwargs):
        """
        Initialize the CustomRequestHandler.

        Args:
            app_instance: An instance of the WSGI application to handle the requests.
        """
        self.app_instance = app_instance
        super().__init__(*args, **kwargs)

    # pylint: disable=C0103
    def do_GET(self):
        """
        Handle HTTP GET requests.

        Forwards the GET request to the WSGI application and sends the response
        back to the client.
        """
        print("Received GET request:", self.path)
        environ = {
            "REQUEST_METHOD": self.command,
            "PATH_INFO": self.path,
            "SERVER_PROTOCOL": "HTTP/1.1",
            "wsgi.version": (1, 0),
            "wsgi.url_scheme": "http",
            "wsgi.input": BytesIO(),
            "wsgi.errors": sys.stderr,
            "wsgi.multithread": True,
            "wsgi.multiprocess": True,
            "wsgi.run_once": False,
            "HTTP_HOST": self.headers.get("Host"),
            "SERVER_NAME": self.server.server_address[0],
            "SERVER_PORT": str(self.server.server_address[1]),
            "REMOTE_ADDR": self.client_address[0],
        }
        request = Request(environ)
        # response = App.handle_request(request)
        response = self.app_instance.handle_request(request)
        self.send_response(response.status_code)
        for key, value in response.headers.items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(response.data)

    # pylint: disable=C0103
    def do_POST(self):
        """
        Handle HTTP POST requests.

        Forwards the POST request to the WSGI application and sends the response
        back to the client.
        """
        print("Received POST request:", self.path)
        content_length = int(self.headers.get("Content-Length", 0))
        request_data = self.rfile.read(content_length)
        environ = {
            "REQUEST_METHOD": self.command,
            "PATH_INFO": self.path,
            "SERVER_PROTOCOL": "HTTP/1.1",
            "wsgi.version": (1, 0),
            "wsgi.url_scheme": "http",
            "wsgi.input": BytesIO(request_data),
            "wsgi.errors": sys.stderr,
            "wsgi.multithread": True,
            "wsgi.multiprocess": True,
            "wsgi.run_once": False,
            "HTTP_HOST": self.headers.get("Host"),
            "SERVER_NAME": self.server.server_address[0],
            "SERVER_PORT": str(self.server.server_address[1]),
            "REMOTE_ADDR": self.client_address[0],
        }
        request = Request(environ)
        # response = App.handle_request(request)
        response = self.app_instance.handle_request(request)
        self.send_response(response.status_code)
        for key, value in response.headers.items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(response.data)


if __name__ == "__main__":
    server_address = ("", 4000)
    httpd = HTTPServer(server_address, CustomRequestHandler)
    httpd.serve_forever()
