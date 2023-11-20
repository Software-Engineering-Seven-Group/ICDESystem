from database_manager import user_infor_manager
from flask import render_template, request, session, redirect, url_for, flash, Blueprint
register_blueprint = Blueprint('register_blueprint', __name__)
@register_blueprint.route('/register', methods=['POST', 'GET'])
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
                'email': request.form['email'],
                'secret': request.form['secret']
            })
            session['username'] = request.form['username']
            return redirect(url_for('questionnaire_api.questionnaire'))
        flash('Username is existed！PlZ change another one!')
        return redirect(url_for('register'))
    return render_template('register.html')
