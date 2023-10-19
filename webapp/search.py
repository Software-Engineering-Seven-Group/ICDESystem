from flask import render_template, request, redirect, url_for, Blueprint,flash
from database_manager import user_preference_infor_manager
from database_manager import MongoDBManager, UserInfoCollection, mongo_manager, user_infor_manager, user_preference_infor_manager
import copy
search_api = Blueprint('search_api', __name__)
from crawler.Get_Hotel import Get_booking_hotel
@search_api.route('/search', methods=['POST', 'GET'])  # Search
def search():
    hotels = mongo_manager.get_collection("Hotels")

    if request.method == 'POST':
        Keyword = request.form['Keyword']
        checkin = request.form['checkin']
        checkout = request.form['checkout']
        exist_data = hotels.find({"Location": {"$regex": Keyword}}).limit(10)
        exist_datas = list(copy.deepcopy(exist_data))
        list_num = len(exist_datas)
        if list_num > 0:
            print('载入数据')
            # print(exist_data[0])
            return render_template('search.html', results=exist_datas)

        search_data = Get_booking_hotel(Keyword, checkin, checkout)
        if search_data:
            list_data = search_data.json()['data']['searchQueries']['search']['results']
            for each_data in list_data:
                insert_data = {
                    'Hotel_name': each_data['displayName']['text'],
                    'Location': each_data['location']['displayLocation'],
                    'Images': 'https://cf.bstatic.com/' +
                              each_data['basicPropertyData']['photos']['main']['highResJpegUrl']['relativeUrl'],
                    'score': each_data['basicPropertyData']['reviewScore']['score'],
                    'Price': each_data['blocks'][0]['finalPrice']['amount'],
                    'address': each_data['basicPropertyData']['location']
                }
                # print(insert_data)
                hotels.insert_one(insert_data)
        flash('搜索成功')
        exist_data = hotels.find({"Location": {"$regex": Keyword}}).limit(10)
        exist_datas = list(copy.deepcopy(exist_data))
        return render_template('search.html', results=exist_datas)
    return render_template('search.html')