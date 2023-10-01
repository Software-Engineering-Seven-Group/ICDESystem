from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/user_data"
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
            users.insert({
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

if __name__ == '__main__':
    app.run(debug=True)