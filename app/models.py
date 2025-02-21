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

class Hotel(db.Model):
    __tablename__ = 'hotels'

    hotel_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hotel_name = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Hotel {self.hotel_name}>'

