from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_pymongo import PyMongo
from crawler.Get_Hotel import Get_booking_hotel
import copy
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Tripedia"
app.secret_key = "mysecretkey"
mongo = PyMongo(app)

"“首页，重定向”"
@app.route('/')
def home():
    return redirect(url_for('register'))
"插入信息（注册用户信息）"
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.userInfo
        existing_user = users.find_one({'username': request.form['username']})

        if existing_user is None:
            users.insert_one({
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
        users = mongo.db.userInfo
        login_user = users.find_one({'username': request.form['username']})

        if login_user:
            if request.form['password'] == login_user['password']:
                session['username'] = request.form['username']
                return "登陆成功!"

        flash('用户名或密码不正确！')
    return render_template('login.html')

@app.route('/search',methods=['POST', 'GET'])# Search
def search():
    hotels=mongo.db.Hotels
    
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