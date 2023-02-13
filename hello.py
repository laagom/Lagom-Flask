
# Flask를 이용한 WSGI Server 열기
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Index Page"

@app.route('/hello')
def hello():
    return f"Hello, World!"
