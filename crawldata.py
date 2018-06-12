from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_coin_data():
    url="https://coinmarketcap.com/"
    conn=urlopen(url)
    raw_data=conn.read()
    text=raw_data.decode("UTF8")
    soup=BeautifulSoup(text,"html.parser")
    coins=["bitcoin","ethereum","ripple","bitcoin-cash","eos","litecoin","tron","neo","bitcoin-gold","binance-coin"]
    coin_data = []
    for coin in coins:
        section=soup.find("tr",id="id-{0}".format(coin))
        td_list=section.find_all("td")
        for td in range(len(td_list)):
            if td == 0:
                continue
            elif td == 1:
                image=td_list[td].find('img','logo-sprite')['src']
                a = list(image)
                tail = a[len(a)-3]+a[len(a)-2]+a[len(a)-1]
                if tail != "png":
                    if tail != "jpg":
                        image=td_list[td].find('img','logo-sprite').get('data-src')
                else:
                    image=td_list[td].find('img','logo-sprite').get('src')
                name = td_list[td].find('a','currency-name-container').string
            elif td == 2:
                marketcap = float(td_list[td].string)
            elif td == 3:
                price = td_list[td].a.string
                price = float(price.replace('$',''))
            elif td == 4:
                volume = td_list[td].a.string
                volume = float(volume.replace('$','').replace(',',''))
            elif td == 5:
                supply = td_list[td].a.span.string
                supply = float(supply.replace('$','').replace(',',''))
            elif td == 6:
                change = td_list[td].string
                change = float(change.replace('%','')) #unit of change is percentage (%)
        coin_dict = {
            "name": name,
            'image': image,
            "marketcap": marketcap,
            "price": price,
            "volume": volume,
            "supply": supply,
            "change": change
        }
        coin_data.append(coin_dict)

    return coin_data
