##This is the file that opens the chart
import datetime as dt
#import candlestick_data2
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf
import pandas_datareader as wb 
import MACD_Indicator as MI

#add pandadata reader dependency
from mplfinance.original_flavor import candlestick_ohlc

#Define Time Fram

import yfinance as yf


#if using yf , must be a 60 day period if time interval is greater than 1m and less than 90m, 1h is 730 days, 1d is infinite, 1m is last 7 days. 
start_date = dt.datetime(2023,4,6)
end_date = dt.datetime(2023,6,3) 

print(start_date)
print(end_date)

# Load Data
ticker = 'NQM23.CME'
data = yf.download(tickers = ticker,  # list of tickers
            start = start_date,         # time period
            end = end_date,
            interval = "5m",       # trading interval
            prepost = False,       # download pre/post market hours data?
            repair = False)         # repair obvious price errors e.g. 100x? asks for 1minute information which causes call rate to exceed lim when set to true 

print(data.head())

#Restructure Data

dataPlot = data[['Open','High','Low','Close']]
#mpf.plot(dataPlot, type= "candle", style = "nightclouds")
print("Restructured data")
print(dataPlot)

#dataPlot will use the dates as the index representation, while data will use 0,1,2,3... as the index represention, throwing the dates into a new colunm

data.reset_index(inplace=True)

#copy = data['datetime'].map(mdates.date2num)



#### Need to fix below code since we changed libraries to access the candlestick data 

print(data['Datetime'])
#copy = data['datetime'].map(mdates.date2num)
copy = data['Datetime'].map(mdates.date2num)
#data['Datetime'] = copy
print(data['Datetime'])

#close_colunm = CC.data['close']
movingPeriod = 5
day_5_emaTest = MI.EMA(movingPeriod, 5, [])
day_5_emaTest.createXEMA(data['Close'])

print("Start ema Test")
print(day_5_emaTest.EMARecord)

print(len(data['Datetime']))
print(len(day_5_emaTest.EMARecord))
EMALineTest = []

for i in range (len(day_5_emaTest.EMARecord)):
#for i in range (len(data['Datetime'])-movingPeriod-1):
    EMALineTest.append((data['Datetime'][i+movingPeriod-1], day_5_emaTest.EMARecord[i-1]))

print(len(day_5_emaTest.EMARecord))
print(len(dataPlot))
print(movingPeriod)

for i in range (movingPeriod) :
    dataPlot.iloc[1: , :]


macdObj = MI.MACD()
macdObj.create_macd(26,12,9,data['Close'])
print(len(data['Datetime']))
print(len(data['Close']))
print(len(macdObj.signal))
print(len(macdObj.twEMA))
print(len(macdObj.tsEMA))
print(len(macdObj.macdLine))


#ap = [mpf.make_addplot(day_5_emaTest.EMARecord,panel=1,type='line',ylabel='Line'),
#      mpf.make_addplot()]


#mpf.plot(dataPlot.tail(len(macdObj.macdLine) - len(dataPlot)),type='candle',ylabel='Candle', addplot=ap, style = "nightclouds")



#mpf.plot(dataPlot, type= "candle", style = "nightclouds", alines = EMALineTest)
#mpf.plot(dataPlot, type= "candle", style = "nightclouds")
#print(data)
#print(copy.head())



#visualization


#ax = plt.subplot()
#ax.grid(True)
#ax.set_title(ticker, color="white")
#ax.set_axisbelow(True)
#ax.set_facecolor('black')
#ax.figure.set_facecolor('#121212')
#ax.tick_params(axis='x', colors='white')
#ax.tick_params(axis='y', colors='white')
#ax.xaxis_date()
#candlestick_ohlc(ax, data.values, width=0.5, colorup='g',colordown='r')

#plt.show()
