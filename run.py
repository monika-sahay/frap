# run.py
"""
Frappy Framework Application Runner

This script is used to run a Frappy web application using the Hypercorn ASGI server in a threaded mode.

Usage:
    To start the Frappy web application, execute this script with Python:
        python run.py

    Ensure that the 'app' variable is correctly set to your Frap application instance in this script.

Author:
    Your Name

Date:
    Date when this script was created or last modified.
"""
# from server.threaded_server import run_threaded
from app.routes import app  # Import your app instance

if __name__ == '__main__':
    HOST = '0.0.0.0'  # Set your desired host
    PORT = 8000  # Set your desired port
    # run_threaded(app, host, port)
    app.run_server()
