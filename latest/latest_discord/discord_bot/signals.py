import numpy as np

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]


#utility // so funciona para o rsi_overbought_oversold
def rsi_volatility(price_list):
    content = []
    inicial_price = price_list[-9]
    for x in price_list:
        content.append(((inicial_price-x)*100/inicial_price)-100)
    
    content = [np.round(x, 2) for x in content[-10:]]
    return content

#signal
def rsi_overbought_oversold(real,sym, interval, indicator, h, l, c):
    content = None
    if real[-1] >= 77 and real[-2] >= 70:
        if  h[-1] > h[-2] and h[-2] > h[-3] and h[-3] > h[-4] and h[-4] > h[-5] :
            circle = ":red_circle:"
            content = f"\n{circle}  {sym} :candle:  **{interval}** \n```**{indicator}** {real[-8:-1]}\n**Rsi Variation** {rsi_volatility(real)[-8:-1]}\n**Price** {c[-8:-1]}\n**Price Variation** {rsi_volatility(c)[-8:-1]}```"
    elif real[-1] < 23  and real[-2] < 30 and real[-2] > 12 and real[-1] > 12:
        if  l[-1] < l[-2] and l[-2] < l[-3] and l[-3] < l[-4] and l[-4] < l[-5]:
            circle = ":green_circle:"
            content = f"\n{circle}  {sym} :candle:  **{interval}** \n```**{indicator}** {real[-8:-1]}\n**Rsi Variation** {rsi_volatility(real)[-8:-1]}\n**Price** {c[-8:-1]}\n**Price Variation** {rsi_volatility(c)[-8:-1]}```"
    return content

#signal
def macd_crossover(macd,macdsignal, sym, interval, indicator):
    content = None
    if macd[-4] > macdsignal[-4] and macd[-3] < macdsignal[-3] and macd[-2] < macdsignal[-2] and macd[-1] < macdsignal[-1]:
        circle = ":red_circle:"
        content = f"\n{circle}  {sym} :candle:  **{interval}** \n```{indicator} **CROSSOVER**```"
    elif macd[-4] < macdsignal[-4] and macd[-3] > macdsignal[-3] and macd[-2] > macdsignal[-2] and macd[-1] > macdsignal[-1]:
        circle = ":green_circle:"
        content = f"\n{circle}  {sym} :candle:  **{interval}** \n```{indicator} **CROSSOVER**```"
    return content

#signal
def ema_crossover(ema1,ema2, sym, interval):
    content = None
    name1 = namestr(ema1, globals())
    name2 = namestr(ema2, globals())
    if name1 and name2:
        if ema1[-4] > ema2[-4] and ema1[-3] < ema2[-3] and ema1[-2] < ema2[-2] and ema1[-1] < ema2[-1]:
            circle = ":red_circle:"
            content = f"\n{circle}\t{sym} last **{interval}** \n```{name2[0]} **CROSSOVER** {name1[0]}```"
        elif ema1[-4] < ema2[-4] and ema1[-3] > ema2[-3] and ema1[-2] > ema2[-2] and ema1[-1] > ema2[-1]:
            circle = ":green_circle:"
            content = f"\n{circle}\t{sym} last **{interval}** \n```{name1[0]} **CROSSOVER** {name2[0]}```"
    return content


#signal
def rsi_price_divergence(real, c, interval, indicator, sym):
    content = None

    rsi_avg = []
    price_avg = []
    i = 0
    while i < 4:
        j = i*4
        rsi_avg.append(sum(real[-13+j:-9+j])/len(real[-13+j:-9+j]))
        price_avg.append(sum(c[-13+j:-9+j])/len(c[-13+j:-9+j]))
        i+=1
    if rsi_avg[0] < rsi_avg[1] and rsi_avg[1] > rsi_avg[2] and rsi_avg[2] < rsi_avg[3] and rsi_avg[1] > rsi_avg[3]:
        if  price_avg[0] > price_avg[1] and price_avg[1] < price_avg[2] and price_avg[2] > price_avg[3] and price_avg[1] < price_avg[3]:
            circle = ":red_circle:"
            content = f"\n{circle}  {sym} :candle:  **{interval}** \n```**{indicator}** {real[-8:-1]}\n**Rsi Divergence** ```"
    elif rsi_avg[0] > rsi_avg[1] and rsi_avg[1] < rsi_avg[2] and rsi_avg[2] > rsi_avg[3] and rsi_avg[1] < rsi_avg[3]:
        if  price_avg[0] < price_avg[1] and price_avg[1] > price_avg[2] and price_avg[2] < price_avg[3] and price_avg[1] > price_avg[3]:
            circle = ":green_circle:"
            content = f"\n{circle}  {sym} :candle:  **{interval}** \n```**{indicator}** {real[-8:-1]}\n**Rsi Divergence** ```"
    return content
