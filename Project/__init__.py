from flask import Flask, request, abort
import requests
import json
from Project.Config import *
from forex_python.converter import CurrencyRates 
import math
import locale
app = Flask(__name__)


def GET_BTC_PRICE():
    data = requests.get('http://api.coinlayer.com/api/live?access_key=a7b45c7f695628be717a4bc8d8ba6c85')
    BTC_PRICE = data.text.split('BTC')[1].strip('":,')
    BTC_PRICE_INT = float(BTC_PRICE)
    locale.setlocale(locale.LC_ALL, 'en_US')
    USD = locale.format("%f", BTC_PRICE_INT, grouping=True)
    return USD

def CONVERT_BTC_TO_THB():
    data = requests.get('http://api.coinlayer.com/api/live?access_key=a7b45c7f695628be717a4bc8d8ba6c85')
    BTC_PRICE = data.text.split('BTC')[1].strip('":,')
    BTC_PRICE_INT = float(BTC_PRICE)
    CONVERT = int(BTC_PRICE_INT * 31.26)
    locale.setlocale(locale.LC_ALL, 'en_US')
    THB = locale.format("%f", CONVERT, grouping=True)
    return str(THB)

def GET_BNB_PRICE():
    data = requests.get('http://api.coinlayer.com/api/live?access_key=a7b45c7f695628be717a4bc8d8ba6c85')
    BNB_PRICE = data.text.split('BNB')[1].strip('":')
    sep = ','
    BNB_PRICE = BNB_PRICE.split(sep, 1)[0]
    BNB_PRICE_INT = float(BNB_PRICE)
    locale.setlocale(locale.LC_ALL, 'en_US')
    USD = locale.format("%f", BNB_PRICE_INT, grouping=True)
    return USD

def CONVERT_BNB_TO_THB():
    data = requests.get('http://api.coinlayer.com/api/live?access_key=a7b45c7f695628be717a4bc8d8ba6c85')
    BNB_PRICE = data.text.split('BNB')[1].strip('":')
    sep = ','
    BNB_PRICE = BNB_PRICE.split(sep, 1)[0]
    BNB_PRICE_INT = float(BNB_PRICE)
    CONVERT = int(BNB_PRICE_INT * 31.26)
    locale.setlocale(locale.LC_ALL, 'en_US')
    THB = locale.format("%f", CONVERT, grouping=True)
    return str(THB)

def GET_ADA_PRICE():
    data = requests.get('http://api.coinlayer.com/api/live?access_key=a7b45c7f695628be717a4bc8d8ba6c85')
    ADA_PRICE = data.text.split('ADA')[1].strip('":')
    sep = ','
    ADA_PRICE = ADA_PRICE.split(sep, 1)[0]
    ADA_PRICE_INT = float(ADA_PRICE)
    locale.setlocale(locale.LC_ALL, 'en_US')
    USD = locale.format("%f", ADA_PRICE_INT, grouping=True)
    return USD

def CONVERT_ADA_TO_THB():
    data = requests.get('http://api.coinlayer.com/api/live?access_key=a7b45c7f695628be717a4bc8d8ba6c85')
    ADA_PRICE = data.text.split('ADA')[1].strip('":')
    sep = ','
    ADA_PRICE = ADA_PRICE.split(sep, 1)[0]
    ADA_PRICE_INT = float(ADA_PRICE)
    CONVERT = int(ADA_PRICE_INT * 31.26)
    locale.setlocale(locale.LC_ALL, 'en_US')
    THB = locale.format("%f", CONVERT, grouping=True)
    return str(THB)

def GET_ETH_PRICE():
    data = requests.get('http://api.coinlayer.com/api/live?access_key=a7b45c7f695628be717a4bc8d8ba6c85')
    ETH_PRICE = data.text.split('ETH')[1].strip('":')
    sep = ','
    ETH_PRICE = ETH_PRICE.split(sep, 1)[0]
    ETH_PRICE_INT = float(ETH_PRICE)
    locale.setlocale(locale.LC_ALL, 'en_US')
    USD = locale.format("%f", ETH_PRICE_INT, grouping=True)
    return USD


def CONVERT_ETH_TO_THB():
    data = requests.get('http://api.coinlayer.com/api/live?access_key=a7b45c7f695628be717a4bc8d8ba6c85')
    ETH_PRICE = data.text.split('ETH')[1].strip('":')
    sep = ','
    ETH_PRICE = ETH_PRICE.split(sep, 1)[0]
    ETH_PRICE_INT = float(ETH_PRICE)
    CONVERT = int(ETH_PRICE_INT * 31.26)
    locale.setlocale(locale.LC_ALL, 'en_US')
    THB = locale.format("%f", CONVERT, grouping=True)
    return str(THB)

