from flask import Flask, render_template, request
import pymongo


g_debug_flag = True
host_id = '127.0.0.1'
port_id = 2023

#1. create the database
database_client = pymongo.MongoClient("mongodb://localhost:27017/")
database_instance = database_client["runoobdb"]
db_list = database_client.list_database_names()
if "runoobdb" in db_list:
    print("data base has existed")

collection = database_instance["sites"]
collection_list = database_instance.list_collection_names()
if "sites" in collection_list:
    print("collection has existed")

#database insert operation
test_user_infor = {"name" : "alex", "pwd" : "123"}
collection.insert_one(test_user_infor)

#2. flask back-end logic
app = Flask(__name__)

#home page
@app.route('/')
def index():
    msg = '' #"software engineering projection"
    return render_template("home.html", data = msg)

#infor page2
@app.route('/page1')
def page1():
    msg = "the page1 content"
    return render_template("page1.html", data=msg)

#infor page1
@app.route('/page2')
def page2():
    msg = "the page2 content"
    return render_template("page2.html", data = msg)

# login page
@app.route('/login')
def page_login():
    return render_template("login.html")

# login function
@app.route('/login_function', methods = ['POST'])
def login_function():
    if request.method == 'POST':
        user_name = request.form['name']
        user_pwd = request.form['pwd']

        #database finding operation
        query = {"name": user_name}
        doc = collection.find(query)
        user_info = None
        for x in doc:
            user_info = x
            print(x)

        #check the user data by mongodb
        if user_info != None and user_pwd == user_info['pwd']:
            print(user_name, ' login success')
            return render_template('home.html', data = user_name)
        else:
            return render_template('login.html', data = 'wrong user pwd')


if __name__ == '__main__':
    app.run(debug = g_debug_flag, host = host_id, port = port_id)
