from flask import request
from flask_pymongo import PyMongo
from app_instance import app

#mongodb base class
class MongoDBManager():
    def __init__(self, app_instance):
        self.mongo = PyMongo(app_instance)
        #attention: add the collection name when a table is added.
        self.collection_names = ['userInfo']

    #get the collection by collection_name
    def get_collection(self, collection_name):
        return self.mongo.db[collection_name]

    #get target entry list of all items
    def list_all_items_target_entry(self, collection_name, target_entry):
        data = self.mongo.db[collection_name].find()
        res_list = []
        for item in data:
            res_list.append(item[target_entry])
        return res_list

    #insert item to collection with collection_name
    def insert_item_to_collection(self, collection_name, item):
        return self.get_collection(collection_name).insert_one(item)

    #find the item from collection with request
    def find_item_from_collection_with_request(self, collection_name, item_key):
        return self.get_collection(collection_name).find_one({item_key: request.form[item_key]})

    #find the item from collection without request
    def find_item_from_collection(self, collection_name, item_key, item_value):
        return self.get_collection(collection_name).find_one({item_key: item_value})

    def update_item_in_collection(self, collection_name, query, update_data):
        self.get_collection(collection_name).update_one(query, update_data)

    def update_user_info(self, username, updated_data):
        return self.get_collection('userInfo').update_one({'username': username}, {'$set': updated_data})
    #todo: insert data/ delete data/ modify data/ ... add the basic database interface

#global database manager
mongo_manager = MongoDBManager(app)

#The different table has its own logic
class UserInfoCollection():
    def __init__(self, ):
        self.collection_name = 'userInfo'

    def insert_one_user(self, item):
        return mongo_manager.insert_item_to_collection(self.collection_name, item)

    def find_user_info(self, user_name):
        return mongo_manager.find_item_from_collection_with_request(self.collection_name, user_name)
    def list_users_name(self):
        users_name_list = mongo_manager.list_all_items_target_entry(self.collection_name, 'username')
        return users_name_list

    def find_user_by_username(self, username):
        return mongo_manager.find_item_from_collection(self.collection_name, 'username', username)

    def update_user_info(self, username, new_name, new_phone, new_email, new_sex, new_age, new_secret):
        mongo_manager.get_collection(self.collection_name).update_one(
            {"username": username},
            {
                "$set": {
                    "name": new_name,
                    "phone": new_phone,
                    "email": new_email,
                    "sex": new_sex,
                    "age": new_age,
                    "secret": new_secret
                }
            }
        )

    def get_user_info(self, username):
        user_data = mongo_manager.get_collection(self.collection_name).find_one({"username": username})
        return user_data if user_data else None
    def update_password(self, username, new_password):
        mongo_manager.update_item_in_collection(self.collection_name, {'username': username}, {'$set': {'password': new_password}})
    #todo: add user data logic info according to the structure of userinfo table, for example:
    def get_user_nationality(self, user_name):
        return ''


#a global userinfor manager
user_infor_manager = UserInfoCollection()

