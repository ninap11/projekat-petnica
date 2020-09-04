import pickle
import re
import nltk 
from nltk import sentiment
from nltk.sentiment import util
from nltk import classify
from nltk.classify import naivebayes
from nltk.tokenize import RegexpTokenizer
import random


# values_file = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\values test set.txt", "r+", encoding= "utf-8-sig")
# values = values_file.readlines()
# values_file.close()
# values = [v.strip() for v in values]

# print(lines)

def separate_articles(line, mistakes, semicolon, tokenized_article):

    if semicolon == -1:
        mistakes.append(line)
    else:
        article = line[semicolon+1 :] 
        tokenized_article = tokenizer.tokenize(article)
        return tokenized_article

def upper_func(tokenized_article):
    upper_article = []
    for word in tokenized_article:
        word = re.sub(r'[0-9]+', '', word)
        if word != "":
            upper_article.append(word.upper())
    return upper_article

# def no_stopwords_func(article):
#     no_stops_article = [word for word in article if not word.lower() in corpus]
#     return no_stops_article

def feature_func(article):
    article_dict = {word: True for word in article}
    # tup = (article_dict, value)
    return article_dict


# def find_value(line):
#     index = line.index(" ")
#     if index != -1:
#         id_number = line[:index].strip()
#         print(id_number)
#     for l in values:
#         if id_number in l:
#             print("in l")
#             value = l.strip()[-1]
#             if value != -1:
#                 print(value)
#                 return value


txt_file = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\sites\wsj3.txt", "r+", encoding= "utf-8")
lines = txt_file.readlines()
# lines = []
txt_file.close()

classifier_txt = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\classifier.txt", "rb")
classifier = pickle.load(classifier_txt)

tokenized_article = []

# print(values)


mistakes = []
tokenized_articles = []
tokenizer = RegexpTokenizer(r'\w+')
uppercase_articles = []
vocabulary = set()
feature_set = []
id_date = []
no_stop_articles = []
corpus = nltk.corpus.stopwords.words('english')
values = []
old = []
# print(find_value(lines[0]))

length = len(lines)
for i in range(length):
    line = lines[i]
    space = line.find(" ")
    hashtag = line.find("&")

    if space != -1 and hashtag != -1:
        id_num = line[:space]
        # id_numbers.append(id_num
        date = line[space+1:hashtag-1].encode("utf-8").decode("utf-8-sig")
        full = id_num + " " + date
        id_date.append(full)
        print(i)
        try:
            int(date[0:4])
            a = True
        except:
            a = False
        if a and int(date[0:4]) < 2020 and int(date[0:4]) > 2016:

            tokenized_articles.append(separate_articles(line, mistakes, hashtag, []))
            tokenized_articles = [t for t in tokenized_articles if t != None]

        else:
            old.append(id_num)
    else:
        mistakes.append(lines.index(line))
    
# for article in tokenized_articles:
#     no_stop_articles.append(no_stopwords_func(article))
# print(no_stop_articles)
# print(tokenized_articles)

for t in tokenized_articles:
    upper_t = upper_func(t)
    uppercase_articles.append(upper_t)
    # vocabulary.update(upper_t)
# print(uppercase_articles)
# print(vocabulary)

c = 0

for u in uppercase_articles:
    dict_article = feature_func(u)
    id_date[c] += " " + classifier.classify(dict_article) + "\n"    
    c+=1
print(mistakes)

vals = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\sites\wsj values.txt", "w", encoding= "utf-8-sig")
vals.writelines(id_date)
vals.close()
# print(nltk.classify.accuracy(classifier, feature_set))

