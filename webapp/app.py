from flask import Flask, render_template, request, redirect, url_for, flash, session
from crawler.Get_Hotel import Get_booking_hotel
from database_manager import MongoDBManager, UserInfoCollection, mongo_manager, user_infor_manager
from app_instance import app
import copy


"“首页，重定向”"
@app.route('/')
def home():
    #return redirect(url_for('register'))

    #todo: data analysis model
    analysed_data = {"America": 14, "China": 10, "India": 20, "France": 50, "England": 6}

    analysed_data_keys = list(analysed_data.keys())
    analysed_data_values = list(analysed_data.values())

    print(analysed_data_values)
    print(analysed_data_keys)

    #return render_template("search.html", data_keys_list=analysed_data_keys, data_values_list=analysed_data_values,
    return render_template("home.html", data_keys_list=analysed_data_keys, data_values_list=analysed_data_values,
                           loginstate='')


"插入信息（注册用户信息）"
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        existing_user = user_infor_manager.find_user_info('username')

        if existing_user is None:
            user_infor_manager.insert_one_user({
                'username': request.form['username'],
                'name': request.form['name'],
                'password': request.form['password'],
                'sex': request.form['sex'],
                'age': request.form['age'],
                'phone': request.form['phone'],
                'email': request.form['email']
            })
            session['username'] = request.form['username']
            return redirect(url_for('login'))

        flash('用户名已经存在，请换一个用户名！')
        return redirect(url_for('register'))

    return render_template('register.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        login_user = user_infor_manager.find_user_info('username')

        if login_user:
            if request.form['password'] == login_user['password']:
                session['username'] = request.form['username']
                return "登陆成功!"

        flash('用户名或密码不正确！')
    return render_template('login.html')

@app.route('/search',methods=['POST', 'GET'])# Search
def search():
    hotels = mongo_manager.get_collection("Hotels")

    if request.method == 'POST':
        Keyword=request.form['Keyword']
        checkin=request.form['checkin']
        checkout=request.form['checkout']
        exist_data=hotels.find({"Location": {"$regex": Keyword}}).limit(10)
        exist_datas=list(copy.deepcopy(exist_data))
        list_num=len(exist_datas)
        if list_num>0:
            print('载入数据')
            # print(exist_data[0])
            return render_template('search.html',results=exist_datas)
        
        search_data=Get_booking_hotel(Keyword,checkin,checkout)
        if search_data:
            list_data=search_data.json()['data']['searchQueries']['search']['results']
            for each_data in list_data:
                insert_data={
                    'Hotel_name':each_data['displayName']['text'],
                    'Location':each_data['location']['displayLocation'],
                    'Images':'https://cf.bstatic.com/'+each_data['basicPropertyData']['photos']['main']['highResJpegUrl']['relativeUrl'],
                    'score':each_data['basicPropertyData']['reviewScore']['score'],
                    'Price':each_data['blocks'][0]['finalPrice']['amount'],
                    'address':each_data['basicPropertyData']['location']
                }
                # print(insert_data)
                hotels.insert_one(insert_data)   
        flash('搜索成功')
        exist_data=hotels.find({"Location": {"$regex": Keyword}}).limit(10)
        exist_datas=list(copy.deepcopy(exist_data))
        return render_template('search.html',results=exist_datas)
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)