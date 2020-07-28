# calculates sentiment mean and trend and performs trading according to the strategies


import pandas as pd
import datetime
import math
from scipy import stats



sentiment_dictionary = pd.read_csv(r'D:\Projekat\sentiment.csv').to_dict("records")[0] #keys are dates, values are sentiments
del sentiment_dictionary["Unnamed: 0"] 
# print(sentiment_dictionary)


current_date = "2020-07-07" #temporary, will start on jan 1 2017
year, month, day = map(int, current_date.split("-"))


sentiment_trend = 0
previous_sentiment = 0
sentiment_mean = 0

N = 10 #temporary, imace razlicite vrenosti koje ce biti uporedjivane

# dates = sentiment_dictionary.keys()    sta je ovo
# print(datetime.date(2020, 7, 7) - datetime.timedelta(N))
dates = [] # datumi koji se uzimaju u obzir pri racunanju sentiment trend i shocka
sentiments = [] #sentimenti tih datuma, ovo je za spirmanovu korelaciju

stocks = [] #napravi da se uzima za datum


for i in range(N):
    dates.append(datetime.date(year, month, day) - datetime.timedelta(N))


for date in dates:
    try:
        current_sentiment = sentiment_dictionary[date]
        sentiments.append(current_sentiment)

        sentiment_trend += sentiment - previous_sentiment
        previous_sentiment = sentiment

        sentiment_mean += current_sentiment

    except:
        print("No sentiment on ", date)
    
sentiment_mean = sentiment_mean / N
sum_of_differences = 0

for date in dates:
    try:
        current_sentiment = sentiment_dictionary[date]
        sum_of_differences += (current_sentiment - sentiment_mean)**2
    except:
        print("No sentiment on ", date)
    

sentiment_deviation = math.sqrt(sum_of_differences / N)
sentiment_shock = (current_sentiment - sentiment_mean) / sentiment_deviation 



spear_rank = stats.spearmanr(sentiments, stocks)
i = spear_rank.index(max(spear_rank))
N = dates[i]



trend_lower_percentile = 10.0  #the percentiles we are going to be backtesting with, these ones are temporary
trend_higher_percentile = 90.0 

trend_values = [] #array of values of sentiment trend
# trend_percentile = stats.percentileofscore(trend_values, sentiment_trend) #percentile of sentiment trend in the array

trend_stocks = 0 #pocinjemo bez bitcoina


if trend_percentile < trend_lower_percentile:
    trend_stocks -= 1 #prodajemo
elif trend_percentile > trend_higher_percentile:
    trend_stocks += 1 #kupujemo
     
shock_lower_percentile = 10.0  
shock_higher_percentile = 90.0

shock_values = [] #array of values of sentiment shock
# shock_percentile = stats.percentileofscore(shock_values, sentiment_shock) #same

if shock_percentile < shock_lower_percentile:
    shock_stocks -= 1 #prodajemo
elif shock_percentile > shock_higher_percentile:
    shock_stocks += 1 #kupujemo
     