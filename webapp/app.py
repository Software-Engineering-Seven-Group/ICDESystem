
from crawler.Get_Hotel import Get_booking_hotel
from database_manager import MongoDBManager, UserInfoCollection, mongo_manager, user_infor_manager, user_preference_infor_manager
from app_instance import app
from questionnaire import questionnaire_api, questionnaire
from data_displayer import displayer_api, enter_analysis_page
from flask import Flask, render_template, request, session, redirect, url_for, flash, make_response
from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from captcha.image import ImageCaptcha
from flask_wtf import FlaskForm
from search import search_api
import copy
import random

#bind questionnaire api
app.register_blueprint(questionnaire_api)
app.register_blueprint(search_api)
app.register_blueprint(displayer_api)
app.secret_key = 'your_secret_key'  # replace with your secret key
"“首页，重定向”"
@app.route('/')
def home():
    return render_template("index.html")

#用户登录表
class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    captcha = StringField('Captcha', [DataRequired()])
    submit = SubmitField('Login')
"插入信息（注册用户信息）"
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        existing_user = user_infor_manager.find_user_info('username')
        # existing_user = user_infor_manager.find_user_info(request.form['username'])
        if existing_user is None:
            user_infor_manager.insert_one_user({
                'username': request.form['username'],
                'name': request.form['name'],
                'password': request.form['password'],
                'sex': request.form['sex'],
                'age': request.form['age'],
                'phone': request.form['phone'],
                'email': request.form['email'],
                'secret': request.form['secret']
            })
            session['username'] = request.form['username']
            return redirect(url_for('questionnaire_api.questionnaire'))

        flash('用户名已经存在，请换一个用户名！')
        return redirect(url_for('register'))

    return render_template('register.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        login_user = user_infor_manager.find_user_info('username')

        if login_user:
            if request.form['password'] == login_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for("home"))

        flash('.用户名或密码不正确！')
    return render_template('login.html')
#"登出"
@app.route('/logout')
def logout():
    session.pop('username', None)  # 从 session 中移除 username
    return redirect(url_for('index'))  # 重定向到主页或其他适当的页面
#"登录状态"
@app.route('/')
def index():
    is_logged_in = 'username' in session
    return render_template('index.html', is_logged_in=is_logged_in, username=session.get('username'))

#编辑个人资料
@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    print("DEBUG: session contents:", session)
    print("DEBUG: request.form contents:", request.form)
    if 'username' not in session:
        flash('请先登录!')
        return redirect(url_for('login'))

    username = session['username']

    if request.method == 'POST':
        new_name = request.form['name']
        new_phone = request.form['phone']
        new_email = request.form['email']
        new_sex = request.form.get('sex')
        new_age = int(request.form['age'])
        new_secret = request.form['secret']

        user_infor_manager.update_user_info(username, new_name, new_phone, new_email, new_sex, new_age, new_secret)
        flash('资料已更新成功！')
        return redirect(url_for('home'))

    user_data = user_infor_manager.get_user_info(username)
    return render_template('edit_profile.html', user_data=user_data)
#修改密码
@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        username = request.form['username']
        secret_answer = request.form['secret']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password != confirm_password:
            flash('两次输入的密码不一致！')
            return render_template('reset_password.html')
        # 验证用户信息
        user_info = user_infor_manager.find_user_by_username(username)
        print(f"Queried user info for {username}: {user_info}")
        if not user_info:
            flash(f'找不到用户名：{username}！')
            return render_template('reset_password.html')
        print(f"Database secret for {username}: {user_info.get('secret')}")
        print(f"Submitted secret: {secret_answer}")
        if user_info.get('secret') != secret_answer:
            flash('密保问题不正确！')
            return render_template('reset_password.html')

        # 更新密码
        user_infor_manager.update_password(username, new_password)
        flash('密码已更新成功！')
        return redirect(url_for('login'))

    return render_template('reset_password.html')






if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)