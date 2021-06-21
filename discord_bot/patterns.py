from binance.client import Client
from discord_webhook import DiscordWebhook
import numpy as np
import time

from main import client
from utils import talib_pattern


# Implement all patterns
class Patterns():

    def __init__(self, binance_options, **kwargs):
        self.discord_webhook = kwargs['discord_webhook']
        self.discord_sleep = kwargs['discord_sleep']
        self.patterns = kwargs['patterns']

        self.client = binance_options['client']
        self.limit = binance_options['limit']
        self.symbols = binance_options['symbols']
        self.interval = binance_options['interval'].lower()


    def start(self):
        print("🚀 Starting ... 💰")
        for sym in self.symbols:
            candles = client.get_klines(symbol=sym, interval=self.interval, limit=self.limit)

            # candle: [1624190400000, '0.00936400', '0.00939200', '0.00928300', '0.00934100', '15934.56000000', 1624193999999, '148.61589299', 7071, '8633.40000000', '80.51476709', '0']
            # Candle example:
            # [
            #     [
            #         1499040000000,      // Open time
            #         "0.01634790",       // Open
            #         "0.80000000",       // High
            #         "0.01575800",       // Low
            #         "0.01577100",       // Close
            #         "148976.11427815",  // Volume
            #         1499644799999,      // Close time
            #         "2434.19055334",    // Quote asset volume
            #         308,                // Number of trades
            #         "1756.87402397",    // Taker buy base asset volume
            #         "28.46694368",      // Taker buy quote asset volume
            #         "17928899.62484339" // Ignore.
            #     ]
            # ]

            ohlcv = [candle[1:6] for candle in candles]
            patterns = talib_pattern(self.patterns, ohlcv)

            for k, v in patterns.items():
                if any([x == 100 for x in v]):
                    content = f":green_circle: {sym} at **{self.interval}** - Pattern **{k.title()}**" #+ "\n\t{v}\n"

                if any([x == -100 for x in v]):
                    content = f":red_circle: {sym} at **{self.interval}** - Pattern **{k.title()}**" #+ "\n\t{v}\n"

                webhook = DiscordWebhook(market_orders_webhook, content=content)
                response = webhook.execute()
                time.sleep(self.discord_sleep)


