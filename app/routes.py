from app.function import *
from flask import render_template, flash, redirect, url_for, request, session
from app.models import User
from app import db

main = Blueprint('main', __name__)


# 主页路由，访问根路径 '/'
@main.route('/', endpoint='home')
def home():
    return render_template('index.html', title="Flask Test Page")


# 登录路由
@main.route('/login', methods=['GET', 'POST'], endpoint='login')
def login():
    if request.method == 'POST':
        # 获取表单数据
        username = request.form['username']
        password = request.form['password']

        # 查找用户
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:  # 直接比较密码
            session['user_id'] = user.id
            flash('登录成功！', 'success')
            return redirect(url_for('main.hello'))
        else:
            flash('用户名或密码错误', 'danger')

    return render_template('login.html')



# 访问 hello 路由
@main.route('/hello', endpoint='hello')
def hello():
    # 检查用户是否登录
    if 'user_id' not in session:
        return redirect(url_for('main.login'))
    return "Hello, Flask!"

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        
        # 检查用户是否已存在
        user = User.query.filter_by(username=username).first()
        if user:
            flash('用户名已存在，请选择其他用户名')
            return redirect(url_for('main.register'))
            
        # 创建新用户
        new_user = User(
            username=username,
            email=email,
            password=password  # 直接存储明文密码
        )
        
        # 保存到数据库
        db.session.add(new_user)
        db.session.commit()
        
        flash('注册成功！请登录')
        return redirect(url_for('main.login'))
        
    return render_template('register.html')