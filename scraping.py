from bs4 import BeautifulSoup
import requests
import os.path
import nltk 
from nltk import sentiment
from nltk.sentiment import util
from nltk.corpus import stopwords
nltk.download('punkt')
import csv
#from nltk import classifiers
#from nltk.classifiers import NaiveBayesClassifier


response = requests.get("https://www.coindesk.com/binance-acquires-crypto-debit-card-provider-swipe-for-undisclosed-sum")
if not response:
    print("Wrong response: ", response)
else:
    doc = response.text

soup = BeautifulSoup(doc, "html.parser")
#print(soup.prettify)

#title = "hej.txt"
title = soup.find("h1", class_= "heading").text

title += ".txt"
complete_title = os.path.join("D:\Projekat", title)

date = soup.time["datetime"][0:10]
txt_file = open(complete_title, "a")
#txt_file.write(date + " ")

tags = soup.find("section", class_ = "has-media news article-body"). find_all("li")

for tag in tags:    
    if tag.a:
        tag.a.unwrap()
        for childtag in tag.find_all():
            tag.child.unwrap()
    txt_file.write(tag.text + " ")

txt_file.close()


txt_file2 = open(complete_title, "r")
separated_file = [nltk.word_tokenize(t) for t in nltk.sent_tokenize(txt_file2.readlines()[0])]
txt_file3 = open(os.path.join("D:\Projekat", "doneArticles.txt"), "a")

for sentence in separated_file:
    no_stop_sentence = [word for word in sentence if not word in nltk.corpus.stopwords.words('english')]
    nltk.sentiment.util.mark_negation(no_stop_sentence, False, True)
    no_stop_sentence = [word + " " for word in no_stop_sentence]
    txt_file3.writelines(no_stop_sentence)

txt_file3.write("\n")





# print(no_stop_words)
#print(nltk.corpus.stopwords.words('english'))




    
    
print("done")