if __name__ == '__main__':

    patterns_webhook = 'https://discord.com/api/webhooks/855340915442188298/4tHOf9mHHbFN0hmn-7swlOjoPM-6EUbR7JlQLNvFzK-eTgHgS4laUG5e3XNzIpIQ3zcG'
    market_orders_webhook = 'https://discord.com/api/webhooks/853186644928626718/dM0WLJS430HVWs-jFhstwLYO4ADiv9cYT68O_OzrTnwJDaavNkL5_FTaCkrXomNz-XPW'

    symbols = ['BTCUSDT', 'ETHBTC', 'LTCBTC', 'BNBBTC', 'NEOBTC', 'BCCBTC', 'GASBTC', 'HSRBTC', 'MCOBTC', 'WTCBTC', 'LRCBTC', 'QTUMBTC', 'YOYOBTC', 'OMGBTC', 'ZRXBTC', 'STRATBTC', 'SNGLSBTC', 'BQXBTC', 'KNCBTC', 'FUNBTC', 'SNMBTC', 'IOTABTC', 'LINKBTC', 'XVGBTC', 'SALTBTC', 'MDABTC', 'MTLBTC', 'SUBBTC', 'EOSBTC', 'SNTBTC', 'ETCBTC', 'MTHBTC', 'ENGBTC', 'DNTBTC', 'ZECBTC', 'BNTBTC', 'ASTBTC', 'DASHBTC', 'OAXBTC', 'ICNBTC', 'BTGBTC', 'EVXBTC', 'REQBTC', 'VIBBTC', 'TRXBTC', 'POWRBTC', 'ARKBTC', 'XRPBTC', 'MODBTC', 'ENJBTC', 'STORJBTC', 'VENBTC', 'KMDBTC', 'RCNBTC', 'NULSBTC', 'RDNBTC', 'XMRBTC', 'DLTBTC', 'AMBBTC', 'BATBTC', 'BCPTBTC', 'ARNBTC', 'GVTBTC', 'CDTBTC', 'GXSBTC', 'POEBTC', 'QSPBTC', 'BTSBTC', 'XZCBTC', 'LSKBTC', 'TNTBTC', 'FUELBTC', 'MANABTC', 'BCDBTC', 'DGDBTC', 'ADXBTC', 'ADABTC', 'PPTBTC', 'CMTBTC', 'XLMBTC', 'CNDBTC', 'LENDBTC', 'WABIBTC', 'TNBBTC', 'WAVESBTC', 'GTOBTC', 'ICXBTC', 'OSTBTC', 'ELFBTC', 'AIONBTC', 'NEBLBTC', 'BRDBTC', 'EDOBTC', 'WINGSBTC', 'NAVBTC', 'LUNBTC', 'TRIGBTC', 'APPCBTC', 'VIBEBTC', 'RLCBTC', 'INSBTC', 'PIVXBTC', 'IOSTBTC', 'CHATBTC', 'STEEMBTC', 'NANOBTC', 'VIABTC', 'BLZBTC', 'AEBTC', 'RPXBTC', 'NCASHBTC', 'POABTC', 'ZILBTC', 'ONTBTC', 'STORMBTC', 'XEMBTC', 'WANBTC', 'WPRBTC', 'QLCBTC', 'SYSBTC', 'GRSBTC', 'CLOAKBTC', 'GNTBTC', 'LOOMBTC', 'BCNBTC', 'REPBTC', 'TUSDBTC', 'ZENBTC', 'SKYBTC', 'CVCBTC', 'THETABTC', 'IOTXBTC', 'QKCBTC', 'AGIBTC', 'NXSBTC', 'DATABTC', 'SCBTC', 'NPXSBTC', 'KEYBTC', 'NASBTC', 'MFTBTC', 'DENTBTC', 'ARDRBTC', 'HOTBTC', 'VETBTC', 'DOCKBTC', 'POLYBTC', 'PHXBTC', 'HCBTC', 'GOBTC', 'PAXBTC', 'RVNBTC', 'DCRBTC', 'MITHBTC', 'BCHABCBTC', 'BCHSVBTC', 'RENBTC', 'BTTBTC', 'ONGBTC', 'FETBTC', 'CELRBTC', 'MATICBTC', 'ATOMBTC', 'PHBBTC', 'TFUELBTC', 'ONEBTC', 'FTMBTC', 'BTCBBTC', 'ALGOBTC', 'ERDBTC', 'DOGEBTC', 'DUSKBTC', 'ANKRBTC', 'WINBTC', 'COSBTC', 'COCOSBTC', 'TOMOBTC', 'PERLBTC', 'CHZBTC', 'BANDBTC', 'BEAMBTC', 'XTZBTC', 'HBARBTC', 'NKNBTC', 'STXBTC', 'KAVABTC', 'ARPABTC', 'CTXCBTC', 'BCHBTC', 'TROYBTC', 'VITEBTC', 'FTTBTC', 'OGNBTC', 'DREPBTC', 'TCTBTC', 'WRXBTC', 'LTOBTC', 'MBLBTC', 'COTIBTC', 'STPTBTC', 'SOLBTC', 'CTSIBTC', 'HIVEBTC', 'CHRBTC', 'MDTBTC', 'STMXBTC', 'PNTBTC', 'DGBBTC', 'COMPBTC', 'SXPBTC', 'SNXBTC', 'IRISBTC', 'MKRBTC', 'DAIBTC', 'RUNEBTC', 'FIOBTC', 'AVABTC', 'BALBTC', 'YFIBTC', 'JSTBTC', 'SRMBTC', 'ANTBTC', 'CRVBTC', 'SANDBTC', 'OCEANBTC', 'NMRBTC', 'DOTBTC', 'LUNABTC', 'IDEXBTC', 'RSRBTC', 'PAXGBTC', 'WNXMBTC', 'TRBBTC', 'BZRXBTC', 'WBTCBTC', 'SUSHIBTC', 'YFIIBTC', 'KSMBTC', 'EGLDBTC', 'DIABTC', 'UMABTC', 'BELBTC', 'WINGBTC', 'UNIBTC', 'NBSBTC', 'OXTBTC', 'SUNBTC', 'AVAXBTC', 'HNTBTC', 'FLMBTC', 'SCRTBTC', 'ORNBTC', 'UTKBTC', 'XVSBTC', 'ALPHABTC', 'VIDTBTC', 'AAVEBTC', 'NEARBTC', 'FILBTC', 'INJBTC', 'AERGOBTC', 'AUDIOBTC', 'CTKBTC', 'BOTBTC', 'AKROBTC', 'AXSBTC', 'HARDBTC', 'RENBTCBTC', 'STRAXBTC', 'FORBTC', 'UNFIBTC', 'ROSEBTC', 'SKLBTC', 'SUSDBTC', 'GLMBTC', 'GRTBTC', 'JUVBTC', 'PSGBTC', '1INCHBTC', 'REEFBTC', 'OGBTC', 'ATMBTC', 'ASRBTC', 'CELOBTC', 'RIFBTC', 'BTCSTBTC', 'TRUBTC', 'CKBBTC', 'TWTBTC', 'FIROBTC', 'LITBTC', 'SFPBTC', 'FXSBTC', 'DODOBTC', 'FRONTBTC', 'EASYBTC', 'CAKEBTC', 'ACMBTC', 'AUCTIONBTC', 'PHABTC', 'TVKBTC', 'BADGERBTC', 'FISBTC', 'OMBTC', 'PONDBTC', 'DEGOBTC', 'ALICEBTC', 'LINABTC', 'PERPBTC', 'RAMPBTC', 'SUPERBTC', 'CFXBTC', 'EPSBTC', 'AUTOBTC', 'TKOBTC', 'TLMBTC', 'MIRBTC', 'BARBTC', 'FORTHBTC', 'EZBTC', 'ICPBTC', 'ARBTC', 'POLSBTC', 'MDXBTC', 'LPTBTC', 'AGIXBTC', 'NUBTC', 'ATABTC', 'GTCBTC', 'TORNBTC', 'BAKEBTC', 'KEEPBTC']
    patterns = ['COUNTERATTACK',
                'UNIQUE3RIVER',
                'LONGLINE',
                'LONGLEGGEDDOJI',
                '3STARSINSOUTH',
                'DOJISTAR' ,
                'ENGULFING',
                'HANGINGMAN',
                'HARAMICROSS',
                'INVERTEDHAMMER',
                'SHOOTINGSTAR',
                'DOJI']

    # Interval options: '1m', '5m', ... '3D'
    binance_options = {
        'symbols': symbols,
        'client': client,
        'interval': '5m',
        'limit': 20
    }
    settings = {
        'discord_webhook': patterns_webhook,
        'discord_sleep': 2,
        'patterns': patterns
    }

    p = Patterns(binance_options = binance_options, **settings)
    p.start()

