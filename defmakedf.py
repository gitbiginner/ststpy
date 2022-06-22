'''
defmakedf.py
'''

def mdfmake(x,y,m):
    
    import numpy as np
    import pandas as pd
    import pandas_datareader.data as web
    import datetime as datetime


    stcode = x
    dt_now = datetime.datetime.now()
    ly = dt_now.year
    lm = dt_now.month-1
    ld = dt_now.day
    
    stock = web.DataReader(stcode,
                           'stooq',
                           start=datetime.datetime(y,m,1),
                           end=datetime.datetime(ly,lm,31))

    stock = stock.sort_values(by='Date')

    #%Y-%m の形にそろえる列ｙｍを作成し、リスト化
    stock['ym'] = stock.index.strftime("%Y-%m")

    listym = list(stock['ym'])

    #ym の重複をなくす
    mlist = stock['ym'].unique()

    #DateのMultiindexを解除
    stock = stock.reset_index()

    sclist = []

    #毎月の株価を格納するリストを作成
    for i in range(len(mlist)):
        sc = stock['Close'][stock['ym']==mlist[i]]
        listedsc = list(sc)
        sclist.append(listedsc)
        
    print('end')

    listedml = list(mlist)

    #リストをdf化し、転地して列と行を調整
    scdf = pd.DataFrame(sclist).T
    scdf.columns = listedml
    #scdf.index = scdf['days']
    return scdf
    

    
#madedf = mdfmake("1306.JP",2009)
#madedf

