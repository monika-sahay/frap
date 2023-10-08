# threaded_server
"""
Frap Threaded Server

This module defines functions for running a Frap web application using the Hypercorn ASGI server in a threaded environment.
The threaded server allows handling multiple requests concurrently by running them in separate threads.

Usage:
    To use the threaded server for a Frap application, call the `run_threaded` function with your `App` instance,
    host, and port as arguments. This will start the Hypercorn server in a separate thread.

Example:
    Run a Frap application using the threaded server:

    ```python
    from server.threaded_server import run_threaded
    from app.routes import app  # Import your Frap application instance

    if __name__ == '__main__':
        host = '0.0.0.0'  # Set your desired host
        port = 8000  # Set your desired port
        run_threaded(app, host, port)
    ```

Functions:
    - run_hypercorn(app, host, port): Configures and runs the Hypercorn ASGI server for a Frap application using asyncio.
    - run_threaded(app, host, port): Runs the Hypercorn server in a separate thread to allow concurrent handling of requests.

Dependencies:
    - threading.Thread: Provides tools for creating and managing threads.
    - asyncio.new_event_loop: Creates a new event loop for asyncio.
    - asyncio.set_event_loop: Sets the current event loop for asyncio.
    - hypercorn.Config: Configuration settings for the Hypercorn server.
    - hypercorn.asyncio.serve: Runs the Hypercorn server using asyncio.
    - app.routes.app: Import the Frap application instance from your application's routes.

"""
import threading
import asyncio
from hypercorn import Config
from hypercorn.asyncio import serve
from app.routes import app


def run_hypercorn(app,host,port):
    """
    Configure and run the Hypercorn ASGI server for a Frap application using asyncio.

    Args:
        app (App): An instance of the Frap web application.
        host (str): The host address to bind the server (e.g., '0.0.0.0').
        port (int): The port number to listen on (e.g., 8000).

    Returns:
        None

    This function configures and runs the Hypercorn server to serve the specified Frap application. It uses asyncio
    for asynchronous handling of requests. The server is configured with the provided host and port, allowing the
    application to accept incoming HTTP requests.
    """

    # Configure Hypercorn
    config = Config()
    config.bind = [f"{host}:{port}"]  # Specify the host and port

    # Run the Hypercorn server using asyncio
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(serve(app, config))


def run_threaded(app,host,port):
    """
    Run the Hypercorn server in a separate thread to allow concurrent handling of requests.

    Args:
        app (App): An instance of the Frap web application.
        host (str): The host address to bind the server (e.g., '0.0.0.0').
        port (int): The port number to listen on (e.g., 8000).

    Returns:
        None

    This function creates a new thread and starts the Hypercorn server in that thread. The server runs the specified
    Frap application, allowing concurrent handling of multiple HTTP requests. This is useful for improving the
    responsiveness and performance of the web application.
    """

    hypercorn_thread = threading.Thread(target=run_hypercorn(app,host,port))

    # Start the Hypercorn thread
    hypercorn_thread.start()