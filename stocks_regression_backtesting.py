
import pandas_datareader as web
import datetime as dt



from pandas_datareader import data
import matplotlib.pyplot as plt
import datetime as dt
import urllib.request, json
import os
import numpy as np
import seaborn as sns
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

import warnings
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)

statsToAnalyze=['Close', 'Open', 'Volume', 'High', 'Low']
durationsToAnalyze=[2,3,4,5,10,20]

def addMean(data, columnName, duration):
    data[str(duration)+' Day Mean '+columnName]=data[columnName].rolling(duration).mean()

def addStatAnalytics(data, columnName):
    # data[columnName+' Derivate']=np.gradient(data[columnName])
    # data[columnName+' 2nd Derivate']=np.gradient(data[columnName+' Derivate'])

    data[columnName+' Derivate']=data[columnName].diff() / data['Date'].diff().dt.total_seconds()
    data[columnName+' 2nd Derivate']=data[columnName+' Derivate'].diff() / data['Date'].diff().dt.total_seconds()

    # data[columnName].diff() / data['Date'].diff().dt.total_seconds()

    for duration in durationsToAnalyze:
        data[str(duration)+' Day Mean '+columnName]=data[columnName].rolling(duration).mean()
        data[str(duration)+' Day Mean '+columnName+' Derivate']=data[columnName].diff() / data['Date'].diff().dt.total_seconds()
        data[str(duration)+' Day Mean '+columnName+' 2nd Derivate']=data[columnName+' Derivate'].diff() / data['Date'].diff().dt.total_seconds()

    data = data.copy()


performance={}

for stock in ['AMD','ADBE','ALGN','AMZN','AAPL','AMAT','ASML','TEAM','ADSK','GOOG','GOOGL']:
    # stock_name=stock

    start = dt.datetime(2016,1,1)
    end = dt.datetime.now()

    sell_time = 2 #in days

    historical_data = web.DataReader(stock, 'yahoo', start, end)

    historical_data = historical_data.assign(Date=historical_data.index.values)
    historical_data['Date'] = historical_data.index.values

    historical_data.reset_index(drop=True, inplace=True)

    a=[]
    spreads=[]
    for index, row in historical_data.iterrows():
        max_next_index = min(index+sell_time, len(historical_data)-1)
        a.append(historical_data['Close'][max_next_index]/row['Close'])
        spreads.append(row['High']-row['Low'])

    historical_data['Spread'] = pd.Series(np.array(spreads))
    historical_data['Buy'] = pd.Series(np.array(a))

    for stat in statsToAnalyze:
        addStatAnalytics(historical_data, stat)

    historical_data = historical_data.iloc[durationsToAnalyze[-1]-1: , :]
    historical_data.reset_index(drop=True, inplace=True)


    # print(historical_data)
    # print(historical_data.info())



    for column in historical_data:
        if column not in ['Buy', 'Date']:
            x=historical_data[column].to_numpy().reshape(-1, 1)
            y=historical_data['Buy'].to_numpy()

            #Linear Regression
            # model = LinearRegression().fit(x, y)
            # r_sq = model.score(x, y)


            #Polynomial Regression
            x_ = PolynomialFeatures(degree=2, include_bias=False).fit_transform(x)
            model = LinearRegression().fit(x_, y)
            r_sq = model.score(x_, y)


            performance[stock, column]=r_sq

            # Prints results
            # print(stock, column)
            # print('coefficient of determination:', r_sq)
            # print('intercept:', model.intercept_)
            # print('coefficients:', model.coef_)
            # print()

prev_stocks= []
for w in sorted(performance, key=performance.get, reverse=True):
    if w[0] not in prev_stocks:
        print(w[0], "stock compared with the", w[1], "gave an R^2 of", round(performance[w], 4))
        prev_stocks.append(w[0])























