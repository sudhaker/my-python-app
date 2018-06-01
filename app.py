import signal
import sys
import logging
import platform

from flask import Flask

def sigterm_handler(signal, frame):
    sys.exit(0)

signal.signal(signal.SIGTERM, sigterm_handler)

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'My Python Flask App v-1.0 !! Server : ' + platform.node()

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
