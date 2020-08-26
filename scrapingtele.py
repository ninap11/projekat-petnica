from bs4 import BeautifulSoup
import requests


import csv
from selenium import webdriver
# from selenium.webdriver.common.by 
# import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime 
# import threading
# import time

# result = None
# result_available = threading.Event()


# def background_calculation():
#     time.sleep(5)
#     global result
#     result = 66
#     result_available.set()

old = False
# while i < 2 and not old:
#     print(i)
counter = 211    


while not old:

    driver = webdriver.Chrome()
    url = "https://cointelegraph.com/search?query=bitcoin&page=" + str(counter)
    driver.get(url)
    # response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
     
    soup = BeautifulSoup(driver.page_source, "lxml")
    # print(soup.prettify) 
    o = 0
    tag = soup.body.main.find("div", id = "main").section.div.div.find_all("div", class_ = "results row boxed")[0].div.find_all("div", class_ = "row result")#.section.find_all("div", class_ = "list-item-wrapper")
        # for t in tag:
        #     print(t["class"])
    for t in tag:
        link = t.h2.a["href"]
        if link[26:35] != "explained":
            title = t.h2.a.get_text(strip = True)
            # print(title)
            response2 = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
            if not response2:
                print("Wrong response2: ", response2)
            else:
                article_doc = response2.text
                a_soup = BeautifulSoup(article_doc, "lxml")
                article = ""
                date = ""
                try:
                    tag2 = a_soup.body.div.main.div.article.find_all("div", class_ = "post-content")[0].find_all("p")
                    for p in tag2:
                        article += p.get_text(strip = True)
                    date = a_soup.body.div.main.div.article.time["datetime"]
                    if int(date[0:4]) < 2017:
                        old = True 
                    # if o <1:
                    #     print(article)
                    #     o += 1
                except:
                    print("mistake", link)
                full = date + " ; " + title + " ; " + article + "\n"
                txt = open(r'D:\Projekat\cointelegraph.txt', "a", encoding="utf-8")
                txt.write(full)
                # for p in tag2:
                #     if o < 1:
                #         print(p.text)
                #         o+=1
    print(counter)
    counter+=1
    driver.close()
