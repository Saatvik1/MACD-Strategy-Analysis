import datetime as dt
import candlestick_data2
import MACD_Indicator
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf
import pandas_datareader as wb 

#add pandadata reader dependency
from mplfinance.original_flavor import candlestick_ohlc

#Define Time Fram

import yfinance as yf



start = dt.datetime(2023,1,3)
end = dt.datetime(2023,1,24)

print(start)
print(end)

# Load Data
ticker = 'NQH3'
#data = yf.download(ticker, start, end)


#Restructure Data
#data = candlestick_data2.nas_fut
data = candlestick_data2.nas_fut_5min
data = data[['open','high','low','close']]
mpf.plot(data, type= "candle", style = "nightclouds")



data.reset_index(inplace=True)

#copy = data['datetime'].map(mdates.date2num)

copy = data['datetime'].map(mdates.date2num)
data['datetime'] = copy



print(data)

print(copy.head())



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
