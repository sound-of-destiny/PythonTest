import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.metrics import mean_squared_error
from math import sqrt
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX

df = pd.read_excel('CRE/000002.xls',usecols=[5,10])
test_size = 5
train_size = int(len(df) - test_size)
train,test = df[:train_size],df[train_size:] 

df.index = pd.to_datetime(df.END_DATE,format='%Y-%m-%d') 
train.index = pd.to_datetime(train.END_DATE,format='%Y-%m-%d') 
test.index = pd.to_datetime(test.END_DATE,format='%Y-%m-%d') 
'''
train.REVENUE.plot(figsize=(15,8), title= 'Daily Ridership', fontsize=14)
test.REVENUE.plot(figsize=(15,8), title= 'Daily Ridership', fontsize=14)
plt.show()

dd= np.asarray(train.REVENUE)
y_hat = test.copy()
y_hat['naive'] = dd[len(dd)-1]
plt.figure(figsize=(12,8))
plt.plot(train.index, train['REVENUE'], label='Train')
plt.plot(test.index,test['REVENUE'], label='Test')
plt.plot(y_hat.index,y_hat['naive'], label='Naive Forecast')
plt.legend(loc='best')
plt.title("Naive Forecast")
plt.show()

y_hat_avg = test.copy()
y_hat_avg['avg_forecast'] = train['REVENUE'].mean()
plt.figure(figsize=(12,8))
plt.plot(train['REVENUE'], label='Train')
plt.plot(test['REVENUE'], label='Test')
plt.plot(y_hat_avg['avg_forecast'], label='Average Forecast')
plt.legend(loc='best')
plt.show()

y_hat_avg = test.copy()
y_hat_avg['moving_avg_forecast'] = train['REVENUE'].rolling(4).mean().iloc[-1]
plt.figure(figsize=(16,8))
plt.plot(train['REVENUE'], label='Train')
plt.plot(test['REVENUE'], label='Test')
plt.plot(y_hat_avg['moving_avg_forecast'], label='Moving Average Forecast')
plt.legend(loc='best')
plt.show()

y_hat_avg = test.copy()
fit2 = SimpleExpSmoothing(np.asarray(train['REVENUE'])).fit(smoothing_level=0.6,optimized=False)
y_hat_avg['SES'] = fit2.forecast(len(test))
plt.figure(figsize=(16,8))
plt.plot(train['REVENUE'], label='Train')
plt.plot(test['REVENUE'], label='Test')
plt.plot(y_hat_avg['SES'], label='SES')
plt.legend(loc='best')
plt.show()

sm.tsa.seasonal_decompose(train.REVENUE,freq=4).plot()
result = sm.tsa.stattools.adfuller(train.REVENUE)
plt.show()

y_hat_avg = test.copy()

fit1 = Holt(np.asarray(train['REVENUE'])).fit(smoothing_level = 0.3,smoothing_slope = 0.1)
y_hat_avg['Holt_linear'] = fit1.forecast(len(test))

plt.figure(figsize=(16,8))
plt.plot(train['REVENUE'], label='Train')
plt.plot(test['REVENUE'], label='Test')
plt.plot(y_hat_avg['Holt_linear'], label='Holt_linear')
plt.legend(loc='best')
plt.show()

y_hat_avg = test.copy()
fit1 = ExponentialSmoothing(np.asarray(train['REVENUE']) ,seasonal_periods=4 ,trend='add', seasonal='add',).fit()
y_hat_avg['Holt_Winter'] = fit1.forecast(len(test))
plt.figure(figsize=(16,8))
plt.plot( train['REVENUE'], label='Train')
plt.plot(test['REVENUE'], label='Test')
plt.plot(y_hat_avg['Holt_Winter'], label='Holt_Winter')
plt.legend(loc='best')
plt.show()
'''
pdq = (2, 1, 4)
PDQ = (0, 1, 1, 4)
model_train = SARIMAX(train.REVENUE, order=pdq,seasonal_order=PDQ).fit()
predict_train = model_train.forecast(test_size + 1)
#fitted_train = model_train.fittedvalues.append(predict_train)

model_run = SARIMAX(df.REVENUE, order=pdq, seasonal_order=PDQ).fit() 
predict_run = model_run.forecast(1)
#fitted_run = model_run.fittedvalues.append(predict_run) 

predict_run.to_csv('sub.csv', index = False, tupleize_cols = True)
#predict_run.to_csv('sub.csv')

plt.plot(df.REVENUE, label='df', marker='o')
plt.plot(predict_train, label='SARIMA', marker='o', linestyle='--')
plt.plot(predict_run, label='SARIMA_RUN', marker='o')
#plt.plot(df[-1].REVENUE, predict_run, linestyle='--')
plt.legend(loc='best')
plt.show()