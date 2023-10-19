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

    #insert item to collection with collection_name
    def insert_item_to_collection(self, collection_name, item):
        return self.get_collection(collection_name).insert_one(item)

    #find the item from collection with request
    def find_item_from_collection_with_request(self, collection_name, item_key):
        return self.get_collection(collection_name).find_one({item_key: request.form[item_key]})

    #find the item from collection without request
    def find_item_from_collection(self, collection_name, item_key, item_value):
        return self.get_collection(collection_name).find_one({item_key: item_value})


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
        return mongo_manager.find_item_from_collection(self.collection_name, 'user_name', user_name)

    def insert_one_user_preference_data_item(self, item):
        return mongo_manager.insert_item_to_collection(self.collection_name, item)

user_preference_infor_manager = PreferenceInforCollection()


if __name__ == '__main__':
    city_infor_manager_test_case()

