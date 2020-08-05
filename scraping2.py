from bs4 import BeautifulSoup
import requests
import os.path
import nltk 
from nltk import sentiment
from nltk.sentiment import util
from nltk.corpus import stopwords
nltk.download('punkt')
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.bloomberg.com/topics/bitcoin")
assert "Python" in driver.title
elem = driver.find_element_by_class_name("load-more-topics load-more-topics--enabled")
elem.clear()
elem.click()
driver.close()

links = []