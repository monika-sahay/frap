# rule.py


class Rule:
    def __init__(self, path, methods, endpoint, handler):
        self.path = path
        self.methods = methods
        self.endpoint = endpoint
        self.handler = handler

    def build(self, **kwargs):
        url = self.path
        values = {}
        for key, value in kwargs.items():
            url = url.replace(f"{{{key}}}", str(value))
            values[key] = value
        return url, values


if __name__ == "__main__":
    rule = Rule()
