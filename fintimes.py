from datetime import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

from selenium.webdriver import Chrome, ChromeOptions

options = ChromeOptions()
options.add_extension(r"D:\Downloads\bypass-paywalls-chrome-master\bypass-paywalls-chrome-master.crx")


counter = 1
o = 1

while counter < 600:
    url = "https://www.ft.com/search?q=bitcoin&page=" + str(counter) + "&contentType=article&dateTo=2017-12-31&dateFrom=2017-01-01&sort=date&expandRefinements=true"

    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    if not response:
        print("Wrong response: ", response)
    else:
        doc = response.text
        soup = BeautifulSoup(doc, "lxml")

        ul = soup.select("#site-content > div > ul > li")
        for li in ul:
            a = li.select_one("div > div > div > div.o-teaser__content > div.o-teaser__heading > a")
            link = a["href"]
            if link[0] == "/":
                link = "https://www.ft.com" + link

            title = a.get_text(strip = True)

            time = li.select_one("div > div > div > div.o-teaser__content > div.o-teaser__timestamp > time")
            
            date = time["datetime"]
            ind = date.index("T")
            date = date[:ind]
            
            # print(link, date, title)
            
            driver = Chrome("C:/chromedriver_win32/chromedriver.exe", options=options)
            driver.get(link)
            article = ""
            try:
                ps = driver.find_elements_by_css_selector("body > section > div > div > div > div:nth-child(1) > div.article__main > article > p")
                for p in ps:
                    article += p.text
                print(ps)
                if ps == []:
                    raise Exception
            except:
                try:
                    ps = driver.find_elements_by_css_selector("#site-content > div.article__content.p402_premium > div.article__content-body.n-content-body.js-article__content-body > p")
                    for p in ps:
                        article += p.text
                except:
                    print("mistake", link)
            full = str(date) + " ; " + title + " ; " + article + "\n"
            # print(full)
            txt = open(r'D:\Projekat\FT.txt', "a", encoding="utf-8")
            txt.write(full)

            o+=1
            print(o)

            driver.close()
            window_before = driver.window_handles[0] 
            driver.switch_to_window(window_before)
            driver.close()
    counter +=1
    print(counter)
