from bs4 import BeautifulSoup
import requests


import csv
# from selenium import webdriver
# from selenium.webdriver.common.by import By
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
counter = 46    

while not old:
    
    # thread = threading.Thread(target=background_calculation)
    # thread.start()
    # result_available.wait()
    # time.sleep(5)

    url = "https://www.coindesk.com/tag/markets-bitcoin/" + str(counter)
    # print(url)
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if not response:
        print("Wrong response: ", response)
    else:

        doc = response.text
        soup = BeautifulSoup(doc, "lxml")
        # print(soup.prettify) 
        o = 0
        tag = soup.body.div.main.section.find_all("div", class_ = "story-stack-chinese-wrapper")[0].div.find_all("section", class_ = "page-area-dotted-content")[0].div.section.find_all("div", class_ = "list-item-wrapper")
            # for t in tag:
            #     print(t["class"])
        for div in tag:
            date = div.time.text
            rdate = str(datetime.strptime(date, "%b %d, %Y").date())
            try:
                if int(date[-4:]) < 2017:
                    old = True
            except:
                print("date error", counter)
            link = "https://www.coindesk.com" + div.find_all("a")[1]["href"]
            title = div.find_all("a")[1]["title"]
            response2 = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
            if not response2:
                print("Wrong response2: ", response2)
            else:
                article_doc = response2.text
                a_soup = BeautifulSoup(article_doc, "lxml")
                article = ""
                
                
                try:
                    
                    am = a_soup.body.div.main.section.div.div.article.find_all("div", class_ = "article-pharagraph")
                    
                    for d in am:
                        
                        article += d.p.get_text(strip = True)
            
                    if article == "":
                        
                    
                        try: 
                            am = a_soup.body.div.main.section.div.div.article.find_all("div", class_ = "classic-body")[0].find_all("p")
                            for d in am:
                                article += d.get_text(strip = True)
                        except:
                            print("mistake", link)
                except:
                    
                    try: 
                        am = a_soup.body.div.main.section.div.div.article.find_all("div", class_ = "classic-body")[0].find_all("p")
                        for d in am:
                            article += d.get_text(strip = True)
                    except:
                        print("mistake", link)
                full = rdate + " ; " + title + " ; " + article + "\n"
                txt = open(r'D:\Projekat\coindesk.txt', 'a', encoding="utf-8")
                txt.write(full)


    print(counter)
    counter+=1
              
