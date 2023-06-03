from time import time
import datetime as dt
import re 


start = dt.datetime(2023,1,3)
end = dt.datetime(2023,1,24)
numDays = end - start
print(numDays)
numDays = str(numDays)
numDays = re.search(r'\d+', numDays).group()
print(numDays)


#MACD is 12EMA - 26EMA, and the signal line is the 9EMA (nEMA)
class MACD(object):
    twEMA = []
    tsEMA = []
    signal = [] #signal is 9EMA OF the MACD LINE 
    macdLine = []

    def create_macd(self, tsEMA, twEMA, nEMA, candlestick_record):
        #MACD.tsEMA = tsEMA
        #MACD.twEMA = twEMA
        #MACD.nEMA = nEMA
        tsObj = EMA(tsEMA, 1, candlestick_record)
        twObj = EMA(twEMA, 1, candlestick_record)
        #nObj = EMA(nEMA, 1, candlestick_record)

        self.twEMA = twObj.createXEMA(candlestick_record)
        self.tsEMA = tsObj.createXEMA(candlestick_record)
        #self.nEMA = nObj.createXEMA(candlestick_record)

        #self.signal = self.nEMA[tsEMA-nEMA:]
        #self.tsEMA = self.tsEMA[tsEMA:]
        self.twEMA = self.twEMA[tsEMA-twEMA:]

        for i in range(len(self.tsEMA)):
            self.macdLine.append(self.twEMA[i] - self.tsEMA[i])

        nObj = EMA(nEMA, 1, self.macdLine)
        self.signal = nObj.createXEMA(self.macdLine)

        self.macdLine = self.macdLine[len(self.macdLine)-len(self.signal):]

        
        pass

    def create():
        pass

# [2 ÷ (number of observations + 1)]. For a 20-day moving average, the multiplier would be [2/(20+1)]= 0.0952.
# Finally, the following formula is used to calculate the current EMA: 
# EMA = Closing price x multiplier + EMA (previous day) x (1-multiplier)

#To calculate the EMA, we will have to make a recursive function going back into the beginning of time that we would disclose.

#To get the data we would need, I am thinking of having.... a global variable in this file that will have four extra columns
#in addition to the the previous nasfut panda set. 
#The four extra columns will be the 9EMA, 12EMA, 26EMA, MACD Line.

#When we create an EMA, we go through the data set, append the ema values as we go. THen our EMA object will have 
#have the pandas column of that EMA, that is the data the object represents. 

#MACD object will have all 4 columns appended to one data set.

#__init__(20, 5min, [])
class EMA:
    def __init__(self, movingperiod, timeframe, EMARecord):
        self.movingperiod = movingperiod
        self.timeframe = timeframe
        self.EMARecord = EMARecord
        pass

    def calcEMA(self, TPrice, YEma, day, smoothing = 2):
        emaVal = (TPrice * (smoothing / (1+day))) + (YEma * (1-((smoothing / (1+day)))))

        return emaVal

    def createXEMA(self, close_colunm):
        #start from the beginning of the contract period (start of data passed)
        # contractStart and contractEnd tell the start and end of the market contracts we are looking at 
        # data = data[['open','high','low','close']]




        Xema = [0]
        #close_colunm = CC.data['close']

        #calculate the ema based on time period X (20 ema means self.timeframe = 20)
        #firstEma is start of EMA, or the entities SMA. 

        firstEMA = 0
        for i in range(self.movingperiod):
            #find some of first x days
            firstEMA += close_colunm[i]

        
        firstEMA = firstEMA / self.movingperiod   #finalize fist EMA calc
        Xema[0] = firstEMA
        i = 1
        day = self.movingperiod
        for close_data in close_colunm:
            if(day != 0):    #iterate though close_data we already accounted for in the sma
                day = day - 1 
            else:            #iterate through rest
                #roundedVal = self.calcEMA(close_data, Xema[i-1], self.movingperiod)

                Xema.append(round((self.calcEMA(close_data, Xema[i-1], self.movingperiod)), 2))   #add to EMA list
                i = i + 1

        #now at this point XEMA is populated with all the EMA values from start to finish 


        
        self.EMARecord = Xema 

        #self.movingperiod
        return Xema


    


