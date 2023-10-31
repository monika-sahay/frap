# rule.py
"""
This module defines the Rule class, which represents a routing rule in a web application.
Each rule specifies a URL path, HTTP methods, an endpoint, and a handler function.
"""


class Rule:
    """
    Represents a routing rule in a web application.

    Attributes:
        path (str): The URL path associated with the rule.
        methods (list): The HTTP methods allowed for the rule.
        endpoint (str): The endpoint associated with the rule.
        handler (function): The handler function associated with the rule.
    """
    def __init__(self, path, methods, endpoint, handler):
        """
        Initializes a Rule instance.

        Parameters:
        - path (str): The URL path associated with the rule.
        - methods (list): The HTTP methods allowed for the rule.
        - endpoint (str): The endpoint associated with the rule.
        - handler (function): The handler function associated with the rule.
        """
        self.path = path
        self.methods = methods
        self.endpoint = endpoint
        self.handler = handler

    def build(self, **kwargs):
        """
        Builds the URL with the given parameters.

        Parameters:
        - **kwargs: Variable keyword arguments used to fill in dynamic parts of the path.

        Returns:
        - str: The URL with dynamic parts filled in.
        - dict: A dictionary containing the values of the dynamic parts of the URL.
        """
        url = self.path
        values = {}
        for key, value in kwargs.items():
            url = url.replace(f"{{{key}}}", str(value))
            values[key] = value
        return url, values


if __name__ == "__main__":
    rule = Rule('/', 'POST', 'message', 'Do_get')
