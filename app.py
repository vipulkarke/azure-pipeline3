
from flask import Flask
app = Flask(__name__)
 
@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response
@app.route('/')
def hello_world():
    return 'Hello from karke ECS Container'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
