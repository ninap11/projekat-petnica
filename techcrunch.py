from datetime import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

from selenium.webdriver import Chrome, ChromeOptions

options = ChromeOptions()
options.add_extension(r"D:\Downloads\bypass-paywalls-chrome-master\bypass-paywalls-chrome-master.crx")


counter = 1
o = 1
while True:
    
    url = "https://search.techcrunch.com/search;_ylt=A0PDsBt9cEBfu_MAJHGnBWVH;_ylu=X3oDMTEzajVvczlrBGNvbG8DYmYxBHBvcwMxBHZ0aWQDBHNlYwNwYWdpbmF0aW9u?p=bitcoin&pz=10&fr=techcrunch-s&bct=0&b=" + str(counter) + "1&pz=10&bct=0&xargs=0"
    driver = Chrome("C:/chromedriver_win32/chromedriver.exe", options=options)
    driver.get(url)

    ul = driver.find_elements_by_css_selector("#web > ol > li > div > ul > li")
    link = ""
    # print(ul)
    for li in ul:

        try:
            a = li.find_element_by_tag_name("a")
            title = a.get_attribute("title")
            link = a.get_attribute("href")
            # print(a.get_attribute("cbdeuweduewfbweffr"), "aaaa")
            # print(link) 

        except:
            print("mistake", counter)
        # print(link)
        if link != "":
            print(link)
            driver2 = Chrome("C:/chromedriver_win32/chromedriver.exe", options=options)
            driver2.get(link)
            try:
                ps = driver2.find_elements_by_css_selector("#tc-main-content > div > div > div > article.article-container.article--post > div:nth-child(2) > div:nth-child(2) > div.article-content > p")
                
                article = ""
                
                for p in ps:
                    article += p.text
                divs = driver2.find_elements_by_css_selector("#tc-main-content > div > div > div > article.article-container.article--post > div:nth-child(2) > div:nth-child(2) > div.article-content > div")

                for div in divs:
                    article += div.text
                    # for elem in div.find_elements_by_css_selector("*"):
                    #     print("aaaaaa", elem.text)
                    #     article+= elem.text
                try:
                    time = driver2.find_element_by_css_selector("#tc-main-content > div > div > div > article.article-container.article--post > div:nth-child(2) > div:nth-child(1) > header > div.article__byline-wrapper > div.article__byline > span > time")    
                except:
                    time = driver2.find_element_by_css_selector("#tc-main-content > div > div > div > article.article-container.article--post > div:nth-child(2) > div:nth-child(1) > header > div.article__byline-wrapper > div.article__byline > span.article__byline__meta > time")    

                date = time.get_attribute("datetime")
                ind = date.index("T")
                date = date[:ind]
                
                # print(article, date, title)
                
                full = str(date) + " ; " + title + " ; " + article + "\n"
                # print(full)
                txt = open(r'D:\Projekat\TC.txt', "a", encoding="utf-8")
                txt.write(full)
            except:
                print("mistake", link)

            o +=1
            driver2.close()
            window_before = driver2.window_handles[0] 
            driver2.switch_to_window(window_before)
            driver2.close()
            

    driver.close()
    window_before = driver.window_handles[0] 
    driver.switch_to_window(window_before)
    driver.close()
            
    counter += 1
    print(counter)