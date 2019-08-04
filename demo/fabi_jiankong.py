# coding:utf-8
"""
文件的作用：法币报价python监控脚本
"""
import json
from urllib.request import Request, urlopen
import time
import pandas as pd

# coinID
btc = '1'
eth = '3'
usdt = '2'
# tradeType
buy = '1'
sell = '0'


def getPrice(coinID, tradeType):
    huobiapi = "https://api-otc.huobi.pro/v1/otc/trade/list/public"
    api_url = huobiapi + "?coinId=" + coinID + "&tradeType=" + tradeType + "&currentPage=1&payWay=&country=&merchant=1&online=1&range=0"
    firefox_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    request = Request( api_url, headers=firefox_headers )
    html = urlopen( request )
    data = html.read().decode( 'utf-8' )
    dataJson = json.loads( data )
    price = dataJson['data'][0]['price']
    # print(price)
    return price


def getAllPrice(showprice=0):
    btc_buy = getPrice( coinID=btc, tradeType=buy )
    btc_sell = getPrice( coinID=btc, tradeType=sell )

    eth_buy = getPrice( coinID=eth, tradeType=buy )
    eth_sell = getPrice( coinID=eth, tradeType=sell )

    usdt_buy = getPrice( coinID=usdt, tradeType=buy )
    usdt_sell = getPrice( coinID=usdt, tradeType=sell )

    prices = {
        "btc": {
            "buy": btc_buy,
            "sell": btc_sell
        },
        "eth": {
            "buy": eth_buy,
            "sell": eth_sell
        },
        "usdt": {
            "buy": usdt_buy,
            "sell": usdt_sell
        }
    }
    prices_df = pd.DataFrame( prices )
    if showprice:
        print( prices_df )
    return prices_df

def getChajia(prices,showChajia = 0):
    cj = prices.iloc[0]-prices.iloc[1]
    if showChajia:
        print('差价:')
        print(cj)
    return cj


num = 0
r = 0

while(1):
    t = time.strftime( '%H:%M:%S', time.localtime( time.time() ) )
    print( t,r )

    try:
        prices = getAllPrice( showprice=1 )
        cj = getChajia( prices=prices, showChajia=1 )

        if (cj['btc'] < 0 or cj['eth'] < 0 or cj['usdt'] < 0):
            num = num + 1
        print( u"第",num,u"次发现价差")

    except:
        pass
    r = r+1

    time.sleep( 3 )