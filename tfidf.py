import pickle
import re
import math
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
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

txt_file = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\test set.txt", "r+", encoding= "utf-8-sig")
lines = txt_file.readlines()
# lines = []
txt_file.close()

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



def lemma_func(article, lemmatized):
    for word in article:
        l = lemmatizer.lemmatize(word)
        lemmatized.append(stemmer.stem(l))
    return lemmatized 

def tfidf_func(word, article, articles, idfs, processed):
    # print("log", math.log())

    counter2 = 0
    if word not in processed:
        processed.add(word)
        for vocabulary in vocabularies:
            if word in vocabulary:
                # print("it is")
                counter2 += 1
        df = counter2 / len(articles)
        idf = math.log(len(articles) / (counter2))  

    else:
        idf = idfs[word]
        df = dfs[word]
    counter = article.count(word)
    tf = counter / len(article)
    tfidf = tf * idf
    # tfs[word] = tf
    # tfidf[c][word] = tf * idf 
        # try:
        #     if tf * idf != 0 and idf < 0.0033 and counter2 > 1 and df > 0.7:
        #         article2.append(word)

        # except:
        #     pass
    
    # new_articles.append(article2)
        # print(word, tf, idf, counter2, len(articles))
    return (tf, idf, tfidf, df, counter2)
                
        

tokenized_article = []

mistakes = []
tokenized_articles = []
tokenizer = RegexpTokenizer(r'\w+')
uppercase_articles = []
lemmatized_articles = []

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

vocabulary = set()
feature_set = []
id_numbers_a = []
no_stop_articles = []
corpus = nltk.corpus.stopwords.words('english')
# print(find_value(lines[0]))
tfs = {}
idfs = {}
dfs = {}
processed = set()
length = len(lines)
tfidfs = [{} for i in range(length)]
v = set()
vocabularies = [set() for i in range(length)]

for i in range(length):
    line = lines[i]
    if line.index(" ") != -1:
        id_num = line[:line.index(" ")]
        id_numbers_a.append(id_num)
    else:
        mistakes.append(lines.index(line))
    tokenized_articles.append(separate_articles(line, mistakes, []))
    tokenized_articles = [t for t in tokenized_articles if t != None]


# print(no_stop_articles)
# print(tokenized_articles)
for article in tokenized_articles:
    lemmatized_articles.append(lemma_func(article, []))

c = 0 

for s in range(2):
    print(vocabularies[s])


for t in lemmatized_articles:
    upper_t = upper_func(t)
    uppercase_articles.append(upper_t)
    vocabularies[c].update(upper_t)
    print(vocabularies[c])
    c+=1

new_articles = []


count = 0
av_idf = 0
# print(vocabularies)

for article in uppercase_articles:
    processed_ = set()
    new_article = []
    for word in article:
        tf, idf, tfidf, df, counter2 = tfidf_func(word, article, uppercase_articles, idfs, processed_)
        print(tf, idf, tfidf, df, counter2)
        if tfidf != 0.0 and counter2 > 0 and df < 0.8:
            new_article.append(word)
            print("appended")
        tfs[word] = tf
        idfs[word] = idf
        tfidfs[count][word] = tfidf
        dfs[word] = df
    # print(count)++
    new_articles.append(id_numbers_a[count] + " " + " ".join(new_article) + "\n" )
    count+=1
    
print(new_articles)


# a = set()
# b = [1, 2, 3]
# a.update(b)
# print(a)
print(length)

# print(tfidf)

pik = open(r"C:\Users\Bratislav\Desktop\petnica projekat\data\new test articles 7.txt", "w", encoding= "utf-8-sig")
pik.writelines(new_articles)

print("m", mistakes)
# print(uppercase_articles)
# print(vocabulary)