def GET_DOGE_PRICE():
    data = requests.get('http://api.coinlayer.com/api/live?access_key=a7b45c7f695628be717a4bc8d8ba6c85')
    DOGE_PRICE = data.text.split('DOGE')[1].strip('":')
    sep = ','
    DOGE_PRICE = DOGE_PRICE.split(sep, 1)[0]
    DOGE_PRICE_INT = float(DOGE_PRICE)
    locale.setlocale(locale.LC_ALL, 'en_US')
    USD = locale.format("%f", DOGE_PRICE_INT, grouping=True)
    return USD

def CONVERT_DOGE_TO_THB():
    data = requests.get('http://api.coinlayer.com/api/live?access_key=a7b45c7f695628be717a4bc8d8ba6c85')
    DOGE_PRICE = data.text.split('DOGE')[1].strip('":')
    sep = ','
    DOGE_PRICE = DOGE_PRICE.split(sep, 1)[0]
    DOGE_PRICE_INT = float(DOGE_PRICE)
    CONVERT = int(DOGE_PRICE_INT * 31.26)
    locale.setlocale(locale.LC_ALL, 'en_US')
    THB = locale.format("%f", CONVERT, grouping=True)
    return str(THB)


def GET_USDT_PRICE():
    data = requests.get('http://api.coinlayer.com/api/live?access_key=a7b45c7f695628be717a4bc8d8ba6c85')
    USDT_PRICE = data.text.split('USDT')[1].strip('":')
    sep = ','
    USDT_PRICE = USDT_PRICE.split(sep, 1)[0]
    USDT_PRICE_INT = float(USDT_PRICE)
    locale.setlocale(locale.LC_ALL, 'en_US')
    USD = locale.format("%f", USDT_PRICE_INT, grouping=True)
    return USD

def CONVERT_USDT_TO_THB():
    data = requests.get('http://api.coinlayer.com/api/live?access_key=a7b45c7f695628be717a4bc8d8ba6c85')
    USDT_PRICE = data.text.split('USDT')[1].strip('":')
    sep = ','
    USDT_PRICE = USDT_PRICE.split(sep, 1)[0]
    USDT_PRICE_INT = float(USDT_PRICE)
    CONVERT = int(USDT_PRICE_INT * 31.26)
    locale.setlocale(locale.LC_ALL, 'en_US')
    THB = locale.format("%f", CONVERT, grouping=True)
    return str(THB)

def GET_XRP_PRICE():
    data = requests.get('http://api.coinlayer.com/api/live?access_key=a7b45c7f695628be717a4bc8d8ba6c85')
    XRP_PRICE = data.text.split('XRP')[1].strip('":')
    sep = ','
    XRP_PRICE = XRP_PRICE.split(sep, 1)[0]
    XRP_PRICE_INT = float(XRP_PRICE)
    locale.setlocale(locale.LC_ALL, 'en_US')
    USD = locale.format("%f", XRP_PRICE_INT, grouping=True)
    return USD

def CONVERT_XRP_TO_THB():
    data = requests.get('http://api.coinlayer.com/api/live?access_key=a7b45c7f695628be717a4bc8d8ba6c85')
    XRP_PRICE = data.text.split('XRP')[1].strip('":')
    sep = ','
    XRP_PRICE = XRP_PRICE.split(sep, 1)[0]
    XRP_PRICE_INT = float(XRP_PRICE)
    CONVERT = int(XRP_PRICE_INT * 31.26)
    locale.setlocale(locale.LC_ALL, 'en_US')
    THB = locale.format("%f", CONVERT, grouping=True)
    return str(THB)

