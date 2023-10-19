from database_manager import user_preference_infor_manager, city_infor_manager
from queue import PriorityQueue

#A simple data analyzer
class KNNDataAnalayzer():
    #initialize algorithm parameters
    #change the weights, change the performance
    def __init__(self):
        self.humanistic_weight = 1.5
        self.historical_weight = 0.8
        self.natural_weight = 1.7
        self.metropolis_weight = 1.1
        self.forest_weight = 10.0
        self.mountain_weight = 10.0
        self.river_weight = 10.0
        self.sea_weight = 10.0
        self.lake_weight = 10.0
        self.cost_weight = 20.0
        self.priority_num = 5

    #transfer the user's mood data to the appropriate city data
    def map_preference_to_city(self, user_name):
        if user_name == None:
            return None

        #default city data
        user_dream_city_data = {
            "humanistic": 0,
            "historical": 0,
            "natural": 0,
            "metropolis": 0,
            "forest": 0,
            "mountain": 0,
            "river": 0,
            "sea": 0,
            "lake": 0,
            "cost": 0
        }

        #map current login user's preference data
        preference_data = user_preference_infor_manager.get_user_all_preference_data(user_name)
        if preference_data == None:
            return user_dream_city_data
        user_dream_city_data['humanistic'] = preference_data['daily_workload'] * 0.3 + preference_data['prefer_culture'] * 0.7
        user_dream_city_data['historical'] = preference_data['prefer_history'] * 0.7 + preference_data['prefer_solitude'] * 0.3
        user_dream_city_data['natural'] = preference_data['prefer_nature'] * 0.6 + preference_data['quiet_chara'] * 0.4
        user_dream_city_data['metropolis'] = preference_data['noisy_chara'] * 0.5 + (100 - preference_data['address_urbanization']) * 0.5
        user_dream_city_data['forest'] = preference_data['quiet_chara'] > 50
        user_dream_city_data['mountain'] = preference_data['sports'] >= 4
        user_dream_city_data['river'] =  preference_data['sports'] >= 2
        user_dream_city_data['sea'] = preference_data['sports'] >= 3
        user_dream_city_data['lake'] = preference_data['sports'] >= 1
        user_dream_city_data['cost'] = (preference_data['noisy_chara'] * 0.5 + (100 - preference_data['daily_workload']) * 0.5) / 10.0
        return user_dream_city_data

    #calculate the distance between current city and dream city
    def loss_function(self, current_city, user_dream_city):
        humanistic_distance = abs(current_city['humanistic'] - user_dream_city['humanistic']) * self.humanistic_weight
        historical_distance = abs(current_city['historical'] - user_dream_city['historical']) * self.historical_weight
        natural_distance = abs(current_city['natural'] - user_dream_city['natural']) * self.natural_weight
        metropolis_distance = abs(current_city['metropolis'] - user_dream_city['metropolis']) * self.metropolis_weight
        forest_distance = abs(current_city['forest'] - user_dream_city['forest']) * self.forest_weight
        mountain_distance = abs(current_city['mountain'] - user_dream_city['mountain']) * self.mountain_weight
        river_distance = abs(current_city['river'] - user_dream_city['river']) * self.river_weight
        sea_distance = abs(current_city['sea'] - user_dream_city['sea']) * self.sea_weight
        lake_distance = abs(current_city['lake'] - user_dream_city['lake']) * self.lake_weight
        cost_distance = abs(current_city['cost'] - user_dream_city['cost']) * self.cost_weight
        final_weight = humanistic_distance + historical_distance + natural_distance + metropolis_distance + forest_distance + mountain_distance + river_distance + sea_distance + lake_distance + cost_distance
        return final_weight

    #return the recommend cities
    def recommend_cities(self, user_name):
        user_dream_city_data = self.map_preference_to_city(user_name)
        cities_namelists = city_infor_manager.list_cities_name()
        cities_queue = PriorityQueue()
        for city_name in cities_namelists:
            current_city = city_infor_manager.get_city_all_data(city_name)
            loss_value = self.loss_function(current_city, user_dream_city_data)
            cities_queue.put((loss_value, city_name))

        recommend_cities_name_list = []
        recommend_cities_priority_list = []
        for i in range(0, self.priority_num):
            cur_priority_num = cities_queue.get()[0]
            cur_city_name = cities_queue.get()[1]
            recommend_cities_name_list.append(cur_city_name)
            recommend_cities_priority_list.append(cur_priority_num)

        return recommend_cities_name_list, recommend_cities_priority_list

#the test case of KNN data analyser
def KNNDataAnalayzer_test_case():
    analyzer_instance = KNNDataAnalayzer()
    recommend_cities_values, recommend_cities_names= analyzer_instance.recommend_cities('zhangyulin')
    print(recommend_cities_values)
    print(recommend_cities_names)

if __name__ == '__main__':
    KNNDataAnalayzer_test_case()

