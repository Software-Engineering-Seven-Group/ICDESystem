from flask import render_template, request, redirect, url_for, Blueprint,flash,jsonify,render_template
from database_manager import user_preference_infor_manager
from database_manager import MongoDBManager, UserInfoCollection, mongo_manager, user_infor_manager, user_preference_infor_manager
import copy
from crawler.Get_Hotel import Get_booking_hotel
from crawler.Get_Tickets import get_tickets_list
from flask_cors import CORS

search_api = Blueprint('search_api', __name__)

CORS(search_api)
@search_api.route('/search_hotel', methods=['POST', 'GET'])  # Search
def search_hotel():
    hotels = mongo_manager.get_collection("Hotels")

    if request.method == 'POST':
        # print(request.form)
        Keyword = request.form['Keyword']
        checkin = request.form['checkin']
        checkout = request.form['checkout']
        exist_data = hotels.find({"Location": {"$regex": Keyword, "$options": 'i'},"CheckIn":checkin,"CheckOut":checkout}).limit(9)
        exist_datas = list(copy.deepcopy(exist_data))
        list_num = len(exist_datas)
        if list_num > 0:
            print('载入数据')
            # print(exist_data[0])
            return render_template('search2.html', results=exist_datas)

        search_data = Get_booking_hotel(Keyword, checkin, checkout)
        if search_data:
            list_data = search_data.json()['data']['searchQueries']['search']['results']
            for each_data in list_data:
                room_id=each_data['blocks'][0]['blockId']['roomId']
                policyGroupId=each_data['blocks'][0]['blockId']['policyGroupId']
                pagename=each_data['basicPropertyData']['pageName']
                countryCode=each_data['basicPropertyData']['location']['countryCode']
                # print(each_data['location'])
                insert_data = {
                    'Hotel_name': each_data['displayName']['text'],
                    'CheckIn':checkin,
                    'CheckOut':checkout,
                    'Location': each_data['location']['displayLocation'],
                    'Images': 'https://cf.bstatic.com' +
                              each_data['basicPropertyData']['photos']['main']['highResJpegUrl']['relativeUrl'],
                    'score': each_data['basicPropertyData']['reviewScore']['score'],
                    'Price': each_data['blocks'][0]['finalPrice']['amount'],
                    'address': each_data['basicPropertyData']['location'],
                    'Linkss':'https://www.booking.com/hotel/{}/{}.en-gb.html?all_sr_blocks={}_{}_0_2_0;checkin={};checkout={}'.format(countryCode,pagename,room_id,policyGroupId,checkin,checkout),

                }
                print(insert_data)
                hotels.insert_one(insert_data)
        # flash('搜索成功')
        exist_data = hotels.find({"Location": {"$regex": Keyword, "$options": 'i'},"CheckIn":checkin,"CheckOut":checkout}).limit(9)
        exist_datas = list(copy.deepcopy(exist_data))
        print(exist_datas)
        # exist_datas = copy.deepcopy(exist_data)
        return render_template('search2.html', results=exist_datas)
        # jsonify(exist_datas)
    return render_template('search2.html')
@search_api.route('/search_tickets', methods=['POST', 'GET'])  # Search
def search_tickets():
    tickets = mongo_manager.get_collection("Tickets")
    result_list=get_tickets_list('YTO','YMQ','2023-11-27','2023-12-04')
    resultIds = result_list['resultIds']
    for i in range(1, len(resultIds)):
        try:
            each = result_list['results'][resultIds[i]]
            legs = each['legs']
            legs_list = [i['segments'][0] for i in legs]
            fees = each['optionsByFare']
            bookingurl = 'https://www.ca.kayak.com' + fees[0]['options'][0]['url']
            price = fees[0]['options'][0]['fees']['rawPrice']
            result_dict = {
                'depart': 'YTO',
                'arrive': 'YMQ',
                'depart_date': '2023-11-27',
                'return_date': '2023-11-30',
                'price': price,
                'bookingurl': bookingurl,
                'legs_list': legs_list
            }
            print(result_dict)
            tickets.insert_one(result_dict)
        except:pass
if __name__=='__main__':
    search_tickets()