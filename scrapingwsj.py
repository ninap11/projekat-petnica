from datetime import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

from selenium.webdriver import Chrome, ChromeOptions

options = ChromeOptions()
options.add_extension(r"D:\Downloads\bypass-paywalls-chrome-master\bypass-paywalls-chrome-master.crx")


counter = 6
old = False
o = 1
txt = open(r'D:\Projekat\WSJmistake.txt', "r", encoding="utf-8")
lines = txt.readlines()
while not old:
    # url = "https://www.wsj.com/search/term.html?KEYWORDS=bitcoin&page=" + str(counter)

    # # driver = Chrome("C:/chromedriver_win32/chromedriver.exe", options=options)
    # response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    # if not response:
    #     print("Wrong response: ", response)
    # else:
    #     doc = response.text
    #     soup = BeautifulSoup(doc, "lxml")
    #     ul = soup.select("#search-results > div > div > ul > li")
    #     for li in ul:
    #         a = li.select_one("div > div > h3 > a")
    #         link = a["href"]
    #         if link[0] == "/":
    #             link = "https://www.wsj.com" + link
    #         title = a.get_text()
    #         # print(link, title)
    #         if o < 2:
    try:     
        driver = Chrome("C:/chromedriver_win32/chromedriver.exe", options=options)
        link = lines[counter]
        # link = "https://www.wsj.com/articles/federal-authorities-arrest-suspect-in-twitter-hack-11596223550?mod=searchresults&page=1&pos=14"
        driver.get(link)
        article = ""
        title = driver.find_element_by_css_selector("#main > header > div:nth-child(2) > div > h1").text
        print(title)
        date_text = driver.find_element_by_css_selector("#wsj-article-wrap > div.clearfix.byline-wrap > time").text[:-6]
        # print(date_text)


        try:
            try:
                date = datetime.strptime(date_text, "%b. %d, %Y %I:%M").date()
            except:
                date = datetime.strptime(date_text, "%B %d, %Y %I:%M").date()
        except:    
            date_text = date_text[:-4] + "0" + date_text[-4:]   
            if date_text[0] == "U" or date_text[0] == "u":
                date_text = date_text[8:]
            try:
                date = datetime.strptime(date_text, "%b. %d, %Y %I:%M").date()
            except:
                date = datetime.strptime(date_text, "%B %d, %Y %I:%M").date()




        if date.year < 2017:
            old = True

        ps = driver.find_elements_by_css_selector("#wsj-article-wrap > div.article-content > p")
        for p in ps:
            article += p.text
        pay_ps = driver.find_elements_by_css_selector("#wsj-article-wrap > div.article-content > div > p")
        for p in pay_ps:
            article += p.text

        full = str(date) + " ; " + title + " ; " + article + "\n"
        # print(full)
        txt = open(r'D:\Projekat\WSJ.txt', "a", encoding="utf-8")
        txt.write(full)
    except:
        print("mistake", link, o)
        #     txt = open(r'D:\Projekat\WSJmistake.txt', "a", encoding="utf-8")
        #     txt.write(link)
        o+=1





    driver.close()
    window_before = driver.window_handles[0] 
    driver.switch_to_window(window_before)
    driver.close()
    print(counter)
    counter+=1
    # driver.close()

