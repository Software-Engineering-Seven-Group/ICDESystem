from database_manager import user_infor_manager
from flask import render_template, request, session, redirect, url_for, flash, Blueprint
edit_profile_blueprint = Blueprint('edit_profile_blueprint', __name__)
@edit_profile_blueprint.route('/edit_profile', methods=['GET', 'POST'])
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