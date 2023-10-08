# app.py
from werkzeug.wrappers import Request, Response
from werkzeug.serving import make_server
from IPython import embed
from werkzeug.debug import DebuggedApplication

class App:
    def __init__(self, name):
        self.routes = []
        self.url_map = {}
        self.name = name

    def route(self, path, methods=None):
        if methods is None:
            methods = ['GET']

        def decorator(f):
            self.routes.append((path, methods, f))
            return f

        return decorator

    def handle_request(self, environ, start_response):
        request = Request(environ)
        for path, methods, handler in self.routes:
            if request.path == path and request.method in methods:
                response = handler(request)
                return response(environ, start_response)

        response = Response('Not Found', status=404)
        return response(environ, start_response)
    
    def add_url_rule(self, endpoint, url_pattern):
        self.url_map[endpoint] = url_pattern

    def url_for(self, endpoint, **values):
        if endpoint in self.url_map:
            url_pattern = self.url_map[endpoint]
            url = url_pattern.format(**values)
            return url
        else:
            raise ValueError(f"Endpoint '{endpoint}' not found in URL rules")

    def run_server(self, host='0.0.0.0', port=8000):
        httpd = make_server(host, port, self)
        print(f"Serving on {host}:{port}")
        httpd.serve_forever()



    def __call__(self, environ, start_response):
        return self.handle_request(environ, start_response)




if __name__ == '__main__':
    app = App()
    app.run()