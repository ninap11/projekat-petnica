
# i'm using this to search for a given word in the loughran and mcdonald dictionary
# and calculate the sentiment of all articles
# 
#


import csv
import os.path
import nltk
import pandas as pd


csv_dictionary = open(os.path.join('D:\Projekat','Seconddict.csv'), "r", newline = "") #preimenuj dict 
reader = csv.reader(csv_dictionary, delimiter=',', quotechar='"') #ucitavamo recnik da bi nasli rec


first_row = list(reader.__next__()) #prvi red je sa recima
second_row = list(reader.__next__()) #drugi sa neg sentimentom
third_row = list(reader.__next__()) #treci sa pozitivnim


articles = open(os.path.join('D:\Projekat','doneArticles.txt'), "r") #svaka linija je jedan clanak
# print(articles.readlines()[0])


sentiment_dictionary = {}
dates = []
# print("date", date)



for line in articles.readlines():

    # print(line)
    date = line[0:10]
    dates.append(date)

    line = str(line)[11:]
    # print(line)

    article_sentiment = 0 #sentiment clanka
    text = nltk.sent_tokenize(line) #pravimo niz recenica (stringova) u clanku

    for sentence_ in text:

        sentence = nltk.word_tokenize(sentence_) #pravimo niz reci
        sentence_sentiment = 0 #sentiment recenice

        for word in sentence:
            if word[-4:] == "_NEG":
                word = word[:-4]
                # print(word)
                # ukoliko je rec negirana racunamo suprotni sentiment

                try:
                    finder = first_row.index(word.upper()) # trazimo  index reci u recniku

                    if int(second_row[finder]) > 0: #nisam sigurna za ovo
                        sentence_sentiment -= 1  
                    elif int(third_row[finder]) > 0:
                        sentence_sentiment += 1

                except:
                    print("passed  ", word)
            
            else:  
                try:
                    finder = first_row.index(word.upper())

                    if int(second_row[finder]) > 0:
                        sentence_sentiment += 1
                    elif int(third_row[finder]) > 0:
                        sentence_sentiment -= 1
                
                except:
                    print("passed  ", word)

        #print("end of sentence", sentence_sentiment)    
        
        if sentence_sentiment > 0:
            article_sentiment += 1
        elif sentence_sentiment < 0:
            article_sentiment -= 1
    
    if date in sentiment_dictionary:
        sentiment_dictionary[date] += article_sentiment #uvecavamo ukupni sentiment tog dana za sentiment clanka
    else:
        sentiment_dictionary[date] = article_sentiment

# print(dates, sentiment_dictionary)


sentiment_csv = open(os.path.join("D:\Projekat", "sentiment.csv"), "r+", newline = "")
writer = csv.DictWriter(sentiment_csv, delimiter = ",", quotechar = "'", fieldnames = dates)


sd = pd.DataFrame(sentiment_dictionary, index = [0]) #upisujemo sentiment u csv 
sd.to_csv(r'D:\Projekat\sentiment.csv')

sentiment_csv.close()

print("done")