@app.route('/webhook', methods=['POST','GET'])
def webhook():
    
    if request.method == 'POST':
        payload = request.json
       
        Reply_token = payload['events'][0]['replyToken']
        print(Reply_token)
        message = payload['events'][0]['message']['text']
        print(message)
        if "btc" in message :
            Reply_messasge = 'ราคา BITCOIN ขณะนี้ \n{}'.format(GET_BTC_PRICE()) + ' USD\n' + format(CONVERT_BTC_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "BTC" in message :
            Reply_messasge = 'ราคา BITCOIN ขณะนี้ \n{}'.format(GET_BTC_PRICE()) + ' USD\n' + format(CONVERT_BTC_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "Btc" in message :
            Reply_messasge = 'ราคา BITCOIN ขณะนี้ \n{}'.format(GET_BTC_PRICE()) + ' USD\n' + format(CONVERT_BTC_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "Bitcoin" in message :
            Reply_messasge = 'ราคา BITCOIN ขณะนี้ \n{}'.format(GET_BTC_PRICE()) + ' USD\n' + format(CONVERT_BTC_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "บิทคอยน์" in message :
            Reply_messasge = 'ราคา BITCOIN ขณะนี้ \n{}'.format(GET_BTC_PRICE()) + ' USD\n' + format(CONVERT_BTC_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "bnb" in message :
            Reply_messasge = 'ราคา BINANCE ขณะนี้ \n{}'.format(GET_BNB_PRICE()) + ' USD\n' + format(CONVERT_BNB_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        
        if "Bnb" in message :
            Reply_messasge = 'ราคา BINANCE ขณะนี้ \n{}'.format(GET_BNB_PRICE()) + ' USD\n' + format(CONVERT_BNB_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "BNB" in message :
            Reply_messasge = 'ราคา BINANCE ขณะนี้ \n{}'.format(GET_BNB_PRICE()) + ' USD\n' + format(CONVERT_BNB_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)


        if "Binance" in message :
            Reply_messasge = 'ราคา BINANCE ขณะนี้ \n{}'.format(GET_BNB_PRICE()) + ' USD\n' + format(CONVERT_BNB_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "ไบแนนซ์" in message :
            Reply_messasge = 'ราคา BINANCE ขณะนี้ \n{}'.format(GET_BNB_PRICE()) + ' USD\n' + format(CONVERT_BNB_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "ada" in message :
            Reply_messasge = 'ราคา ADA ขณะนี้ \n{}'.format(GET_ADA_PRICE()) + ' USD\n' + format(CONVERT_ADA_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "Ada" in message :
            Reply_messasge = 'ราคา ADA ขณะนี้ \n{}'.format(GET_ADA_PRICE()) + ' USD\n' + format(CONVERT_ADA_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "ADA" in message :
            Reply_messasge = 'ราคา ADA ขณะนี้ \n{}'.format(GET_ADA_PRICE()) + ' USD\n' + format(CONVERT_ADA_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        
        if "เอด้า" in message :
            Reply_messasge = 'ราคา ADA ขณะนี้ \n{}'.format(GET_ADA_PRICE()) + ' USD\n' + format(CONVERT_ADA_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "eth" in message :
            Reply_messasge = 'ราคา Ethereum ขณะนี้ \n{}'.format(GET_ETH_PRICE()) + ' USD\n' + format(CONVERT_ETH_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "Eth" in message :
            Reply_messasge = 'ราคา Ethereum ขณะนี้ \n{}'.format(GET_ETH_PRICE()) + ' USD\n' + format(CONVERT_ETH_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "ETH" in message :
            Reply_messasge = 'ราคา Ethereum ขณะนี้ \n{}'.format(GET_ETH_PRICE()) + ' USD\n' + format(CONVERT_ETH_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "อีเทอเลียม" in message :
            Reply_messasge = 'ราคา Ethereum ขณะนี้ \n{}'.format(GET_ETH_PRICE()) + ' USD\n' + format(CONVERT_ETH_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        
        if "Ethereum" in message :
            Reply_messasge = 'ราคา Ethereum ขณะนี้ \n{}'.format(GET_ETH_PRICE()) + ' USD\n' + format(CONVERT_ETH_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "DOGE" in message :
            Reply_messasge = 'ราคา DOGECOIN ขณะนี้ \n{}'.format(GET_DOGE_PRICE()) + ' USD\n' + format(CONVERT_DOGE_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "doge" in message :
            Reply_messasge = 'ราคา DOGECOIN ขณะนี้ \n{}'.format(GET_DOGE_PRICE()) + ' USD\n' + format(CONVERT_DOGE_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "Doge" in message :
            Reply_messasge = 'ราคา DOGECOIN ขณะนี้ \n{}'.format(GET_DOGE_PRICE()) + ' USD\n' + format(CONVERT_DOGE_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "DOG" in message :
            Reply_messasge = 'ราคา DOGECOIN ขณะนี้ \n{}'.format(GET_DOGE_PRICE()) + ' USD\n' + format(CONVERT_DOGE_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "Dog" in message :
            Reply_messasge = 'ราคา DOGECOIN ขณะนี้ \n{}'.format(GET_DOGE_PRICE()) + ' USD\n' + format(CONVERT_DOGE_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "dog" in message :
            Reply_messasge = 'ราคา DOGECOIN ขณะนี้ \n{}'.format(GET_DOGE_PRICE()) + ' USD\n' + format(CONVERT_DOGE_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
      
        if "dogecoin" in message :
            Reply_messasge = 'ราคา DOGECOIN ขณะนี้ \n{}'.format(GET_DOGE_PRICE()) + ' USD\n' + format(CONVERT_DOGE_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "Dogecoin" in message :
            Reply_messasge = 'ราคา DOGECOIN ขณะนี้ \n{}'.format(GET_DOGE_PRICE()) + ' USD\n' + format(CONVERT_DOGE_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        
        if "DOGECOIN" in message :
            Reply_messasge = 'ราคา DOGECOIN ขณะนี้ \n{}'.format(GET_DOGE_PRICE()) + ' USD\n' + format(CONVERT_DOGE_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "ด็อกคอยส์" in message :
            Reply_messasge = 'ราคา DOGECOIN ขณะนี้ \n{}'.format(GET_DOGE_PRICE()) + ' USD\n' + format(CONVERT_DOGE_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "USDT" in message :
            Reply_messasge = 'ราคา TetherUS ขณะนี้ \n{}'.format(GET_USDT_PRICE()) + ' USD\n' + format(CONVERT_USDT_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "Usdt" in message :
            Reply_messasge = 'ราคา TetherUS ขณะนี้ \n{}'.format(GET_USDT_PRICE()) + ' USD\n' + format(CONVERT_USDT_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "usdt" in message :
            Reply_messasge = 'ราคา TetherUS ขณะนี้ \n{}'.format(GET_USDT_PRICE()) + ' USD\n' + format(CONVERT_USDT_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "Tether" in message :
            Reply_messasge = 'ราคา TetherUS ขณะนี้ \n{}'.format(GET_USDT_PRICE()) + ' USD\n' + format(CONVERT_USDT_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "tether" in message :
            Reply_messasge = 'ราคา TetherUS ขณะนี้ \n{}'.format(GET_USDT_PRICE()) + ' USD\n' + format(CONVERT_USDT_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "เทเทอร์" in message :
            Reply_messasge = 'ราคา TetherUS ขณะนี้ \n{}'.format(GET_USDT_PRICE()) + ' USD\n' + format(CONVERT_USDT_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "XRP" in message :
            Reply_messasge = 'ราคา Ripple ขณะนี้ \n{}'.format(GET_XRP_PRICE()) + ' USD\n' + format(CONVERT_XRP_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "Xrp" in message :
            Reply_messasge = 'ราคา Ripple ขณะนี้ \n{}'.format(GET_XRP_PRICE()) + ' USD\n' + format(CONVERT_XRP_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "xrp" in message :
            Reply_messasge = 'ราคา Ripple ขณะนี้ \n{}'.format(GET_XRP_PRICE()) + ' USD\n' + format(CONVERT_XRP_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "Ripple" in message :
            Reply_messasge = 'ราคา Ripple ขณะนี้ \n{}'.format(GET_XRP_PRICE()) + ' USD\n' + format(CONVERT_XRP_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        if "ripple" in message :
            Reply_messasge = 'ราคา Ripple ขณะนี้ \n{}'.format(GET_XRP_PRICE()) + ' USD\n' + format(CONVERT_XRP_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        
        if "ริปเปิ้ล" in message :
            Reply_messasge = 'ราคา Ripple ขณะนี้ \n{}'.format(GET_XRP_PRICE()) + ' USD\n' + format(CONVERT_XRP_TO_THB()) + ' THB' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif not "ช่วยเหลือ" in message:
            Reply_messasge = 'กรุณาพิมพ์คำสั่งให้ถูกต้อง' 
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

     

        return request.json, 200

    elif request.method == 'GET' :

        return 'this is method GET!!!' , 200

    else:
        abort(400)

@app.route('/')
def hello():
    return 'hello world book',200

def ReplyMessage(Reply_token, TextMessage, Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Line_Acees_Token) ##ที่ยาวๆ
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }

    data = {
        "replyToken":Reply_token,
        "messages":[{
            "type":"text",
            "text":TextMessage
        }]
    }

    data = json.dumps(data) ## dump dict >> Json Object
    r = requests.post(LINE_API, headers=headers, data=data) 
    return 200