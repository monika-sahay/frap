'''
Module for testing API endpoints
'''


import pytest
from werkzeug.test import EnvironBuilder
from werkzeug.wrappers import Request
from werkzeug.test import Client
from frap.app.app import App as FrapApp  # Import your original App class
import requests
from bs4 import BeautifulSoup


class FrapTestClient:
    """
    A custom test client for Frap web applications.
    """

    def __init__(self, app):
        """
        Initialize the test client with the Frap application instance.

        Args:
            app: An instance of the Frap application.
        """
        self.app = app
        self.base_url = (
            "http://localhost:8000"  # Adjust the URL to match your app's host and port
        )
        self.client = Client(app, Request)

    def get(self, path, **kwargs):
        """
        Send an HTTP GET request to the specified path.

        Args:
            path (str): The URL path to send the GET request to.
            **kwargs: Additional keyword arguments to
            pass to the requests.get function.

        Returns:
            requests.Response: The response object.
        """
        url = self.base_url + path
        response = requests.get(url, **kwargs)
        return response

    def post(self, path, data=None, json=None, **kwargs):
        """
        Send an HTTP POST request to the specified path.

        Args:
            path (str): The URL path to send the POST request to.
            data: The data to include in the request body (as form data).
            json: JSON data to include in the request body.
            **kwargs: Additional keyword arguments to pass
              to the requests.post function.

        Returns:
            requests.Response: The response object.
        """
        url = self.base_url + path
        response = requests.post(
            url, data=data, json=json, allow_redirects=False, **kwargs
        )
        return response

    # Implement other HTTP methods like PUT, DELETE, etc., if needed.

    def close(self):
        """
        Close the test client and release any resources.
        """
        pass  # You can implement this if needed


class App(FrapApp):
    def create_environ(self, path="/", method="GET", data=None, headers=None):
        builder = EnvironBuilder(path=path, method=method, data=data, headers=headers)
        return builder.get_environ()


@pytest.fixture
def app_and_client():
    # Create an instance of your App class
    app = App(__name__)

    # Create a test client for the app
    client = FrapTestClient(app)

    return app, client


def test_index_route(app_and_client):
    app, client = app_and_client

    response = client.get("/")

    assert response.status_code == 200
    assert b"Welcome to the site hosted on Frap server" in response.text.encode()


# Define a test case for the login route
def test_login_route(app_and_client):
    # Create an instance of your App class and a FrapTestClient instance for testing
    app, client = app_and_client

    # Simulate a POST request with valid credentials
    response = client.post("/login", data={"username": "monika", "pw": "moni"})

    # Assert that the response status code is a redirect (e.g., 302)
    assert response.status_code == 303

    # Assert that the response location header is set to '/message'
    assert response.headers["Location"] == "/message"

    # Simulate a POST request with invalid credentials
    response = client.post("/login", data={"username": "invalid", "pw": "invalid"})

    # Assert that the response status code is 200
    assert response.status_code == 200

    # Assert that the response content contains the login page HTML
    assert b"Login Page" in response.text.encode()


def test_message_route(app_and_client):
    app, client = app_and_client

    # Simulate a GET request to the '/message' route
    response = client.get("/message")

    # Assert that the response status code is 200
    assert response.status_code == 200

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the <title> element
    title_element = soup.find("title")

    # Assert that the title element contains "Message Board"
    assert "Message Board" in title_element.text

    # Define the message to be posted
    message_to_post = "This is a test message."

    # Simulate a POST request to the '/message' route with the message data
    response = client.post("/message", data={"message": message_to_post})
    # Follow the redirect manually
    redirect_response = client.get(response.headers['Location'])

    # Parse the updated HTML content using BeautifulSoup
    soup = BeautifulSoup(redirect_response.text, "html.parser")

    # Find the <ul> element where posted messages are typically displayed
    ul_element = soup.find("ul")
    # print(response.text, response.status_code)
    # # Assert that the response status code is 200 (or another appropriate status code)
    # assert response.status_code == 303

    # # Parse the updated HTML content using BeautifulSoup
    # soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    # # Find the <ul> element where posted messages are typically displayed
    # ul_element = soup.find("ul")
    # print(ul_element)

    # Check if the posted message is present within the <ul> element
    assert f"<li>{message_to_post}</li>" in str(ul_element)


def test_submit_route(app_and_client):
    app, client = app_and_client

    # Define the data to be sent in the POST request
    data = {"Slider": "75"}  # Change the slider value as needed

    # Simulate a POST request to the '/submit' route with the data
    response = client.post("/submit", data=data)

    # Assert that the response status code is 200
    # (or another appropriate status code)
    assert response.status_code == 200

    # Assert that the response content contains the expected message
    assert "Slider Value: 75" in response.text
