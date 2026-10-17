from flask import Flask, request
from lambda_function import lambda_handler

app = Flask(__name__)

@app.route('/hello', methods=['POST', 'GET'])
def hello():
    event = {"body": request.get_data(as_text=True) or '{"name":"Deivids do K8s"}'}
    resp = lambda_handler(event, None)
    return resp['body'], resp['statusCode'], {'Content-Type': 'application/json'}

@app.route('/health')
def health():
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)