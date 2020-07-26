import csv
import os.path
import nltk
import pandas as pd

csv_dictionary = open(os.path.join('D:\Projekat','Seconddict.csv'), "r", newline = "") #preimenuj dict
reader = csv.reader(csv_dictionary, delimiter=',', quotechar='"')

first_row = list(reader.__next__())
second_row = list(reader.__next__())
third_row = list(reader.__next__())


articles = open(os.path.join('D:\Projekat','doneArticles.txt'), "r")
#print(articles.readlines()[0])



sentiment_dictionary = {}
dates = []
# print("date", date)
for line in articles.readlines():
    print(line)
    date = line[0:10]
    dates.append(date)
    line = str(line)[11:]
    print(line)
    article_sentiment = 0
    text = nltk.sent_tokenize(line)
    for sentence_ in text:
        sentence = nltk.word_tokenize(sentence_)
        sentence_sentiment = 0
        for word in sentence:
            if word[-4:] == "_NEG":
                word = word[:-4]
                print(word)
                try:
                    finder = first_row.index(word.upper())
                    #print("finder", finder, word, second_row[finder], third_row[finder])
                    if int(second_row[finder]) > 0:
                    #    print("sentiment  ", second_row[finder], word)
                        sentence_sentiment -= 1
                    elif int(third_row[finder]) > 0:
                    #    print("sentiment  ", third_row[finder], word)
                        sentence_sentiment += 1
                except:
                    #print("passed  ", word)
                    pass
            else:  
                try:
                    finder = first_row.index(word.upper())
                    #print("finder", finder, word, second_row[finder], third_row[finder])
                    if int(second_row[finder]) > 0:
                    #    print("sentiment  ", second_row[finder], word)
                        sentence_sentiment += 1
                    elif int(third_row[finder]) > 0:
                    #    print("sentiment  ", third_row[finder], word)
                        sentence_sentiment -= 1
                except:
                    #print("passed  ", word)
                    pass
        print("end of sentence", sentence_sentiment)    
        if sentence_sentiment > 0:
            article_sentiment += 1
        elif sentence_sentiment < 0:
            article_sentiment -= 1
    if date in sentiment_dictionary:
        sentiment_dictionary[date] += article_sentiment
    else:
        sentiment_dictionary[date] = article_sentiment

print(dates, sentiment_dictionary)
sentiment_csv = open(os.path.join("D:\Projekat", "sentiment.csv"), "r+", newline = "")
reader_d = csv.DictReader(sentiment_csv)

writer = csv.DictWriter(sentiment_csv, delimiter = ",", quotechar = "'", fieldnames = dates)
# writer.writeheader()
# writer.writerow(sentiment_dictionary)


senti = {"a": "b", "d": "c"}
# sd = pd.DataFrame(sentiment_dictionary, index = [0])
sd = pd.DataFrame(senti, index = [0])
sd.to_csv(r'D:\Projekat\sentiment.csv')
#writer.writerow({"a": "d"})

# for row in reader_d:
    # print(row["a"])

print("done")

sentiment_csv.close()