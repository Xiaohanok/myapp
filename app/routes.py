from flask import render_template, flash, redirect, url_for, request, session
from app.models import User
from app import db
from flask import Blueprint
from app.models1.hotel import add_hotel, get_all_hotels, update_hotel, delete_hotel

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

@main.route('/hotels', methods=['GET'])
def list_hotels():
    hotels = get_all_hotels()
    return render_template('hotels.html', hotels=hotels)

@main.route('/hotels/add', methods=['POST'])
def add_new_hotel():
    hotel_name = request.form.get('hotel_name')
    location = request.form.get('location')
    description = request.form.get('description')
    price = request.form.get('price')
    add_hotel(hotel_name, location, description, price)
    flash('酒店添加成功！')
    return redirect(url_for('main.list_hotels'))

@main.route('/hotels/update/<int:hotel_id>', methods=['POST'])
def update_existing_hotel(hotel_id):
    hotel_name = request.form.get('hotel_name')
    location = request.form.get('location')
    description = request.form.get('description')
    price = request.form.get('price')
    update_hotel(hotel_id, hotel_name, location, description, price)
    flash('酒店信息更新成功！')
    return redirect(url_for('main.list_hotels'))

@main.route('/hotels/delete/<int:hotel_id>', methods=['POST'])
def delete_existing_hotel(hotel_id):
    delete_hotel(hotel_id)
    flash('酒店删除成功！')
    return redirect(url_for('main.list_hotels'))