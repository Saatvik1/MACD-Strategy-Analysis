import datetime as dt

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from mplfinance.original_flavor import candlestick_ohlc

#Define Time Fram

import yfinance as yf



start = dt.datetime(2023,1,3)
end = dt.datetime(2023,1,24)

print(start)
print(end)

# Load Data
ticker = 'AAPL'
data = yf.download(ticker, start, end)


#Restructure Data

data = data[['Open','High','Low','Close']]

data.reset_index(inplace=True)

copy = data['Date'].map(mdates.date2num)
data['Date'] = copy

print(data)

print(copy.head())

#visualization

ax = plt.subplot()
ax.grid(True)
ax.set_title(ticker, color="white")
ax.set_axisbelow(True)
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.xaxis_date()
candlestick_ohlc(ax,data.values, width=0.5, colorup='g',colordown='r')

plt.show()
