# custom_handler.p
from werkzeug.wrappers import Request
from app.app import App
from io import BytesIO
import sys
import http.server
from http.server import HTTPServer
import pdb
from IPython import embed

class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, app_instance, *args, **kwargs):
        self.app_instance = app_instance
        super().__init__(*args, **kwargs)

  
    breakpoint()
    def do_GET(self):
        print("Received GET request:", self.path)
        breakpoint() 
        environ = {
            'REQUEST_METHOD': self.command,
            'PATH_INFO': self.path,
            'SERVER_PROTOCOL': 'HTTP/1.1',
            'wsgi.version': (1, 0),
            'wsgi.url_scheme': 'http',
            'wsgi.input': BytesIO(),
            'wsgi.errors': sys.stderr,
            'wsgi.multithread': True,
            'wsgi.multiprocess': True,
            'wsgi.run_once': False,
            'HTTP_HOST': self.headers.get('Host'),
            'SERVER_NAME': self.server.server_address[0],
            'SERVER_PORT': str(self.server.server_address[1]),
            'REMOTE_ADDR': self.client_address[0],
        }
        request = Request(environ)
        breakpoint()
        # response = App.handle_request(request)
        response = self.app_instance.handle_request(request)
        self.send_response(response.status_code)
        for key, value in response.headers.items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(response.data)

    def do_POST(self):
        print("Received POST request:", self.path)
        breakpoint() 
        content_length = int(self.headers.get('Content-Length', 0))
        request_data = self.rfile.read(content_length)
        environ = {
            'REQUEST_METHOD': self.command,
            'PATH_INFO': self.path,
            'SERVER_PROTOCOL': 'HTTP/1.1',
            'wsgi.version': (1, 0),
            'wsgi.url_scheme': 'http',
            'wsgi.input': BytesIO(request_data),
            'wsgi.errors': sys.stderr,
            'wsgi.multithread': True,
            'wsgi.multiprocess': True,
            'wsgi.run_once': False,
            'HTTP_HOST': self.headers.get('Host'),
            'SERVER_NAME': self.server.server_address[0],
            'SERVER_PORT': str(self.server.server_address[1]),
            'REMOTE_ADDR': self.client_address[0],
        }
        request = Request(environ)
        # response = App.handle_request(request)
        response = self.app_instance.handle_request(request)
        self.send_response(response.status_code)
        for key, value in response.headers.items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(response.data)


if __name__ == '__main__':
    server_address = ('', 4000)
    httpd = HTTPServer(server_address, CustomRequestHandler)
    httpd.serve_forever()