# Middleware Class
"""
The `Middleware` class serves as the base class for creating custom middleware components in the Frap web framework. 
Middleware components are responsible for processing incoming requests and outgoing 
responses as they pass through the middleware pipeline. 
You can create custom middleware classes by inheriting from this base class 
and implementing the necessary methods.

"""


class Middleware:
    def process_request(self, request):
        """
        Process the incoming HTTP request.

        Args:
            request: An instance of the Request object representing the incoming request.

        Returns:
            None
        """
        pass

    def process_response(self, request, response):
        """
        Process the outgoing HTTP response.

        Args:
            request: An instance of the Request object representing the incoming request.
            response: An instance of the Response object representing the outgoing response.

        Returns:
            None
        """
        pass