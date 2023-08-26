<a name="br1"></a> 

**MACD Trading**

**Strategy Analysis**

A case study performed on a simulation of the

MACD strategy applied on the NASDAQ E-mini

futures market.



<a name="br2"></a> 

**What is the significance in analyzing the**

**MACD strategy?**

Over the past couple of years, the futures market has been heating up. More and more

investors are participating in these markets and as a result volatility is on the rise. With more

volatility comes more chances to make money.

The MACD strategy is a popular strategy, one that has stood the test of time and still has a

successful reputation to this day. At the same time, algorithmic and automated trading is on

the rise, not to mention to exploration of AI and it’s efficiency in the market. But with all

these complicated ways to make money in the markets, perhaps one of the oldest and

simplest will be enough. Can it prove to be effective in today’s market, and should it deserve

remain as one of the most popular strategies amongst new and veteran traders.



<a name="br3"></a> 

**Background**

A little background about the MACD strategy. The MACD (moving average convergence/divergence)

is a technical indicator originally used for securities, created by a man named Gerald Appel in the

1970s. It is meant to depict the direction of the momentum of price. To this day, the MACD is an

extremely popular indicator. If you were to search up on youtube "trading indicator", and then sort

by most amount of views, "Most Effective MACD Strategy for Daytrading Crypto, Forex & Stocks

(High Winrate Strategy)" is the third video, with a whopping 2.3 million views. From a more

personal standpoint, a trading youtuber I watched swore by the MACD indicator, saying things like

"oh its so easy" and "anyone can do it". Well if it is, then why doesn't everyone use it? Well its not

that simple actually.



<a name="br4"></a> 

**Background (continued)**

For those who don't know, the MACD and signal lines are calculated by different exponential

