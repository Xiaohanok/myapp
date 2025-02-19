class Config:
    """
    Flask 配置类，存放应用的基础配置信息
    """
    SECRET_KEY = 'your-secret-key'  # 用于会话加密
    FLASK_ENV = 'development'
    DEBUG = FLASK_ENV == 'development'

    # MySQL 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:xiaozihan@localhost/tourism'  # 修改为你的 MySQL 配置
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 禁用对象修改追踪