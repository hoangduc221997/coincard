from flask import *
from mongoengine import *
from urllib.request import urlopen
from bs4 import BeautifulSoup
from crawldata import get_coin_data
import mlab
from models.user import User

from blogtienao import *

app = Flask(__name__)
app.secret_key = "A secret key"

mlab.connect()




data_craw_from_html = getData()


@app.route('/blogtienao')
def blogtienao():
    data_craw_from_html = getData()
    print(len(data_craw_from_html))
    return render_template('blogtienao.html', data = data_craw_from_html)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']
        fullname = form['fullname']
        yob = form['yob']
        email = form['email']
        gender = form['gender']

        user = User(username=username,
                    password=password,
                    fullname=fullname,
                    yob=yob,
                    email=email,
                    gender=gender)
        user.save()

        return redirect(url_for('login'))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form ['password']

        users = User.objects(username=username, password=password)
        if len(users) == 0:
            return render_template('error.html')
        else:
            session['loggedin'] = True
            return redirect(url_for('mainpage'))


@app.route('/logout')
def logout():
    if "loggedin" in session:
        del session['loggedin']
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


coin_data = get_coin_data()

@app.route('/mainpage')
def mainpage():
    return render_template('mainpage.html')


@app.route('/index_1')
def index_1():
    # coin_data = get_coin_data()
    index_1_am = []
    index_1_duong = []
    for i in coin_data:
        dict = {
            'name':i['name'],
            'change':i['change']
        }
        if i['change'] < 0:
            index_1_am.append(dict)
        elif i['change'] > 0:
            index_1_duong.append(dict)
    return render_template('index_1.html', index_1_am=index_1_am, index_1_duong=index_1_duong)


@app.route('/index_2')
def index_2():
    return render_template('index_2.html', coin_data=coin_data)


@app.route('/index_3')
def index_3():
    return render_template('index_3.html', coin_data=coin_data)


if __name__ == '__main__':
  app.run(debug=True)
