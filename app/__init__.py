from flask import Flask
from .models import db  # 导入 db 对象

def create_app():
    """
    创建并配置 Flask 应用实例
    """
    app = Flask(__name__)

    # 配置应用
    app.config.from_object('config.Config')

    # 初始化数据库
    db.init_app(app)

    # 导入并注册蓝图
    from .routes import main
    app.register_blueprint(main)

    return app