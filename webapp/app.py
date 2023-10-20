
from crawler.Get_Hotel import Get_booking_hotel
from database_manager import MongoDBManager, UserInfoCollection, mongo_manager, user_infor_manager, user_preference_infor_manager
from app_instance import app
from questionnaire import questionnaire_api, questionnaire
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
"“首页，重定向”"
@app.route('/')
def home():
    return render_template("index.html")

# image_captcha = ImageCaptcha()
# #验证码位数(4)
# def generate_captcha():
#     return ''.join([str(random.randint(0, 9)) for _ in range(4)])
# #验证码模块
# @app.route('/captcha/')
# def captcha():
#     code = generate_captcha()
#     session['captcha'] = code
#     data = image_captcha.generate(code)
#     response = make_response(data.read())
#     response.content_type = 'image/png'
#     return response
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

        if existing_user is None:
            user_infor_manager.insert_one_user({
                'username': request.form['username'],
                'name': request.form['name'],
                'password': request.form['password'],
                'sex': request.form['sex'],
                'age': request.form['age'],
                'phone': request.form['phone'],
                'email': request.form['email']
            })
            session['username'] = request.form['username']
            return redirect(url_for('login'))

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
                return redirect(url_for("questionnaire_api.questionnaire"))

        flash('用户名或密码不正确！')
    return render_template('login.html')




if __name__ == '__main__':
    app.run(debug=True)