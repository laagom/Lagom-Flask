
# Flask를 이용한 WSGI Server 열기
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Index Page"

@app.route('/hello')
def hello():
    return f"Hello, World!"


from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # 사용자의 정보 보여주기
    return f"User {escape(username)}"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 요청되어진 POST ID
    return f"Post {post_id}"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # subpath 보여주기
    return f"Subpath {escape(subpath)}"


@app.route('/projects/')
def projects():
    # 기본적으로 endpoint에 /(slash)가 추가되기 때문에 붙여줄 필요 없음
    return "The project page"

@app.route('/about')
def about():
    # 기본적으로 endpoint에 /(slash)가 추가되기 때문에 404 error페이지로 가지 않음
    return "The about page"
