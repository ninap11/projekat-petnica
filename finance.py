#finance

import yfinance as yf
import os.path
import csv

articles = open(os.path.join("D:\Projekat", "articles.txt"), "r")
dates = []
for line in articles:
    dates.append(line[0:10])
print(dates)


btc = yf.Ticker("BTC-USD")
#print(btc.info)
data = yf.download("BTC-USD",start='2020-07-07', end='2020-07-08')
prices_csv = open(os.path.join("D:\Projekat", "shares.csv"), "w", newline = "")
writer = csv.writer(prices_csv, delimiter=',', quotechar='"')
c = 0
for date in dates:
    opening_price = list(data["Open"])[c]
    closing_price = list(data["Close"])[c]
    row = [date, opening_price, closing_price]
    writer.writerow(row)
    c+=1



print("done")
