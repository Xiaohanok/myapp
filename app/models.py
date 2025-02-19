from flask_sqlalchemy import SQLAlchemy

# 创建 SQLAlchemy 实例
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(100))

    def __repr__(self):
        return f'<User {self.username}>'