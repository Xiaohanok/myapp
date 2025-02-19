from flask import Flask
from app import create_app
from app.models import db

app = create_app()

# 初始化数据库
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)