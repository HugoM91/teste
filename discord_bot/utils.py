import numpy as np
import talib
from talib import BOP ,MACD, ADX, AROONOSC, STOCHRSI, WILLR, OBV, BBANDS, EMA, ATR,TRANGE, RSI, CDLCOUNTERATTACK, CDLUNIQUE3RIVER, CDLLONGLINE, CDLLONGLEGGEDDOJI, CDL3STARSINSOUTH, CDL3WHITESOLDIERS, CDLDOJI, CDLDOJISTAR, CDLENGULFING, CDLHANGINGMAN, CDLHARAMICROSS, CDLINVERTEDHAMMER, CDLSHOOTINGSTAR, ADX, AROON, AROONOSC, BOP, CCI , CMO, DX , MACD , RSI, STOCHRSI, TRIX


# used in indicators.py
def talib_indicator(indicators, ohlcv, sym, interval,  **indicators_config):
    """
        params:

        returns dict
    """
    ohlcv = [list(map(float, candle)) for candle in ohlcv]

    o = np.array([np.round(x[0],6) for x in ohlcv])
    h = np.array([np.round(x[1],6) for x in ohlcv])
    l = np.array([np.round(x[2],6) for x in ohlcv])
    c = np.array([np.round(x[3],6) for x in ohlcv])
    v = np.array([np.round(x[4],6) for x in ohlcv])

    out = {}
    for indicator in indicators:
        content = None
        
        if indicator == 'RSI':
            real = RSI(c, **indicators_config[indicator])
            real = [np.round(x, 5) for x in real]
            if real[-1] >= 70 and real[-2] >= 67:
                if  h[-1] > h[-2] and h[-2] > h[-3] and h[-3] > h[-4] :
                    circle = ":red_circle:"
                    content = f"\n{circle}\t{sym} last **{interval}** \n```**{indicator}** {real[-8:-1]}\nPrice {c[-8:-1]}```"
            elif real[-1] < 30  and real[-2] < 33 and real[-2] > 12 and real[-1] > 12:
                if  l[-1] < l[-2] and l[-2] < l[-3] and l[-3] < l[-4]:
                    circle = ":green_circle:"
                    content = f"\n{circle}\t{sym} last **{interval}** \n```**{indicator}** {real[-8:-1]}\nPrice {c[-8:-1]}```"

        elif indicator == 'MACD':
            macd, macdsignal, macdhist = MACD(c, **indicators_config[indicator])
            macd = [np.round(x, 5) for x in macd]
            macdsignal = [np.round(x, 5) for x in macdsignal]

            if macd[-4] > macdsignal[-4] and macd[-3] < macdsignal[-3] and macd[-2] < macdsignal[-2] and macd[-1] < macdsignal[-1]:
                circle = ":red_circle:"
                content = f"\n{circle}\t{sym} last **{interval}** \n```{indicator} **CROSSOVER**```"
            elif macd[-4] < macdsignal[-4] and macd[-3] > macdsignal[-3] and macd[-2] > macdsignal[-2] and macd[-1] > macdsignal[-1]:
                circle = ":green_circle:"
                content = f"\n{circle}\t{sym} last **{interval}** \n```{indicator} **CROSSOVER**```"

        elif indicator == 'ADX':
            real = ADX(h, l, c, **indicators_config[indicator])


        elif indicator == 'AROONOSC':
            real = AROONOSC(h, l, **indicators_config[indicator])

        elif indicator == 'WILLR':
            real = WILLR(h, l, c, **indicators_config[indicator])

        elif indicator == 'OBV':
            real = OBV(c, v)

        elif indicator == 'ATR':
            real = ATR(h, l, c, **indicators_config[indicator])

        elif indicator == 'BOP':
            real = BOP(o, h, l, c)    

        elif indicator == 'TRANGE':
            real = TRANGE(h, l, c)

        elif indicator == 'BBANDS':
            upperband, middleband, lowerband = BBANDS(c, **indicators_config[indicator])

        elif indicator == 'STOCHRSI':
            fastk, fastd = STOCHRSI(c, **indicators_config[indicator])

        elif indicator == 'EMA':
            circle = ':green_circle'
            ema7 = EMA(c, timeperiod=7)
            ema14 = EMA(c, timeperiod=14)
            ema28 = EMA(c, timeperiod=28)
            ema56 = EMA(c, timeperiod=56)
            ema112 = EMA(c, timeperiod=112)
            ema224 = EMA(c, timeperiod=224)

            if ema56[-4] > ema224[-4] and ema56[-3] < ema224[-3] and ema56[-2] < ema224[-2] and ema56[-1] < ema224[-1]:
                circle = ":red_circle:"
                content = f"\n{circle}\t{sym} last **{interval}** \n```{indicator}56 **CROSSOVER** EMA224```"
            elif ema56[-4] < ema224[-4] and ema56[-3] > ema224[-3] and ema56[-2] > ema224[-2] and ema56[-1] > ema224[-1]:
                circle = ":green_circle:"
                content = f"\n{circle}\t{sym} last **{interval}** \n```{indicator}56 **CROSSOVER** EMA224```"


        out[indicator] = content

    return out


# used in patterns.py
def talib_pattern(patterns, ohlcv):
    """
      params:

      returns dict - {'ENGULFING': [0,0,0,100,0]}
    """

    ohlcv = [list(map(float, candle)) for candle in ohlcv]

    o = np.array([x[0] for x in ohlcv])
    h = np.array([x[1] for x in ohlcv])
    l = np.array([x[2] for x in ohlcv])
    c = np.array([x[3] for x in ohlcv])
    v = np.array([x[4] for x in ohlcv])

    out = {}
    for pattern in patterns:
        # - 0 meaning no pattern found.
        # - 100 meaning pattern found upwards (bullish indicator)
        # - -100 (negative 100) meaning pattern found downwards (bearish indicator)

        if pattern == '3STARSINSOUTH':
            integer = CDL3STARSINSOUTH(o,h,l,c)
        elif pattern == '3WHITESOLDIERS':
            integer = CDL3WHITESOLDIERS(o,h,l,c)
        elif pattern == 'DOJI':
            integer = CDLDOJI(o,h,l,c)
        elif pattern == 'DOJISTAR':
            integer = CDLDOJISTAR(o,h,l,c)
        elif pattern == 'ENGULFING':
            integer = CDLENGULFING(o,h,l,c)
        elif pattern == 'HANGINGMAN':
            integer = CDLHANGINGMAN(o,h,l,c)
        elif pattern == 'HARAMICROSS':
            integer = CDLHARAMICROSS(o,h,l,c)
        elif pattern == 'INVERTEDHAMMER':
            integer = CDLINVERTEDHAMMER(o,h,l,c)
        elif pattern == 'SHOOTINGSTAR':
            integer = CDLSHOOTINGSTAR(o,h,l,c)
        elif pattern == 'LONGLEGGEDDOJI':
            integer = CDLLONGLEGGEDDOJI(o,h,l,c)
        elif pattern == 'LONGLINE':
            integer = CDLLONGLINE(o,h,l,c)
        elif pattern == 'UNIQUE3RIVER':
            integer = CDLUNIQUE3RIVER(o,h,l,c)
        elif pattern == 'COUNTERATTACK':
            integer = CDLCOUNTERATTACK(o,h,l,c)

        if any([x == 100 or x == -100 for x in integer]):
            out[pattern] = integer.tolist()

    return out
