# responses.py
from werkzeug.wrappers import Response

def redirect(location):
    response = Response('', status=303)
    response.headers['Location'] = location
    return response