from flask import Flask, render_template, request, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "index"

# ルーティング
# @app.route("/hello")
# def hello_world():
#     return"Hello World!!"

# @app.route("/user/<username>")
# def show_user_profile(username):
#     return f'User {escape(username)}'

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f'Post {post_id}'

@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    #show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
