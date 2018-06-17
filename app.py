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
# <<<<<<< HEAD
#
# # for i in data_craw_from_html:
# #     print(i)
# =======
# data_craw_from_html = getData()
# # for items in data_craw_from_html:
# #     print(items)
# >>>>>>> 729b249bd47c3d4f918d13fc7f83a19544e90d06

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
        index_1 = i['change']
        dict = {
            'name':i['name'],
            'change':i['change'],
            'index_1': index_1,
            'image': i['image']
        }
        if index_1 < 0:
            index_1_am.append(dict)
        elif index_1 >= 0:
            index_1_duong.append(dict)
    return render_template('index_1.html', index_1_am=index_1_am, index_1_duong=index_1_duong)


@app.route('/index_2')
def index_2():
    index_2_buy = []
    index_2_sell = []
    index_2_list =[]
    for i in coin_data:
        index_2 = i['volume'] / i['marketcap']
        index_2 = round(index_2, 2)
        dict = {
            'name':i['name'],
            'volume':i['volume'],
            'marketcap':i['marketcap'],
            'index_2': index_2,
            'image': i['image']
        }
        index_2_list.append(dict)
        if index_2 < 0.03:
            index_2_buy.append(dict)
        elif index_2 >= 0.03:
            index_2_sell.append(dict)

    return render_template('index_2.html', index_2_buy=index_2_buy, index_2_sell=index_2_sell)


@app.route('/index_3')
def index_3():
    index_3_list = []
    for i in coin_data:
        index_3 = (i['volume'] / i['price']) / i['supply']
        index_3 = round(index_3, 5)
        dict = {
            'name': i['name'],
            'volume': i['volume'],
            'marketcap': i['marketcap'],
            'index_3': index_3,
            'image': i['image']
        }
        index_3_list.append(dict)
        buy_index_3_list = sorted(index_3_list, key=lambda i: i['index_3'])
        sell_index_3_list = sorted(index_3_list, key=lambda i: i['index_3'], reverse=True)


    return render_template('index_3.html', buy_index_3_list=buy_index_3_list, sell_index_3_list=sell_index_3_list)


@app.route('/list_coin')
def list_coin():
    coins=["bitcoin","ethereum","ripple","bitcoin-cash","eos","litecoin","tron","neo","bitcoin-gold","binance-coin"]
    return render_template('list_coin.html', coins=coins)


@app.route('/detail_coin/<coin>')
def detail_coin(coin):
    coins=["bitcoin","ethereum","ripple","bitcoin-cash","eos","litecoin","tron","neo","bitcoin-gold","binance-coin"]
    index_3_list = []

    if coin in coins:
        coin_detail = coin_data[coins.index(coin)]
        index_1 = coin_detail['change']
        index_2 = coin_detail['volume'] / coin_detail['marketcap']
        index_2 = round(index_2, 2)
        index_3 = (coin_detail['volume'] / coin_detail['price']) / coin_detail['supply']
        index_3 = round(index_3, 5)

    for coin in coins:
        coin_details = coin_data[coins.index(coin)]
        index_33 = (coin_details['volume'] / coin_details['price']) / coin_details['supply']
        index_33 = round(index_33, 3)
        index_3_list.append(index_33)
        average_list = sum(index_3_list) / len(index_3_list)
    #     sort_index_3_list = index_3_list.sort()
    # print(index_3_list)
    return render_template('detail_coin.html',  coin_detail=coin_detail,
                                                index_1=index_1,
                                                index_2=index_2,
                                                index_3=index_3,
                                                index_3_list = index_3_list,
                                                average_list = average_list)

if __name__ == '__main__':
  app.run(debug=True)
