# import os.path
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



txt_file = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\test set.txt", "r+", encoding= "utf-8-sig")
lines = txt_file.readlines()
# lines = []
txt_file.close()



values_file = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\values test set.txt", "r+", encoding= "utf-8-sig")
values = values_file.readlines()
values_file.close()
values = [v.strip() for v in values]


# print(lines)

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

def no_stopwords_func(article):
    no_stops_article = [word for word in article if not word.lower() in corpus]
    return no_stops_article

def feature_func(article):
    article_dict = {word: True for word in article}
    # tup = (article_dict, value)
    return article_dict



def find_value(line):
    index = line.index(" ")
    if index != -1:
        id_number = line[:index].strip()
        print(id_number)
    for l in values:
        if id_number in l:
            print("in l")
            value = l.strip()[-1]
            if value != -1:
                print(value)
                return value

tokenized_article = []

# print(values)


mistakes = []
tokenized_articles = []
tokenizer = RegexpTokenizer(r'\w+')
uppercase_articles = []
vocabulary = set()
feature_set = []
id_numbers_a = []
no_stop_articles = []
corpus = nltk.corpus.stopwords.words('english')
# print(find_value(lines[0]))

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

for article in tokenized_articles:
    no_stop_articles.append(no_stopwords_func(article))
# print(no_stop_articles)
# print(tokenized_articles)

for t in no_stop_articles:
    upper_t = upper_func(t)
    uppercase_articles.append(upper_t)
    vocabulary.update(upper_t)
# print(uppercase_articles)
# print(vocabulary)

c = 0

for u in uppercase_articles:
    art = feature_func(u)
    tup = (art, find_value(lines[c]))
    feature_set.append(tup)
    c+=1
classifier_txt = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\classifier no stops.txt", "rb")
classifier = pickle.load(classifier_txt)


print(nltk.classify.accuracy(classifier, feature_set))