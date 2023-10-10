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

    #insert item to collection with collection_name
    def insert_item_to_collection(self, collection_name, item):
        return self.get_collection(collection_name).insert_one(item)

    #find the item from collection
    def find_item_from_collection(self, collection_name, item_key_name):
        return self.get_collection(collection_name).find_one({item_key_name: request.form[item_key_name]})

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
        return mongo_manager.find_item_from_collection(self.collection_name, user_name)


    #todo: add user data logic info according to the structure of userinfo table, for example:
    def get_user_nationality(self, user_name):
        return ''


#a global userinfor manager
user_infor_manager = UserInfoCollection()