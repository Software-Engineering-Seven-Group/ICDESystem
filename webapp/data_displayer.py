from flask import  session
from flask import render_template, request, redirect, url_for, Blueprint
from data_analyser import KNNDataAnalayzer
from database_manager import city_infor_manager, user_preference_infor_manager

displayer_api = Blueprint('displayer_api', __name__)

def generate_introduce_of_the_recommend_city(city_name, user_name):
    generate_introduce = 'Bonjour! According to the psychological testing, the best tourist destination for your is ' + city_name + '. '

    #About work load
    user_workload = user_preference_infor_manager.get_daily_workload(user_name)
    city_nature = city_infor_manager.get_city_natural(city_name)
    if user_workload > 50:
        generate_introduce =  generate_introduce + city_name + ' has awsome natural environment (the natural rate is ' + str(city_nature)  + '), you can release your work load and enjoy yourself. '

    user_history = user_preference_infor_manager.get_prefer_history(user_name)
    city_history = city_infor_manager.get_city_historical(city_name)
    if user_history > 50:
        generate_introduce = generate_introduce + city_name + ' is also a famous historical city (the historical rate is ' + str(city_history) + '), you can find a great number of interesting history stories here. '

    user_culture = user_preference_infor_manager.get_prefer_culture(user_name)
    city_culture = city_infor_manager.get_city_humanistic(city_name)
    if user_culture > 50:
        generate_introduce = generate_introduce + city_name + ' is well-known because of her culture (the historical rate is ' + str(city_culture) + '), you can meet interesting people here. '

    user_solitude = user_preference_infor_manager.get_prefer_solitude(user_name)
    city_solitude  = city_infor_manager.get_city_metropolis(city_name)
    if user_solitude < 50:
        generate_introduce = generate_introduce + city_name + ' is a peace place to relax (the city rate is ' + str(city_solitude) + '), you can find a great number of friends. '

    return generate_introduce

def generate_introduce_of_the_popular_city(city_name):
    generate_introduce = 'In this season, the most popular city is ' + city_name + '. '
    return generate_introduce

def recommend_the_best_city():
    if session['username'] != '':
        analyzer = KNNDataAnalayzer()
        recommend_cities_name_list, recommend_cities_priority_list = analyzer.recommend_cities(session['username'])
        return recommend_cities_name_list[4]
    return 'Montreal'

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
        current_recommend_rate = ((priority_value - min_priority) / (max_priority - min_priority)) * 90.0 + 10.0
        recommend_rates.append(current_recommend_rate)

    popular_cities_name_list, popular_cities_priority_list = analyzer.popular_cities()

    preference_introduction =  generate_introduce_of_the_recommend_city(recommend_cities_name_list[4], session['username'])
    popular_introduction = generate_introduce_of_the_popular_city(popular_cities_name_list[0])

    print(recommend_rates)
    print(recommend_rates)
    print(recommend_rates)

    return render_template("analysis.html", data_keys_list=recommend_cities_name_list, data_values_list=recommend_rates,
                           data_keys_list_popular=popular_cities_name_list, data_values_list_popular=popular_cities_priority_list,
                           recommend_city_word = preference_introduction, popular_city_word = popular_introduction)

#process analysis logic
@displayer_api.route('/analysis')
def analysis():
    return enter_analysis_page()

#the test case for recommend city introduction
def generate_preference_introduction_test_case():
    analyzer = KNNDataAnalayzer()
    recommend_cities_name_list, recommend_cities_priority_list = analyzer.recommend_cities('zhangyulin')
    introduction = generate_introduce_of_the_recommend_city(recommend_cities_name_list[0], 'zhangyulin')
    print(introduction)

#the test case for popular city introduction
def generate_popular_introduce_test_case():
    analyzer = KNNDataAnalayzer()
    popular_cities_name_list, popular_cities_priority_list = analyzer.popular_cities()
    popular_introduction = generate_introduce_of_the_popular_city(popular_cities_name_list[0])
    print(popular_introduction)


if __name__ == '__main__':
    generate_preference_introduction_test_case()
    generate_popular_introduce_test_case()
