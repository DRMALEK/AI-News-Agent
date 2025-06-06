import os
from multiprocessing import Process

from dotenv import load_dotenv
from flask import Flask, send_from_directory
from flask_cors import CORS

# Load environment variables before importing backend modules
load_dotenv()

from backend.server import backend_app
CORS(backend_app)


frontend_app = Flask(__name__, static_folder='frontend')

@frontend_app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

@frontend_app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory('frontend', path)

@frontend_app.route('/outputs/<path:path>')
def serve_outputs(path):
    return send_from_directory('outputs', path)


def run_frontend():
    debug = os.environ.get('FLASK_ENV') == 'development'
    frontend_app.run(host='0.0.0.0', port=5000)

def run_backend():
    debug = os.environ.get('FLASK_ENV') == 'development'
    backend_app.run(host='0.0.0.0', port=8000)

if __name__ == '__main__':
    # Start the backend server
    backend_process = Process(target=run_backend)
    backend_process.start()

    # Start the frontend server
    frontend_process = Process(target=run_frontend)
    frontend_process.start()

    # Join the processes so that the main process waits for them to complete
    backend_process.join()
    frontend_process.join()