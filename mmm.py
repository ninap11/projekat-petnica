from bs4 import BeautifulSoup
import requests
import os.path
import nltk 
from nltk import sentiment
from nltk.sentiment import util
from nltk.corpus import stopwords
nltk.download('punkt')
import csv



response = requests.get("https://www.coindesk.com/search?q=bitcoin&s=relevant")
if not response:
    print("Wrong response: ", response)
else:
    doc = response.text

soup = BeautifulSoup(doc, "html.parser")

txt = open(os.path.join("D:\Projekat", "marija.txt"), "w+")
txt.writelines(soup.prettify())
print("done")