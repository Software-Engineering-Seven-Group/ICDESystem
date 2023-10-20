from flask import  session
from flask import render_template, request, redirect, url_for, Blueprint
from database_manager import user_preference_infor_manager
from data_displayer import enter_analysis_page
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

    preference_data['username'] = session['username']
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
        existing_preference_infor = user_preference_infor_manager.find_user_preference_infor(session['username'])

        if existing_preference_infor is None:
            processed_data = prcess_questionnaire_data(
                int(request.form['workload'][0]),
                int(request.form['area'][0]),
                int(request.form['history']),
                int(request.form['people']),
                int(request.form['alone']),
                int(request.form['hum']),
                int(request.form['sports']),
                int(request.form['water']),
            )
            #print('process_data:',processed_data)
            user_preference_infor_manager.insert_one_user_preference_data_item(processed_data)
            existing_preference_infor2 = user_preference_infor_manager.find_user_preference_infor(session['username'])
            #print('existing:', existing_preference_infor2)
            return enter_analysis_page()
            #return redirect(url_for('home'))

    return render_template('questionnaire.html')

