from binance.client import Client
import time
from discord_webhook import DiscordWebhook
import numpy as np
from main import client, simbolos,url_padroes ,url_marketOrders ,url_misc

trade_id=[]


def set_key(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    elif type(dictionary[key]) == list:
        dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]


def mensagem_compra_venda(buyermaker, symbol, quantity_usd, quantity):
    if buyermaker == True:
        webhook = DiscordWebhook(url_marketOrders , content= (':red_circle: ' + '------Sell------  ' + symbol + '\n' + quantity_usd + ' USD' + ' / ' + quantity + ' Coins'))
    if buyermaker == False:
        webhook = DiscordWebhook(url_marketOrders , content= (':green_circle: ' + '------Buy------  ' + symbol + '\n' + quantity_usd + ' USD' + ' / ' + quantity + ' Coins'))
    response = webhook.execute()

def start_qnt(sym):

    simbolos1 =  ['BNBBTC','ETHBTC', 'XRPBTC' , 'XMRBTC' , 'LTCBTC' , 'EOSBTC', 'TRXBTC', 'NEOBTC', 'IOTABTC', 'ZECBTC', 'DASHBTC' ,'DOGEBTC']
    simbolos2 = ['ENJBTC','XLMBTC' ,'BATBTC','ONTBTC', 'LINKBTC', 'WAVESBTC' ,'THETABTC' ,'XLMBTC','MANABTC' ,'QTUMBTC' ,'NANOBTC' ,'ETCBTC','CAKEBTC', 'XEMBTC']
    simbolos3 = ['CTSIBTC', 'ANKRBTC', 'AVABTC', 'DATABTC' ,'GOBTC' ,'CVCBTC' ,'ATOMBTC', 'UNIBTC', 'AAVEBTC', 'ALGOBTC',  'HOTBTC', 'SCBTC'] 
    
    trades2 = client.get_recent_trades(symbol='BTCUSDT')
    btc_price = 0
    for x in trades2[-1:]:
        btc_price = float(x['price'])

    trades = client.get_recent_trades(symbol=sym)
    for x in trades:
        if x['id'] not in trade_id:
            q = float(x['qty'])
            d = x['isBuyerMaker']
            p = float(x['price'])
            pd = q * p
            q1 = float("{:.3f}".format(q))
            q1 = str(q1)
            pd3 = str(float("{:.3f}".format(pd)))
            pd4 = btc_price * pd

            if sym == 'BTCUSDT' and pd >= 250000:
                mensagem_compra_venda(d, sym, pd3, q1)
                trade_id.append(x['id'])
            elif sym in simbolos1 and pd4 >= 150000:
                mensagem_compra_venda(d, sym, pd3, q1)
                trade_id.append(x['id'])
            elif sym in simbolos2 and pd4 >= 100000:
                mensagem_compra_venda(d, sym, pd3, q1)
                trade_id.append(x['id'])
            elif sym in simbolos3 and pd4 >= 50000:
                mensagem_compra_venda(d, sym, pd3, q1)
                trade_id.append(x['id'])


def start_var(sym):
    candles = client.get_klines(symbol=sym, interval=Client.KLINE_INTERVAL_1MINUTE, limit = 10)

    op = []
    hi = []
    lo = []
    cl = []
    vo = []

    for x in candles:
        op.append(float(x[1]))
        hi.append(float(x[2]))
        lo.append(float(x[3]))
        cl.append(float(x[4]))
        vo.append(float(x[5]))
#---------------------------
    op_dif = (op[-1] * 100 / op[-5]) - 100

    if op[-1] < cl[-1] and op[-2] < cl[-2] and op[-3] < cl[-3] and op[-4] < cl[-4] and op[-5] < cl[-5] and op_dif > 0.35:
        webhook = DiscordWebhook(url_padroes , content= (':green_circle:' + ' Five White Soldiers - 1 minute // ' + sym))
        response = webhook.execute()
    if op[-1] > cl[-1] and op[-2] > cl[-2] and op[-3] > cl[-3] and op[-4] > cl[-4] and op[-5] > cl[-5] and op_dif > 0.35:
        webhook = DiscordWebhook(url_padroes , content= (':red_circle:' + ' Five Black Crows - 1 minute // ' + sym))
        response = webhook.execute()

#------------------------
    if op[-1] < cl[-2]:
        if vo[-1] > ((sum(vo)/len(vo)) * 6):
            webhook = DiscordWebhook(url_misc , content= (':red_circle:' + ' High Volume // ' + sym))
            response = webhook.execute()
    if op[-1]  > cl[-2]:
        if vo[-1] > ((sum(vo)/len(vo)) * 6):
            webhook = DiscordWebhook(url_misc , content= (':green_circle:' + ' High Volume // ' + sym))
            response = webhook.execute()

#---------------------------
    open1 = float(op[-3])
    open2 = float(op[-1])
    dif_open = float((open2 * 100 / open1) - 100)
    dif_open2 = float("{:.3f}".format(dif_open))

    if dif_open > 3.5:
        dif_open3 = str(dif_open2)
        webhook = DiscordWebhook(url_misc , content= (':green_circle: ' + sym + '//' + dif_open3 + '%' + ' Up'))
        response = webhook.execute()
    if dif_open < -3.5:
        dif_open3 = str(dif_open2)
        webhook = DiscordWebhook(url_misc , content= (':red_circle: ' + sym + '//' + dif_open3 + '%' + ' Down'))
        response = webhook.execute()


while True:
    for x in simbolos:
        start_qnt(x)
        start_var(x)
        time.sleep(2)

    if len(trade_id) > 20000:
        del trade_id[:10000]