from time import time
import candlestick_data2

#MACD is 12EMA - 26EMA, and the signal line is the 9EMA (nEMA)
class MACD:
    def __init__(self, timeframe, tsEMA, twEMA, nEMA):
        self.timeframe = timeframe
        self.tsEMA = tsEMA
        self.twEMA = twEMA
        self.nEMA = nEMA

    def create():
        pass

# [2 ÷ (number of observations + 1)]. For a 20-day moving average, the multiplier would be [2/(20+1)]= 0.0952.
# Finally, the following formula is used to calculate the current EMA: 
# EMA = Closing price x multiplier + EMA (previous day) x (1-multiplier)

#To calculate the EMA, we will have to make a recurseive function going back into the beginning of time that we would disclose.

#To get the data we would need, I am thinking of having.... a global variable in this file that will have four extra columns
#in addition to the the previous nasfut panda set. 
#The four extra columns will be the 9EMA, 12EMA, 26EMA, MACD Line.

#When we create an EMA, we go through the data set, append the ema values as we go. THen our EMA object will have 
#have the pandas column of that EMA, that is the data the object represents. 

#MACD object will have all 4 columns appended to one data set.

class EMA:
    def __init__(self, movingperiod, timeframe):
        pass

    def createNineEMA():
        pass

    def createTwelveEMA():
        pass

    def createTwentySixEMA():
        pass


