from tradingview_ta import *
import tradingview_ta
import datetime
from datetime import *

print(tradingview_ta.__version__)



nasfut = TA_Handler(
    symbol="NQH2023",
    screener="america",
    exchange="CME_MINI",
    interval=Interval.INTERVAL_1_DAY,
    # proxies={'http': 'http://example.com:8080'} # Uncomment to enable proxy (replace the URL).
)



analysis = nasfut.get_analysis()






print(analysis.time)
print(analysis.indicators["low"])
analysis = nasfut.get_analysis()


# Example output: {"RECOMMENDATION": "BUY", "BUY": 8, "NEUTRAL": 6, "SELL": 3}