'''
defmakedf.py
'''

def mdfmake(x, y, m):
    
    import numpy as np
    import pandas as pd
    import pandas_datareader as data 
    import datetime as datetime


    stcode = x
    dt_now = datetime.datetime.now()
    ly = dt_now.year
    lm = dt_now.month
    ld = dt_now.day
    
    stock = data.DataReader(stcode,'stooq',start=datetime.date(y, m, 1),end=datetime.date(ly,lm,ld))
    #datetime.datetime(ly,lm,ld))

    stock = stock.sort_values(by='Date')

    #%Y-%m の形にそろえる列ｙｍを作成し、リスト化
    stock['ym'] = stock.index.strftime("%Y-%m")

    listym = list(stock['ym'])

    #ym の重複をなくす
    mlist = stock['ym'].unique()

    #DateのMultiindexを解除
    stock = stock.reset_index()
    highs = []


    #毎月の株価を格納するリストを作成
    for i in range(len(mlist)):
        sc = stock['High'][stock['ym']==mlist[i]]
        listedsc = list(sc)
        highmonth = max(listedsc)
        highs.append(highmonth)

        
    print('end')

    return highs
    

    
#madedf = mdfmake("1306.JP",2009)
#madedf


