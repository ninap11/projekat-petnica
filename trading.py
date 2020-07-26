import pandas as pd
import datetime
import math
from scipy import stats

print(stats.spearmanr([1, 2, 3, 4],[1, 3, 2, 5]))


"""
sentiment_dictionary = pd.read_csv(r'D:\Projekat\sentiment.csv').to_dict("records")[0]
del sentiment_dictionary["Unnamed: 0"] 
print(sentiment_dictionary)
current_date = "2020-07-07"
year, month, day = map(int, current_date.split("-"))

sentiment_trend = 0
previous_sentiment = 0
sentiment_mean = 0

N = 10
dates = sentiment_dictionary.keys()
print(datetime.date(2020, 7, 7) - datetime.timedelta(N))
dates = []

for i in range(N):
    dates.append(datetime.date(year, month, day) - datetime.timedelta(N))

for date in dates:
    try:
        current_sentiment = sentiment_dictionary[date]
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

"""