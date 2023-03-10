
# Flask를 이용한 WSGI Server 열기
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/')
def index():
    return "Index Page"


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


'''
    # 내용: url_for(함수명, 인자)를 사용해서 해당 라우팅의 url을 호출 할 수 있음
    -------------------------------------------------------------- 
'''
# from flask import url_for

# @app.route('/login')
# def login():
#     return "login"

# @app.route('/user/<username>')
# def profile(username):
#     return f"{username}\'s profile"

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))

from flask import request
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        return do_the_login()
    else:
        return show_the_login_form()

def do_the_login():
    print("do_the_login")
    return "do_the_login"

def show_the_login_form():
    print("show_the_login_form")
    return "show_the_login_form"


# Flask에서 제공하는 RFC 사용
@app.get('/login/rfc')
def login_get():
    return show_the_login_form()

@app.post('/login/rfc')
def login_post():
    return do_the_login()


# 템플릿 render 처리 방법
from flask import render_template

@app.route('/hello/render')
@app.route('/hello/render/<name>')
def hello(name=None):
    return render_template('/hello.html', name=name)

# request args를 이용하여 request 값 받아보기
from flask import request
@app.route('/args')
def args():
    print(request.args['keyword'])
    return 'hello'