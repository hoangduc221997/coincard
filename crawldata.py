import pyexcel
from urllib.request import urlopen
from bs4 import BeautifulSoup
url="https://coinmarketcap.com/"
conn=urlopen(url)
raw_data=conn.read()
text=raw_data.decode("UTF8")
soup=BeautifulSoup(text,"html.parser")
coins=["bitcoin","ethereum","ripple"]
# for coin in coins:
section=soup.find("tr",id="id-bitcoin")
td_list=section.find_all("td")
for td in range(len(td_list)):
    if 0 <= td <= 1:
        continue
    elif td == 2:
        marketcap = td_list[td].string
        print(float(marketcap))
    elif td == 3:
        market = td_list[td].a.string
        marketcap = market.replace('$','')
        print(float(marketcap))
    elif td == 4:
        market = td_list[td].a.string
        marketcap = market.replace('$','').replace(',','')
        print(float(marketcap))
    elif td == 5:
        marketcap = td_list[td].a.span.string
        print(marketcap)
    elif td == 6:
        marketcap = td_list[td].string
        print(marketcap)
    # pyexcel.save_as(records=itune_list,dest_file_name="Itunetopsong.xlsx")
    # options = {
    #     'default_search': 'ytsearch',
    #     'max_downloads': 1
    # }
