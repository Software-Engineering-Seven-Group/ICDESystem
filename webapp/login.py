from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from database_manager import user_infor_manager
login_blueprint = Blueprint('login_blueprint', __name__)
@login_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        login_user = user_infor_manager.find_user_info('username')

        if login_user:
            if request.form['password'] == login_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for("home"))

        flash('.username or password is incorrect！')
    return render_template('login.html')
@login_blueprint.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login_blueprint.index'))
@login_blueprint.route('/')
def index():
    is_logged_in = 'username' in session
    return render_template('index.html', is_logged_in=is_logged_in, username=session.get('username'))