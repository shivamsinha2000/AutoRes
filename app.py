from flask import Flask, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter

app = Flask(__name__)

c = Counter('my_requests_total', 'Total HTTP Requests')

@app.route('/')
def hello():
    c.inc()
    return "Hello, World!"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)