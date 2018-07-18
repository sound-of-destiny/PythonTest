import pandas as pd 
import numpy as np 
from statsmodels.tsa.statespace.sarimax import SARIMAX
import warnings
import itertools
import sys

TS = pd.read_csv('forecast.csv', header=None)
TS.insert(1, column = 'B', value = '1')
for tc in TS.values:
    ti = tc[0][0:6]
    if ti == '000750':
        continue
    if ti == '000776':
        continue
    #df = pd.read_excel('CRE/000002.xls',usecols=[5,10])
    df = pd.read_excel('CRE/'+ti+'.xls')
    df = df.drop_duplicates('END_DATE').sort_values('END_DATE')
    df.index = pd.to_datetime(df.END_DATE,format='%Y-%m-%d') 

    pdq = (0, 1, 1)
    PDQ = (1, 1, 1, 4)
    '''
    p = d = q = range(0, 2)
    pdq = list(itertools.product(p, d, q))
    PDQ = [(x[0], x[1], x[2], 4) for x in list(itertools.product(p, d, q))]
    warnings.filterwarnings("ignore") # specify to ignore warning messages
    a = sys.maxsize
    s = 'error'
    for param in pdq:
        for param_seasonal in PDQ:
            try:
                mod = SARIMAX(df.REVENUE,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)

                results = mod.fit()
                if results.aic < a:
                    a = results.aic
                    s = 'ARIMA{}x{} - AIC:{}'.format(param, param_seasonal, results.aic)
            except:
                continue
    '''
    print(ti)
    model_run = SARIMAX(df.REVENUE, order=pdq, seasonal_order=PDQ ,enforce_invertibility=False, enforce_stationarity=False).fit() 
    predict_run = model_run.forecast(1)

    tc[1] = predict_run.values[0]

TS.to_csv('sub.csv', index = False)