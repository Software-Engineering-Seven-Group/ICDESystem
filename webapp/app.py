
from crawler.Get_Hotel import Get_booking_hotel
from database_manager import MongoDBManager, UserInfoCollection, mongo_manager, user_infor_manager, \
    user_preference_infor_manager, Moments
from app_instance import app
from questionnaire import questionnaire_api, questionnaire
from data_displayer import displayer_api, enter_analysis_page
from flask import Flask, render_template, request, session, redirect, url_for, flash
from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from search import search_api
from werkzeug.utils import secure_filename
import os
from pymongo import MongoClient, DESCENDING
from datetime import datetime
#bind questionnaire api
app.register_blueprint(questionnaire_api)
app.register_blueprint(search_api)
app.register_blueprint(displayer_api)
app.secret_key = 'your_secret_key'  # replace with your secret key
"“Homepage, redirect”"
app.config['MAX_CONTENT_PATH'] = '16 * 1024 * 1024'
moments = Moments()
@app.route('/')
def home():
    return render_template("index.html")

#Login Form
class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    captcha = StringField('Captcha', [DataRequired()])
    submit = SubmitField('Login')
"User info for registration"
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

        flash('Username is existed！PlZ change another one!')
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

        flash('.username or password is incorrect！')
    return render_template('login.html')
#"Logout"
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
#"Login State"
@app.route('/')
def index():
    is_logged_in = 'username' in session
    return render_template('index.html', is_logged_in=is_logged_in, username=session.get('username'))

#Editing Personal Information
@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    print("DEBUG: session contents:", session)
    print("DEBUG: request.form contents:", request.form)
    if 'username' not in session:
        flash('Please Login!')
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
        flash('Update Successfully！')
        return redirect(url_for('home'))

    user_data = user_infor_manager.get_user_info(username)
    return render_template('edit_profile.html', user_data=user_data)
#Changing Password
@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        username = request.form['username']
        secret_answer = request.form['secret']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password != confirm_password:
            flash('Inconsistency between the two input passwords！')
            return render_template('reset_password.html')
        # validate user info
        user_info = user_infor_manager.find_user_by_username(username)
        print(f"Queried user info for {username}: {user_info}")
        if not user_info:
            flash(f'Cannot find username：{username}！')
            return render_template('reset_password.html')
        print(f"Database secret for {username}: {user_info.get('secret')}")
        print(f"Submitted secret: {secret_answer}")
        if user_info.get('secret') != secret_answer:
            flash('Security Question is not correct ！')
            return render_template('reset_password.html')

        # Update Password
        user_infor_manager.update_password(username, new_password)
        flash('Updating password successfully！')
        return redirect(url_for('login'))

    return render_template('reset_password.html')


#database info
app.config["MONGO_URI"] = "mongodb://localhost:27017/Tripedia"
app.secret_key = "mysecretkey"
app.config['UPLOAD_FOLDER'] = 'static/uploads'

mongo_client = MongoClient(app.config["MONGO_URI"])
db = mongo_client.Tripedia
moments_collection = db.moments
#momentsData
@app.route('/moments')
def show_moments():
    moments_data = moments_collection.find().sort("create_at", DESCENDING)
    return render_template('moments.html', moments=moments_data)
#moments_upload
@app.route('/upload_moment', methods=['POST'])
def upload_moment():
    text = request.form['text']
    if 'username' in session:
        username = session['username']
    else:
        username = None
    if 'image' in request.files:
        image = request.files['image']
        if image.filename != '':
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_url = f'uploads/{filename}'
        else:
            image_url = None
    else:
        image_url = None
    create_at = datetime.now()
    create_at = create_at.strftime("%Y-%m-%d %I:%M %p")
    moment_data = {
        'text': text,
        'image_url': image_url,
        'create_at': create_at,
        'username': username
    }
    moments_collection.insert_one(moment_data)
    return redirect(url_for('show_moments'))


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)