#The cities table
class CitiesInfoCollection():
    def __init__(self, ):
        self.collection_name = 'citychara'

    # the cities infor cannot be added
    # todo: administrator addition function
    def insert_one_city(self, item):
        pass

    def find_city_infor(self, city_name):
        return mongo_manager.find_item_from_collection(self.collection_name, 'city_name', city_name)

    def get_city_all_data(self, city_name):
        city_data = {
            "popularity": self.get_city_popularity(city_name),
            "humanistic": self.get_city_humanistic(city_name),
            "historical": self.get_city_historical(city_name),
            "natural": self.get_city_natural(city_name),
            "metropolis": self.get_city_metropolis(city_name),
            "forest": self.get_city_forest(city_name),
            "mountain": self.get_city_mountain(city_name),
            "river": self.get_city_river(city_name),
            "sea": self.get_city_sea(city_name),
            "lake": self.get_city_lake(city_name),
            "cost": self.get_city_cost(city_name)
        }
        return city_data

    def list_cities_name(self):
        cities_name_list = mongo_manager.list_all_items_target_entry(self.collection_name, 'city_name')
        return cities_name_list

    def get_city_popularity(self, city_name):
        return self.find_city_infor(city_name)['popularity']

    def get_city_humanistic(self, city_name):
        return self.find_city_infor(city_name)['humanistic']

    def get_city_historical(self, city_name):
        return self.find_city_infor(city_name)['historical']

    def get_city_natural(self, city_name):
        return self.find_city_infor(city_name)['natural']

    def get_city_forest(self, city_name):
        return self.find_city_infor(city_name)['forest']

    def get_city_mountain(self, city_name):
        return self.find_city_infor(city_name)['mountain']

    def get_city_river(self, city_name):
        return self.find_city_infor(city_name)['river']

    def get_city_sea(self, city_name):
        return self.find_city_infor(city_name)['sea']

    def get_city_lake(self, city_name):
        return self.find_city_infor(city_name)['lake']

    def get_city_cost(self, city_name):
        return self.find_city_infor(city_name)['cost']

    def get_city_metropolis(self, city_name):
        return self.find_city_infor(city_name)['metropolis']

#a global cities infor manager
city_infor_manager = CitiesInfoCollection()

def city_infor_manager_test_case():
    print(city_infor_manager.list_cities_name())
    print('city population:', city_infor_manager.get_city_popularity('Calgary'))
    print('city metropolis:', city_infor_manager.get_city_metropolis('Calgary'))
    print('city mountain:', city_infor_manager.get_city_mountain('Calgary'))
    print('city historical:', city_infor_manager.get_city_historical('Calgary'))
    print('city humanistic:', city_infor_manager.get_city_humanistic('Calgary'))
    print('city natural:', city_infor_manager.get_city_natural('Calgary'))

class PreferenceInforCollection():
    def __init__(self, ):
        self.collection_name = 'preferenceInfo'

    def find_user_preference_infor(self, user_name):
        return mongo_manager.find_item_from_collection(self.collection_name, 'username', user_name)

    def insert_one_user_preference_data_item(self, item):
        return mongo_manager.insert_item_to_collection(self.collection_name, item)

    def get_daily_workload(self, user_name):
        return self.find_user_preference_infor(user_name)['daily_workload']

    def get_address_urbanization(self, user_name):
        return self.find_user_preference_infor(user_name)['address_urbanization']

    def get_quiet_chara(self, user_name):
        return self.find_user_preference_infor(user_name)['quiet_chara']

    def get_noisy_chara(self, user_name):
        return self.find_user_preference_infor(user_name)['noisy_chara']

    def get_sports(self, user_name):
        return self.find_user_preference_infor(user_name)['sports']

    def get_prefer_solitude(self, user_name):
        return self.find_user_preference_infor(user_name)['prefer_solitude']

    def get_prefer_history(self, user_name):
        return self.find_user_preference_infor(user_name)['prefer_history']

    def get_prefer_culture(self, user_name):
        return self.find_user_preference_infor(user_name)['prefer_culture']

    def get_prefer_nature(self, user_name):
        return self.find_user_preference_infor(user_name)['prefer_nature']

    def get_user_all_preference_data(self, user_name):
        preference_data = {
            "daily_workload": self.get_daily_workload(user_name),
            "address_urbanization": self.get_address_urbanization(user_name),
            "quiet_chara": self.get_quiet_chara(user_name),
            "noisy_chara": self.get_noisy_chara(user_name),
            "sports": self.get_sports(user_name),
            "prefer_solitude": self.get_prefer_solitude(user_name),
            "prefer_history": self.get_prefer_history(user_name),
            "prefer_culture": self.get_prefer_culture(user_name),
            "prefer_nature": self.get_prefer_nature(user_name)
        }
        return preference_data


user_preference_infor_manager = PreferenceInforCollection()


if __name__ == '__main__':
    city_infor_manager_test_case()

