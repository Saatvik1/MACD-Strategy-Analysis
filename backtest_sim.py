import candlestick_chart as chart
import numpy as np

#class for editing testing parameters -- although this may be a longer term goal 
#going to place buy and sell signals whenever they cross... with no regard for RR. 

#macdLINE = blue 
#macdSignal = purple

#two runs for checking the profits, one run will be buys waiting for sell to exit
#the other run is sells waiting for a buy to exit 

#1 indicates buy, 0 indicates nothing, -1 indicates sell 
buy_sell = []
last_sig = 0
#macdline above signal 

if(chart.macdObj.macdLine[0] > chart.macdObj.signal[0]): 
    buy_sell.append(1)
    last_sig = 1
elif(chart.macdObj.macdLine[0] < chart.macdObj.signal[0]):
    buy_sell.append(-1)
    last_sig = -1
else:
    if(chart.macdObj.macdLine[0] > chart.macdObj.signal[0]): 
        buy_sell.append(1)
        last_sig = 1
    else:
        buy_sell.append(-1)
        last_sig = -1


for i in range(1,len(chart.macdObj.signal)):
    #buy signal 
    if(chart.macdObj.macdLine[i] > chart.macdObj.signal[i] and last_sig == -1):
        buy_sell.append(1)
        last_sig = 1
        continue
    
    elif(chart.macdObj.macdLine[i] < chart.macdObj.signal[i] and last_sig == 1):
        buy_sell.append(-1)
        last_sig = -1
        continue

    buy_sell.append(0)

#dataPlot_copy = chart.dataPlot.values.tolist()
#dataPlot_copy.reset_index(inplace=True)
dataPlot_copy = chart.dataPlot.tail(len(chart.macdObj.macdLine) - len(chart.dataPlot))

#print(dataPlot_copy)

buy_scatter = []
for i in range(len(buy_sell)):
    if(buy_sell[i] == 1):
        buy_scatter.append(dataPlot_copy["Close"].iloc[i])
    else:
        buy_scatter.append(np.nan)


sell_scatter = []
for i in range(len(buy_sell)):
    if(buy_sell[i] == -1):
        sell_scatter.append(dataPlot_copy["Close"].iloc[i])
    else:
        sell_scatter.append(np.nan)

#print(sell_scatter)

#chart.ap.append(chart.mpf.make_addplot(buy_scatter, type = "scatter", markersize = 150, marker = "^"),)
#chart.ap.append(chart.mpf.make_addplot(sell_scatter, type = "scatter", markersize = 150, marker = "v"),)

apa = [chart.mpf.make_addplot(chart.macdObj.signal, panel =1 , type='line',ylabel='Line', secondary_y = True, color = "fuchsia"), 
    chart.mpf.make_addplot(chart.macdObj.macdLine, panel = 1, type='line',ylabel='Line', secondary_y = False, color = "b"),
    chart.mpf.make_addplot(buy_scatter, type = "scatter", markersize = 150, marker = "^"),
    chart.mpf.make_addplot(sell_scatter, type = "scatter", markersize = 150, marker = "v"),]



#2 for loops, one finding all the buy signals first, and then find all the sell signals to close the trades 
#2nd for loop is for finding all the second sell signals to open the trade and then looking for the next buy signal to close the trade

profit_list = []

#buy loop
iter = 0
for i in range(max(len(buy_scatter), len(sell_scatter))):
    if(not np.isnan(buy_scatter[i])):
        temp = buy_scatter[i]
        print("sdasdasdass")
        print(buy_scatter[i])
        j = i + 1
        while(j < len(buy_sell)):
            if(not np.isnan(sell_scatter[j])):
                profit_list.append((sell_scatter[j] - buy_scatter[i]) * 20)
                break
            else:
                j = j+1
 
#sell loop
for i in range(max(len(buy_scatter), len(sell_scatter))):
    if(not np.isnan(sell_scatter[i])):
        temp = sell_scatter[i]
        j = i + 1
        while(j < len(buy_sell)):
            if(not np.isnan(buy_scatter[j])):
                profit_list.append((sell_scatter[i] - buy_scatter[j]) * 20)
                break
            else:
                j = j+1        

#print(buy_scatter)
print(profit_list)
print(sum(profit_list))



chart.mpf.plot(chart.dataPlot.tail(len(chart.macdObj.macdLine) - len(chart.dataPlot)),type='candle',ylabel='Candle', addplot=apa, style = "nightclouds")






