from database_manager import user_infor_manager
from flask import  render_template, request, redirect, url_for, flash, Blueprint
reset_password_blueprint = Blueprint('reset_password_blueprint', __name__)
@reset_password_blueprint.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        username = request.form['username']
        secret_answer = request.form['secret']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password != confirm_password:
            flash('Inconsistency between the two input passwords！')
            return render_template('reset_password.html')

        user_info = user_infor_manager.find_user_by_username(username)
        if not user_info:
            flash(f'Cannot find username：{username}！')
            return render_template('reset_password.html')

        if user_info.get('secret') != secret_answer:
            flash('Security Question is not correct ！')
            return render_template('reset_password.html')

        user_infor_manager.update_password(username, new_password)
        flash('Password updated successfully！')
        return redirect(url_for('login_blueprint.login'))

    return render_template('reset_password.html')