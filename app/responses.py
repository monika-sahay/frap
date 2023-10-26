"""
HTTP Response Handling

This module provides functions for handling HTTP responses in the Frap web framework.
It includes a function for creating redirection responses.

Usage:
    To create a redirection response, use the `redirect(location)` function, where `location` is the URL to redirect to.

Example:
    To redirect to the '/login' page, use:

    redirect('/login')

Functions:
    - redirect(location): Creates a redirection response to the specified location (URL).

Dependencies:
    - werkzeug.wrappers.Response: Provides tools for constructing HTTP responses.

"""


# responses.py
from werkzeug.wrappers import Response


def redirect(location):
    """
    Generate a redirect response to the specified location.

    Args:
        location (str): The URL to which the client should be redirected.

    Returns:
        Response: An HTTP response with a status code of 303 (See Other) and
        a 'Location' header indicating the redirection target.
    """
    response = Response('', status=303)
    response.headers['Location'] = location
    return response