moving averages (EMA's), taking the EMA of each candle close since the start of the data set as far

back as possible. Throughout trading, traders observe that certain EMA's under certain timeframes

can be used an indicator of where price will either comeback to, or fall.

For the MACD strategy, it is used as a "momentum" indicator. When the MACD line moves above

the signal line, it is a bullish indicator (bullish usually refers to price going up). When the MACD line

moves below the signal line, it is a bearish (referring to price decreasing) signal. Sounds simple

right? Well thats all it is.



<a name="br5"></a> 

**Establishing Intentions**

To reiterate, the purpose of this analysis/case study is to identify the effectiveness or lack of thereof

of the MACD strategy. In this simulation (to be explained), only the MACD strategy will influence

the buying and selling received by the program.

To identify the effectiveness of it, we will look at the factors that make any trading strategy viable:

Win/Loss ratio, Win percentage, and overall consistency.

A good strategy is a strategy that allows you to win more than lose, and win more often that lose,

and to be able to do that over a longer period of time is also important. So many traders fall into the

trap of big winners and big losers, making nothing or having a negative PnL. Some don’t have

strategies that win often enough. And some win for short periods of time, only to find that it is

ineffective in the long run.



<a name="br6"></a> 

**Data Source**

The data collected is a program run simulation of the MACD. The trade signals are

determined through the regular default MACD requirements. The source of the data being

fed into the formulas are candlestick data provided by yahoo finance (yfinance).

One restriction faced by using this public api is it only allows 60 days worth of data (from

the present date to 60 days in the past). So once the simulation is run, it has 60 days worth

of data and is final. The next day, the simulation would be different by one day.

Example of the simulation being ran is on the next slide.



<a name="br7"></a> 



<a name="br8"></a> 

**Simulation Details**

The candlestick data is collected over 60 days, and is given in 5 minute candlesticks. The simulation was

ran from 4-13-23 until 6-09-23.

The candlestick data is given in the form of a dataframe, indexed by a datetime object.

Using this, we use mplfinance to plot the data, as well as run an algorithm that runs through the data,

finds intersection points in the EMA lines for the MACD (EMA lines calculated by a separate algorithm).

At this point he have a buy/sell colum, time, session, volume, and profit column. This dataframe gets

converted into a csv file and is ready to be analyzed.

The rest of the simulation then shows the visual representation of the trades, having buy and sell

markers, showing the MACD Lines, as well as the candlestick data of price visually.

The trade data collected is undoubtedly accurate, as it was double checked (visually) by a trading

platform that supports the MACD indicator.



<a name="br9"></a> 

**Data Analysis**

The data cleaning process for this dataset was very simple. More or less all I had to do was look for

abnormalities and null values.

For this case study it is more beneficial to include outliers to get a bigger picture of the capabilities

of the strategy. Outliers are important for a trading strategy because it shows you how consistent it

is with and without, and what are the possibilities when you include them.

However, the dataset will be studied with and without the outliers to get a full picture, but for the

early stages I included them.

**For the analysis I used the following: Excel, Pandas, Matplotlib, NumPy, SciPy**



<a name="br10"></a> 

**Data Analysis (continued)**

In order to get a basic understanding of the data I had collected, I decided to organize most

of my filters in terms of the sessions. Meaning trends and findings are mostly classified by

session. This is the best course of action because price action varies greatly throughout the

different sessions.

For instance, RTH Session is the session with the most amount of volume (has the most

active participants), while the one with the least amount is the asia session. Almost always

the session with the least amount of participants means less volatility, which means less

price action and less opportunity for trades. They each have their own recurring events as

well, RTH Session often have certain impactful news that investors keep an eye out.

In summary, each session is unique and must be observed separately.



<a name="br11"></a> 



<a name="br12"></a> 

**Data Analysis (continued)**

In the process of organizing the dataset to get a general view of it, I created different visuals

to give basic information. They were:

Total # of Trades per Session

Median Trade Result per Session

Average Trade Result per Session (we can see the difference between the median and

average, giving an us an idea of what is really affecting the data)

Total PnL per Session

Median Transaction Size per Session



<a name="br13"></a> 



<a name="br14"></a> 



<a name="br15"></a> 



<a name="br16"></a> 



<a name="br17"></a> 



<a name="br18"></a> 

**Data Analysis (continued)**

Notice the big difference between the median trade result and the average trade result in

the RTH Session. The RTH session definitely has large outliers causing that big difference. It

becomes apparent that even though the RTH Session was the only session to have a

positive PnL, it may not be the result of a consistent repetition of trades.

Regardless, it showed that I need to take the RTH Session into careful consideration, as it is

clearly different than the others in a special way, something that I expected due to the nature

of price action during the session.

Many traders solely trade the RTH Session so singling it out will not affect the accuracy of

our conclusion.



<a name="br19"></a> 



<a name="br20"></a> 

**Data Analysis (continued)**

Seeing how bad the PnL was per session (except the RTH Session) and seeing how poor the median trade

was per session, I decided to check the win percentage of each session.

All sessions were less than 50%.

Now thats not the best, that means for every trade made in the simulation, your chances are less than that

of a coin toss. Traders would definitely not like to stake their money on that.

Fortunately, not all strategies are reliant on high win percentages. Even if you win less times than you lose,

as long as you win enough money each time you win, you can out pace the losses. This means checking the

win to loss ratio. To calculate the W:L ratio per session, I took the median winning trade, and took the

median losing trade per session and fount its ratio.

I decided to use the median rather than average because it was shown earlier that the average is skewed to

the higher side. The median will give a better image of the types of trade since it will be in the middle of the

distribution. Here is the summary of the results:



<a name="br21"></a> 

**Data Analysis (continued)**



<a name="br22"></a> 

**Temporary Conclusion**

At this point it seemed like the MACD was completely ineffective in this simulation. But I

decided to test something out. Perhaps the strategy was effective under certain conditions.

So I decided to check it’s effectiveness under various amounts of volume. My reasoning was

to do this was that the MACD seems to be the most effective in the RTH Session, where

there is more volume. Furthermore, to me it seemed as if the RTH Session had more

directional moves with conviction (meaning price moves one way for a purpose). The latter

reason is more anecdotal but it would explain why a momentum indicator would be more

effective.

Of course correlation does not mean causation so I decided to investigate.



<a name="br23"></a> 

**Temporary Conclusion (continued)**

Along with volume filters being applied, I also decided to implement a pseudo stop-loss

function.

In trading a stop loss allows you to exit a trade when you hit a set amount of negative PnL

on a trade (drawdown). This allows traders to manage their drawdown, and gives them an

easier time to make profits to return to a positive PnL.

Basically: “At this point I am wrong about my trade, and there’s no point in losing more

money on it”.

The stop loss filter is applied first since it is the most commonly used method to make a

strategy more effective. The stop loss I applied was all trades below -300 stop at -300. So if

the simulation lost -5000 on a trade it would be turned into a -300 loss instead.



<a name="br24"></a> 



<a name="br25"></a> 



<a name="br26"></a> 

**Stop Loss Implementation Results**

Normally a stop loss would need to be implemented into the simulation directly, but since

the simulation exits and enters trades at the same time, “cutting a trade short” is not against

the simulation rules, and it would result in the same dataset.

Taking a look at the data after applying however, shows drastic improvement. The difference

in profit is 5k greater for three of the sessions, with two of them having ~15k increase in

profits. That is very impressive.

Now lets see what happens when the volume filter was added.



<a name="br27"></a> 



<a name="br28"></a> 



<a name="br29"></a> 

**Volume Filter Results**

The first two graph visually shows little improvement in the ratio count of winning vs losing

trades which high volume. The third graph shows that a filter with low volume filter has

detrimental effects to PnL. The most basic conclusion is that there is a requirement for

volume, but there is no benefit in having above average volume.



<a name="br30"></a> 

**Outlier Testing**

The last step in my analysis was to check the effect of outliers on the total PnL. This is

another measure to see if the longevity of the strategy is good. A strategy that relies on

outliers will most likely fail, whereas one that doesn’t will have consistent and good PnL

gains throughout its use.

To see the effect of outliers I decided to test the PnL when removing trades that fall three,

two, and one standard deviations away from the mean. This is done to see what percent of

trades impact total PnL after normalizing profitable trades.



<a name="br31"></a> 



<a name="br32"></a> 



<a name="br33"></a> 

**Outlier Testing Results**

(All outlier testing was solely tested in the RTH Session, due to its uniqueness)

After taking a look at the effect of the outliers I came up with two visuals. One showing the effect in

PnL when allowing trades above x standard deviations, and the other being the distribution of

profitable trades normalized.

These two visualizations help paint a picture, and they show that past one standard deviation the

PnL greatly increases, and past the second it increases slightly.

In a normal gaussian distribution, one standard deviation above the mean is around 85% of the

curve. However, our data is a little different and skewed so in actuality, only 5 trades are added

when testing the difference between the first and second standard deviations. That would be much

less than the expected 15% remaining amount of trades, further pointing to the conclusion that the

simulated strategy included few but large enough winners to skew PnL, giving it the false sense of

being a profitable strategy.



<a name="br34"></a> 

**Analysis Conclusion**

After thorough analysis of the results of my simulation, the MACD strategy, if left to itself in

an automated fashion is not a profitable trading strategy. For all of the sessions it does not

meet the basic W:L ratio, and does not have a good winning percentage. When

incorporating a stop loss and volume filter, at first glance it seems to have potential.

Undoubtedly, implementing the stop loss would help the win to loss ratio, but it does not

help the win percentage. On top of that, after checking the effect of outliers on profits, it was

found that a majority of the difference in profit between no SL and SL is due to 6 trades. An

underwhelming number that shows that outliers have a major impact, and cannot be

considered to be a positive sign for the MACD being a consistent strategy.



<a name="br35"></a> 

**Next Steps**

So what now? I believe the MACD can go under more testing. I believe that applying more restrictions on the

simulation will give us a better understanding of when and where the MACD strategy can excel. I believe that more

testing is needed to find its strength and weakness. Examples of this can be finding where does it’s win percentage

drop (ie. when trades are taken at value area high/low, point of control, VWAP, etc…). Perhaps combined with

another indicator the quality of trades will improve. Perhaps it is only effective during trend days, or maybe range

days (these are classifications of the type of price action traders experience during the day).

For anyone thinking of using the MACD to start automated trading, I recommend the following:

Test the algorithm extensively: test it under various conditions and parameters

Implement a stop-loss

Restrict it to one or two sessions, including the RTH Session.

Test the MACD with a set take profit, to reduce the chances of results being skewed by large winners.



<a name="br36"></a> 

**Next Steps (continued)**

In my next simulation I plan on implementing my recommendations to create a more niche

environment. I will also try to collect more data parameters, specifically VAH/VAL, POC, and

VWAP trades, trend day and range day trades. This will allow me to gather a greater insight

into the kind of conditions that allow the strategy to excel.

The notebook used in this analysis is prepared to conduct the same analysis on any dataset

shaped the same way.

This project has put into perspective to me how difficult automate trading can be, and how

many complex elements there are. I hope to gain more insight on this topic in the future, and

maybe collaborate with anyone else who is also interested.



<a name="br37"></a> 

**Thank You!!!**

