from flask import *
from mongoengine import *
from urllib.request import urlopen
from bs4 import BeautifulSoup
from crawldata import get_coin_data
import mlab
from models.user import User

app = Flask(__name__)
app.secret_key = "A secret key"

mlab.connect()


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

@app.route('/mainpage')
def mainpage():
    coin_data = get_coin_data()
    return render_template('mainpage.html', coin_data=coin_data)


if __name__ == '__main__':
  app.run(debug=True)
