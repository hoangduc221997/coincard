from urllib.request import urlopen
from bs4 import BeautifulSoup

def getData():
    url = "https://blogtienao.com/tien-ao/bitcoin/"
    conn = urlopen(url)
    raw_data = conn.read()
    text = raw_data.decode('utf8')
    soup = BeautifulSoup(text, "html.parser")
    div = soup.find("div", "td-main-content")
    divv = div.find("div", "td-ss-main-content")
    all = divv.findAll("div", "td_module_10")
    data = []
    _dict = {}
    for item in all:
        a = item.find('div','item-details')
        img = item.find('div','td-module-thumb').find('a').find('img').get('src')
        title = a.find('h3','entry-title').string
        sub_title = a.find('div','td-excerpt').string
        _dict['title'] = title
        _dict['sub_title'] = sub_title
        _dict['image'] = img
        data.append(_dict)
    return data
# print(allitems.prettify())
