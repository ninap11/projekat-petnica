from bs4 import BeautifulSoup
import requests
import os.path
import re
# import nltk 
# from nltk import sentiment
# from nltk.sentiment import util
# from nltk.corpus import stopwords
# nltk.download('punkt')
# import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
# from datetime import datetime 

def background_calculation():
    # here goes some long calculation
    time.sleep(1)

    # when the calculation is done, the result is stored in a global variable
    global result
    result = 42
    result_available.set()



# url = "https://www.ft.com/search?q=bitcoin&page=2&contentType=article&sort=relevance&expandRefinements=true" # + str(i)

# response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
# if not response:
#     print("Wrong response: ", response)
# else:
#     doc = response.text
#     soup = BeautifulSoup(doc, "lxml")
#     # print(soup.prettify) 
#     i =0
#     for li in soup.main.find_all("ul")[8].find_all("li"):
#         link = li.find_all("a")[1]["href"]
#         if link[0] == "/":
#             link = "http://ft.com" + link
#             response2 = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
#             if not response2:
#                 print("wrong response 2 ", response2)
#             else:
#                 article_doc = response2.text
#                 article_soup = BeautifulSoup(article_doc, "html.parser")
#                 article = ""
#                 tag = article_soup.body.div.find_all("div", class_ = "n-layout__row n-layout__row--content")[0].div.find_all(id = "site-content")[0]
#                 print(tag.attrs)
#                 for p in tag.find_all("p"): 
#                     if p.attrs == {}:
#                         article += p.get_text(strip = True)
#                 # if i < 1:
#                 #     print(article)
#                 #     i +=1
                

url = "https://www.coindesk.com/search?q=bitcoin&s=relevant"

# driver = webdriver.Chrome()
# driver.get(url)
# print(driver.page_source)

# System.setProperty("webdriver.chrome.driver","C:\Program Files (x86)\Google\Chrome\Application")
# options.addArguments("user-data-dir= C:\Users\nina\AppData\Local\Google\Chrome\User Data\Default")

# button = div_button.find_element_by_tag_name("button")
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=r'C:\chromedriver_win32\chromedriver.exe')


driver.get(url)
# div_button = driver.find_elements_by_css_selector("#__next > main > section > div > section.page-area-dotted-content > article > div > section > div")                 

# # print(div_button)
# for e in div_button:
#     elem = e
counter = 1
old = False
while counter < 1500 and old == False:
    selector = "#__next > main > section > div > section.page-area-dotted-content > article > div > section > div:nth-child(" + str(counter * 10 + 1) + ") > button"
    try:
        button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
        # print("oce")
    except:
        print("nece")
    # button = driver.find_element_by_css_selector(selector)
    # div_button = driver.find_elements_by_css_selector("#__next > main > section > div > section.page-area-dotted-content > article > div > section > div")
    # print(div_button)
    if counter >= 66:
        for ind in range((counter-1)* 10 + 1, (counter-1)* 10 + 11):
            div_selector = "#__next > main > section > div > section.page-area-dotted-content > article > div > section > div:nth-child(" + str(ind) + ")"
            div =  driver.find_element_by_css_selector(div_selector)
            tag_link =  div.find_element_by_css_selector("div > div.text-content > a:nth-child(2)")
            link = tag_link.get_attribute("href")
            tag_time = div.find_element_by_css_selector("div > div.text-content > div > time")
            date = int(tag_time.text[-4:])
            if date < 2017:
                old = True
            txt = open(r'D:\Projekat\coindesklinks.txt', 'a')
            txt.write(link + "\n")
        
        
    

    button.click()
    counter += 1
    print(counter)
    
        #__next > main > section > div > section.page-area-dotted-content > article > div > section > div:nth-child(11) > button
    
    #__next > main > section > div > section.page-area-dotted-content > article > div > section > div:nth-child(21) > button
    # //*[@id="__next"]/main/section/div/section[2]/article/div/section/div[11]/button
    #__next > main > section > div > section.page-area-dotted-content > article > div > section > div:nth-child(1)
    #__next > main > section > div > section.page-area-dotted-content > article > div > section > div:nth-child(21) > button