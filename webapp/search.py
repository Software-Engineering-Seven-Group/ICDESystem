from flask import render_template, request, redirect, url_for, Blueprint,flash,jsonify,render_template
from database_manager import user_preference_infor_manager
from database_manager import MongoDBManager, UserInfoCollection, mongo_manager, user_infor_manager, user_preference_infor_manager
import copy
from crawler.Get_Hotel import Get_booking_hotel,get_imageing2
from crawler.Get_Tickets import get_tickets_list,get_imageing,get_tickets_list2
from datetime import datetime, timedelta
from flask_cors import CORS
from crawler.Get_Destination import get_destination_result
import requests

search_api = Blueprint('search_api', __name__)

CORS(search_api)
def get_city_from_ip(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json?lang=en")
        data = response.json()
        city = data.get("city", "Unknown")
        if city == "Unknown":
            city = "Montreal"
        if city =='Montréal':
            city ='Montreal'
        return city

    except Exception as e:
        return "Montreal"
def search_hotel_funtion(Keyword,checkin,checkout):
    hotels = mongo_manager.get_collection("Hotels")
    exist_data = hotels.find(
        {"Location": {"$regex": Keyword.split(' ')[0], "$options": 'i'}, "CheckIn": checkin, "CheckOut": checkout}).limit(6)
    exist_datas = list(copy.deepcopy(exist_data))
    list_num = len(exist_datas)
    if list_num > 0:
        print('Load hotel')
        return  exist_datas
    search_data = Get_booking_hotel(Keyword, checkin, checkout)
    if search_data:
        list_data = search_data.json()['data']['searchQueries']['search']['results']
        for each_data in list_data:
            room_id = each_data['blocks'][0]['blockId']['roomId']
            policyGroupId = each_data['blocks'][0]['blockId']['policyGroupId']
            pagename = each_data['basicPropertyData']['pageName']
            countryCode = each_data['basicPropertyData']['location']['countryCode']
            # print(each_data['location'])
            insert_data = {
                'Hotel_name': each_data['displayName']['text'],
                'CheckIn': checkin,
                'CheckOut': checkout,
                'Location': each_data['location']['displayLocation'],
                'Images': 'https://cf.bstatic.com' +
                          each_data['basicPropertyData']['photos']['main']['highResJpegUrl']['relativeUrl'],
                'score': round(each_data['basicPropertyData']['reviewScore']['score'])/2,
                'Price': each_data['blocks'][0]['finalPrice']['amount'],
                'address': each_data['basicPropertyData']['location'],
                'Linkss': 'https://www.booking.com/hotel/{}/{}.en-gb.html?all_sr_blocks={}_{}_0_2_0;checkin={};checkout={}'.format(
                    countryCode, pagename, room_id, policyGroupId, checkin, checkout),

            }
            print(insert_data)
            hotels.insert_one(insert_data)
    exist_data = hotels.find(
        {"Location": {"$regex": Keyword.split(' ')[0], "$options": 'i'}, "CheckIn": checkin, "CheckOut": checkout}).limit(6)
    exist_datas = list(copy.deepcopy(exist_data))
    print(exist_datas)
    return exist_datas
def search_ticket_function(Departure,Arrive,depart_date,return_date):
    tickets = mongo_manager.get_collection("Tickets")
    exist_data = tickets.find(
        {"Depart_city": {"$regex": Departure, "$options": 'i'}, "Arrive_city": {"$regex": Arrive, "$options": 'i'},
         "depart_date": depart_date, "return_date": return_date}).limit(5)
    exist_datas = list(copy.deepcopy(exist_data))
    list_num = len(exist_datas)
    if list_num > 0:
        print('load ticket')
        # print(exist_data[0])
        return exist_datas
    else:
        print(Departure, Arrive, depart_date, return_date)
        try:
            Departure=get_imageing(Departure)[0]['searchFormPrimary']
            Arrive = get_imageing(Arrive)[0]['searchFormPrimary']
            result_list = get_tickets_list2(Departure, Arrive, depart_date, return_date)
            for result_dict in result_list:
                result_dict['depart'] = Departure
                result_dict['arrive'] = Arrive
                tickets.insert_one(result_dict)
            exist_data = tickets.find(
                {"depart": {"$regex": Departure, "$options": 'i'}, "arrive": {"$regex": Arrive, "$options": 'i'},
                 "depart_date": depart_date, "return_date": return_date}).limit(5)
            exist_datas = list(copy.deepcopy(exist_data))
            print(exist_datas)
            # exist_datas = copy.deepcopy(exist_data)
            return exist_datas
        except:
            return ''
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
            print('Load data')
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
                    'score': round(each_data['basicPropertyData']['reviewScore']['score'])/2,
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
# @search_api.route('/search_tickets', methods=['POST', 'GET'])  # Kayaka Ticket
# def search_tickets():
#     tickets = mongo_manager.get_collection("Tickets")
#
#     if request.method == 'POST':
#         Departure = request.form['Departure']
#         Arrive = request.form['Arrive']
#         depart_date = request.form['Departure_date']
#         return_date = request.form['Return_date']
#
#         exist_data = tickets.find(
#             {"depart": {"$regex": Departure, "$options": 'i'}, "arrive": {"$regex": Arrive, "$options": 'i'},"depart_date": depart_date, "return_date": return_date}).limit(5)
#         exist_datas = list(copy.deepcopy(exist_data))
#         list_num = len(exist_datas)
#         if list_num > 0:
#             print('load data')
#             # print(exist_data[0])
#             return render_template('search_tickets.html', results=exist_datas)
#         else:
#             print(Departure,Arrive,depart_date,return_date)
#             try:
#                 result_list=get_tickets_list(Departure,Arrive,depart_date,return_date)
#                 resultIds = result_list['resultIds']
#                 for i in range(1, len(resultIds)):
#                     try:
#                         each = result_list['results'][resultIds[i]]
#                         legs = each['legs']
#                         legs_list = [i['segments'][0] for i in legs]
#                         fees = each['optionsByFare']
#                         bookingurl = 'https://www.ca.kayak.com' + fees[0]['options'][0]['url']
#                         price = fees[0]['options'][0]['fees']['rawPrice']
#                         result_dict = {
#                             'depart': Departure,
#                             'arrive': Arrive,
#                             'depart_date': depart_date,
#                             'return_date': return_date,
#                             'price': price,
#                             'bookingurl': bookingurl,
#                             'legs_list': legs_list
#                         }
#                         print(result_dict)
#                         tickets.insert_one(result_dict)
#                     except:pass
#                 exist_data = tickets.find(
#                     {"depart": {"$regex": Departure, "$options": 'i'}, "arrive": {"$regex": Arrive, "$options": 'i'},"depart_date": depart_date, "return_date": return_date}).limit(5)
#                 exist_datas = list(copy.deepcopy(exist_data))
#                 print(exist_datas)
#                 # exist_datas = copy.deepcopy(exist_data)
#                 return render_template('search_tickets.html', results=exist_datas)
#             except:
#                 return render_template('search_tickets.html', results='ReCaptcha')
#     return render_template('search_tickets.html')
@search_api.route('/search_tickets', methods=['POST', 'GET'])  # Booking
def search_tickets():
    tickets = mongo_manager.get_collection("Tickets")

    if request.method == 'POST':
        Departure = request.form['Departure']
        Arrive = request.form['Arrive']
        depart_date = request.form['Departure_date']
        return_date = request.form['Return_date']

        exist_data = tickets.find(
            {"depart": {"$regex": Departure, "$options": 'i'}, "arrive": {"$regex": Arrive, "$options": 'i'},"depart_date": depart_date, "return_date": return_date}).limit(5)
        exist_datas = list(copy.deepcopy(exist_data))
        list_num = len(exist_datas)
        if list_num > 0:
            print('load data')
            # print(exist_data[0])
            return render_template('search_tickets.html', results=exist_datas)
        else:
            print(Departure,Arrive,depart_date,return_date)
            try:
                result_list=get_tickets_list2(Departure,Arrive,depart_date,return_date)
                for result_dict in result_list:
                    result_dict['depart']=Departure
                    result_dict['arrive']=Arrive
                    tickets.insert_one(result_dict)
                exist_data = tickets.find(
                    {"depart": {"$regex": Departure, "$options": 'i'}, "arrive": {"$regex": Arrive, "$options": 'i'},"depart_date": depart_date, "return_date": return_date}).limit(5)
                exist_datas = list(copy.deepcopy(exist_data))
                print(exist_datas)
                # exist_datas = copy.deepcopy(exist_data)
                return render_template('search_tickets.html', results=exist_datas)
            except:
                return render_template('search_tickets.html', results='ReCaptcha')
    return render_template('search_tickets.html')
@search_api.route('/search_destination', methods=['POST', 'GET'])
def search_destination():
    Destinations = mongo_manager.get_collection("Destination")
    depart_date = datetime.now().date()+ timedelta(days=3)
    return_date = depart_date + timedelta(days=5)
    client_ip = request.remote_addr
    Departure=get_city_from_ip(client_ip)
    if request.method == 'POST':
        destination=request.form['destination'].split(' ')[0]
        hotel_result=search_hotel_funtion(destination, str(depart_date), str(return_date))
        ticket_result=search_ticket_function(Departure, destination, str(depart_date), str(return_date))
        exist_data = Destinations.find( \
            {"destination": {"$regex": destination, "$options": 'i'}}).limit(5)
        exist_datas = list(copy.deepcopy(exist_data))
        list_num = len(exist_datas)
        trip_info=[Departure,destination,str(depart_date),str(return_date)]
        if list_num > 0:
            print('load destination')
            return_result=(hotel_result,ticket_result,exist_datas,trip_info)
            print(len(ticket_result))
            return render_template('Destination.html', results=return_result)
        else:
            result_list=get_destination_result(destination)
            for result_dict in result_list:
                Destinations.insert_one(result_dict)
            exist_data = Destinations.find( \
                {"destination": {"$regex": destination, "$options": 'i'}}).limit(5)
            exist_datas = list(copy.deepcopy(exist_data))
            print(exist_datas)
            return_result = (hotel_result, ticket_result, exist_datas,trip_info)
            print(len(ticket_result))
            return render_template('Destination.html', results=return_result)

@search_api.route('/autocomplete', methods=['GET'])
def autocomplete():
    query = request.args.get('query')
    option=get_imageing(query)
    return jsonify(option)
@search_api.route('/autocomplete2', methods=['GET'])
def autocomplete2():
    query = request.args.get('query')
    option=get_imageing2(query)
    return jsonify(option)
if __name__=='__main__':
    search_tickets()