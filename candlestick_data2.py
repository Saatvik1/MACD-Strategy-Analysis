#from tvDatafeed import TvDatafeed,Interval
from websocket import create_connection

#install: selenium, websocket, websocket-client

#username = 'Project1234'
#password = 'DAPASSWORD1'



#tv=TvDatafeed(username, password, chromedriver_path=None)
""" 
tv = TvDatafeed()

nas_fut = tv.get_hist(symbol='NQH2023',exchange='CME_MINI',interval=Interval.in_daily,n_bars=22)

nas_fut_5min = tv.get_hist(symbol='NQH2023',exchange='CME_MINI',interval=Interval.in_5_minute,n_bars=90)

print(nas_fut)
print(nas_fut_5min)
"""