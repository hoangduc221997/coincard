from urllib.request import urlopen
from bs4 import BeautifulSoup

def getData():
    url = "https://blogtienao.com/tien-ao/bitcoin/"
    conn = urlopen(url)
    raw_data = conn.read()
    text = raw_data.decode('utf8')
    soup = BeautifulSoup(text, "html.parser")
    # div = soup.find_all('div', 'item-details')
    # print(div[0])
    # five_div =
    # for i in div:
    #     print(i.h3.string)
    #     dict = {
    #         'title': i.h3.string,
    #         'content':
    #     }
    # h3_title = div[0:5]
    # five_post_title = []
    # for i in h3_title:
    #
    #     five_post_title.append(i.string)
    # print(five_post_title)


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
        _dict = {
            'link': a.a['href'],
            'title': title,
            'sub_title': sub_title,
            'image': img
            }
        data.append(_dict)
    return data
# getData()
