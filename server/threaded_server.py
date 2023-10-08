# threaded_server
import threading
import asyncio
from hypercorn import Config
from hypercorn.asyncio import serve
from app.routes import app


def run_hypercorn(app,host,port):
    # Configure Hypercorn
    config = Config()
    config.bind = [f"{host}:{port}"]  # Specify the host and port

    # Run the Hypercorn server using asyncio
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(serve(app, config))


def run_threaded(app,host,port):
    hypercorn_thread = threading.Thread(target=run_hypercorn(app,host,port))

    # Start the Hypercorn thread
    hypercorn_thread.start()