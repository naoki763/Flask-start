from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2

db = SQLAlchemy()

def create_app():
    # appの設定
    app = Flask(__name__, instance_relative_config=True)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://aho:aho@localhost/mymedia'
    
    # DBの設定
    db.init_app(app)
    
    with app.app_context():
        from flask_app import models
        db.create_all()  # モデルに基づいてデータベーステーブルを作成

    from flask_app.app import bp
    app.register_blueprint(bp)
    
    return app