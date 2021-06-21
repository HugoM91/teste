import os
#from os.path import join, dirname
#from dotenv import load_dotenv
from binance.client import Client
from keys import BINANCE_API, BINANCE_KEY

#env_path = join(dirname(dirname(__file__)),'.env') # ../.env
#env_path = join(dirname(__file__),'.env')  # /.env
#load_dotenv(dotenv_path=env_path)

api_key = os.getenv(BINANCE_KEY)
api_sekret = os.getenv(BINANCE_API)

client = Client(api_key, api_sekret)

simbolos = ['BNBBTC','ETHBTC', 'XRPBTC' , 'XMRBTC' , 'LTCBTC' , 'EOSBTC', 'TRXBTC', 'NEOBTC', 'IOTABTC', 'ZECBTC', 'DASHBTC' ,'DOGEBTC', 'ENJBTC','XLMBTC' ,'BATBTC','ONTBTC', 'LINKBTC', 'WAVESBTC' ,'THETABTC' ,'XLMBTC','MANABTC' ,'QTUMBTC' ,'NANOBTC' ,'ETCBTC','CAKEBTC', 'XEMBTC', 'CTSIBTC', 'ANKRBTC', 'AVABTC', 'DATABTC' ,'GOBTC' ,'CVCBTC' ,'ATOMBTC', 'UNIBTC', 'AAVEBTC', 'ALGOBTC',  'HOTBTC', 'SCBTC']

url_padroes = 'https://discord.com/api/webhooks/855340915442188298/4tHOf9mHHbFN0hmn-7swlOjoPM-6EUbR7JlQLNvFzK-eTgHgS4laUG5e3XNzIpIQ3zcG'
url_marketOrders = 'https://discord.com/api/webhooks/853186644928626718/dM0WLJS430HVWs-jFhstwLYO4ADiv9cYT68O_OzrTnwJDaavNkL5_FTaCkrXomNz-XPW'
url_misc = 'https://discord.com/api/webhooks/855340676321509406/SBsBfcJTdqirJv2FB3PsIYQUAHfh6-plSLyAp5SWcwvas0J1m4DuWrXLa3-QLFR7nFmi'


if __name__ == '__main__':
    info = client.get_account_status()
    print(info)
