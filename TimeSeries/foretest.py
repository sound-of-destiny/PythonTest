import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from statsmodels.tsa.statespace.sarimax import SARIMAX
import warnings
import itertools
import sys
df = pd.read_excel('CRE/000007.xls',usecols=[5,10])
df = df.drop_duplicates('END_DATE').sort_values('END_DATE')
test_size = 5
train_size = int(len(df) - test_size)
train,test = df[:train_size],df[train_size:] 
df.index = pd.to_datetime(df.END_DATE,format='%Y-%m-%d') 
train.index = pd.to_datetime(train.END_DATE,format='%Y-%m-%d') 
test.index = pd.to_datetime(test.END_DATE,format='%Y-%m-%d') 
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
            mod = SARIMAX(train.REVENUE,
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
print(s)
'''
pdq = (0, 1, 1)
PDQ = (1, 1, 1, 4)
model_train = SARIMAX(train.REVENUE, order=pdq,seasonal_order=PDQ, enforce_stationarity=False).fit()
predict_train = model_train.forecast(test_size+1)

model_run = SARIMAX(df.REVENUE, order=pdq, seasonal_order=PDQ).fit() 
predict_run = model_run.forecast(1)

#residual = predict_train - test
'''
print(model_train.summary())
model_train.plot_diagnostics()
'''
print(predict_run[0])
plt.plot(df.REVENUE, label='df', marker='o')
plt.plot(predict_train, label='SARIMA', marker='o', linestyle='--')
plt.plot(predict_run, label='SARIMA_RUN', marker='o')
plt.legend(loc='best')

plt.show()
