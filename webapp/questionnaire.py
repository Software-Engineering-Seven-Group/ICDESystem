from flask import render_template, request, redirect, url_for, Blueprint
from database_manager import user_preference_infor_manager

questionnaire_api = Blueprint('questionnaire_api', __name__)

#pre-process of questionnaire data
def prcess_questionnaire_data(workload, area, history, people, alone, hum, sports, water):
    preference_data = {
        "daily_workload":0,
        "address_urbanization":0,
        "quiet_chara":0,
        "noisy_chara":0,
        "sports":0,
        "prefer_solitude":0,
        "prefer_history": 0,
        "prefer_culture": 0,
        "prefer_nature": 0
    }

    preference_data['daily_workload'] = workload * 20
    preference_data['address_urbanization'] = area * 20
    preference_data['quiet_chara'] = alone * 20
    preference_data['noisy_chara'] = people * 20
    preference_data['sports'] = sports
    preference_data['prefer_solitude'] = alone * 20
    preference_data['prefer_history'] = history * 20
    preference_data['prefer_culture'] = hum * 20
    preference_data['prefer_nature'] = water * 20

    return preference_data


@questionnaire_api.route('/questionnaire', methods=['POST', 'GET'])
def questionnaire():
    if request.method == 'POST':
        existing_preference_infor = user_preference_infor_manager.find_user_preference_infor('username')

        if existing_preference_infor is None:
            processed_data = prcess_questionnaire_data(
                request.form['workload'],
                request.form['area'],
                request.form['history'],
                request.form['people'],
                request.form['alone'],
                request.form['hum'],
                request.form['sports'],
                request.form['water'],
            )

            user_preference_infor_manager.insert_one_user_preference_data_item(processed_data)
            return redirect(url_for('home'))

    return render_template('questionnaire.html')

