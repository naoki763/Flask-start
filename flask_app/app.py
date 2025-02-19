from flask import Blueprint, render_template, request, redirect, url_for
from flask_app.models import User
# from flask_app import db
from flask_app.factory import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/register', methods=['POST'])
def register():
    # フォームデータを取得
    username = request.form.get('username')
    email = request.form.get('email')

    # 入力値を保存（ここではメモリ内リストに保存）
    if username and email:
        # users.append({"username": username, "email": email})
        user = User(
            username = username,
            email = email
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.success', username=username))
    else:
        return "Error: Please provide both username and email", 400

@bp.route('/search', methods=['POST'])
def search():
    username = request.form.get('search_username')  # フォームから入力された値を取得
    user = User.query.filter_by(username=username).first()  # データベースで検索
    
    if user:
        # ユーザーが見つかった場合、結果を渡す
        return render_template('index.html', user=user, error=None)
    else:
        # ユーザーが見つからない場合、userをNone、エラーメッセージを設定
        error_message = f"User '{username}' not found."
        return render_template('index.html', user=None, error=error_message)
    
    # 検索結果をindex.htmlに渡す
    # return render_template('index.html', user=user)

@bp.route('/success')
def success():
    username = request.args.get('username', 'User')
    return render_template('success.html', username=username)