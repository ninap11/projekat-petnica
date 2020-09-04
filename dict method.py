# i'm using this to search for a given word in the loughran and mcdonald dictionary
# and calculate the sentiment of all articles
# 
#


import csv
import pickle
import re

import nltk 
from nltk import sentiment
from nltk.sentiment import util
# nltk.download("stopwords")
# nltk.download('punkt')
# import csv
from nltk import classify
from nltk.classify import naivebayes
from nltk.tokenize import RegexpTokenizer
import random
# import pandas as pd

def separate_articles(line, mistakes, tokenized_article):
    semicolon_index = line.find(";")
    if semicolon_index == -1:
        mistakes.append(line)
    else:
        article = line[semicolon_index+1 :] 
        tokenized_article = tokenizer.tokenize(article)
        return tokenized_article

def upper_func(tokenized_article):
    upper_article = []
    for word in tokenized_article:
        word = re.sub(r'[0-9]+', '', word)
        if word != "":
            upper_article.append(word.upper())
    return upper_article

def find_value(line):
    index = line.index(" ")
    if index != -1:
        id_number = line[:index].strip()
        print(id_number)
    for l in values:
        if id_number in l:
            # print("in l")
            value = l.strip()[-1]
            if value != -1:
                print(value)
                return value


def no_stopwords_func(article):
    no_stops_article = [word for word in article if not word.lower() in corpus]
    return no_stops_article


txt_file = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\test set.txt", "r+", encoding= "utf-8-sig")
lines = txt_file.readlines()
# lines = []
txt_file.close()


values_file = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\values test set.txt", "r+", encoding= "utf-8-sig")
values = values_file.readlines()
values_file.close()
values = [v.strip() for v in values]
# values = []


tokenized_article = []

mistakes = []
tokenized_articles = []
tokenizer = RegexpTokenizer(r'\w+')
uppercase_articles = []
vocabulary = set()
feature_set = []
id_numbers_a = []
no_stop_articles = []
corpus = nltk.corpus.stopwords.words('english')



csvfile = open(r'C:\Users\Bratislav\Desktop\petnica projekat\data\csv\Seconddict.csv', newline = '')
reader = csv.reader(csvfile, delimiter=',', quotechar='"') #ucitavamo recnik da bi nasli rec


first_row = reader.__next__() #prvi red je sa recima
second_row = reader.__next__()#drugi sa neg sentimentom
third_row = reader.__next__() #treci sa pozitivnim


# articles = open(os.path.join('D:\Projekat','doneArticles.txt'), "r") #svaka linija je jedan clanak
# print(articles.readlines()[0])



length = len(lines)
for i in range(length):
    line = lines[i]
    if line.index(" ") != -1:
        id_num = line[:line.index(" ")]
        id_numbers_a.append(id_num)
    else:
        mistakes.append(lines.index(line))
    tokenized_articles.append(separate_articles(line, mistakes, []))
    tokenized_articles = [t for t in tokenized_articles if t != None]

# for article in tokenized_articles:
#     no_stop_articles.append(no_stopwords_func(article))
# print(no_stop_articles)
# print(tokenized_articles)

for t in tokenized_articles:
    upper_t = upper_func(t)
    uppercase_articles.append(upper_t)
    # vocabulary.update(upper_t)

o = 0
n=0
p = 0
# print(first_row)

for article in uppercase_articles:
    if o <1:
        for word in article:
            try:
                index = first_row.index(word)
                if int(second_row[index]) != 0:
                    print(word)
                    n += 1
                elif int(third_row[index]) != 0:
                    print(word)
                    p += 1
                
            except:
                print(word)
        o+=1
        
print(n, p)        
    

        


# sentiment_dictionary = {}
# dates = []
# print("date", date)



# for line in articles.readlines():

#     # print(line)
#     space = line.index(" ")
#     # if space != -1:
#     #     date = line[space:space+10]
#     #     dates.append(date)
    
#     line = str(line)[11:]
#     # print(line)

#     article_sentiment = 0 #sentiment clanka
#     text = nltk.sent_tokenize(line) #pravimo niz recenica (stringova) u clanku

#     for sentence_ in text:

#         sentence = nltk.word_tokenize(sentence_) #pravimo niz reci
#         sentence_sentiment = 0 #sentiment recenice

#         for word in sentence:
#             if word[-4:] == "_NEG":
#                 word = word[:-4]
#                 # print(word)
#                 # ukoliko je rec negirana racunamo suprotni sentiment

#                 try:
#                     finder = first_row.index(word.upper()) # trazimo  index reci u recniku

#                     if int(second_row[finder]) > 0: #nisam sigurna za ovo
#                         sentence_sentiment -= 1  
#                     elif int(third_row[finder]) > 0:
#                         sentence_sentiment += 1

#                 except:
#                     print("passed  ", word)
            
#             else:  
#                 try:
#                     finder = first_row.index(word.upper())

#                     if int(second_row[finder]) > 0:
#                         sentence_sentiment += 1
#                     elif int(third_row[finder]) > 0:
#                         sentence_sentiment -= 1
                
#                 except:
#                     print("passed  ", word)

#         #print("end of sentence", sentence_sentiment)    
        
#         if sentence_sentiment > 0:
#             article_sentiment += 1
#         elif sentence_sentiment < 0:
#             article_sentiment -= 1
    
#     if date in sentiment_dictionary:
#         sentiment_dictionary[date] += article_sentiment #uvecavamo ukupni sentiment tog dana za sentiment clanka
#     else:
#         sentiment_dictionary[date] = article_sentiment

# # print(dates, sentiment_dictionary)


# sentiment_csv = open(os.path.join("D:\Projekat", "sentiment.csv"), "r+", newline = "")
# writer = csv.DictWriter(sentiment_csv, delimiter = ",", quotechar = "'", fieldnames = dates)


# sd = pd.DataFrame(sentiment_dictionary, index = [0]) #upisujemo sentiment u csv 
# sd.to_csv(r'D:\Projekat\sentiment.csv')

# sentiment_csv.close()

# print("done")