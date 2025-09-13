from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Get the hostname (pod name) to show which container is serving the request
    pod_name = os.environ.get('HOSTNAME', 'unknown')
    return f'Hello from pod {pod_name}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)