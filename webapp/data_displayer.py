from flask import  session
from flask import render_template, request, redirect, url_for, Blueprint
from data_analyser import KNNDataAnalayzer

displayer_api = Blueprint('displayer_api', __name__)

# preprocess of data before enter analysis page
def enter_analysis_page():
    analyzer = KNNDataAnalayzer()
    recommend_cities_name_list, recommend_cities_priority_list = analyzer.recommend_cities(session['username'])

    max_priority, min_priority = 0, 999999999
    for priority_value in recommend_cities_priority_list:
        if priority_value > max_priority:
            max_priority = priority_value
        if priority_value < min_priority:
            min_priority = priority_value

    recommend_rates = []
    for priority_value in recommend_cities_priority_list:
        current_recommend_rate = ((priority_value - min_priority) / (max_priority - min_priority)) * 100.0
        recommend_rates.append(current_recommend_rate)

    popular_cities_name_list, popular_cities_priority_list = analyzer.popular_cities()

    return render_template("analysis.html", data_keys_list=recommend_cities_name_list, data_values_list=recommend_rates,
                           data_keys_list_popular=popular_cities_name_list, data_values_list_popular=popular_cities_priority_list)



#process analysis logic
@displayer_api.route('/analysis', methods=['back'])
def analysis():
    if request.method == 'back':
        return redirect(url_for('home'))

    return render_template('analysis.html')

