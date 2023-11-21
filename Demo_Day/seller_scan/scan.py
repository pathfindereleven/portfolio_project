import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import time
import os
import csv
seller = input("what is the seller name?")
pages_input = input("How many pages?")
pages = int(pages_input)
price_list = []
browser = Browser('chrome')
url = 'https://shop.tcgplayer.com/sellers'
browser.visit(url)

 # add input
seller_list = [seller, 'xyz', 'abc']
browser.fill('SellerName', seller)
browser.find_by_xpath('//*[@id="maincontentinnerpadding"]/div/div/form/div/ul/li[4]/div/input').click()
#time.sleep(5)
browser.find_by_xpath('//*[@id="maincontentinnerpadding"]/div/div[2]/div[3]/div/div[3]/button').click()
time.sleep(3)

for i in range(pages):  #add input
    req = browser.html
    soup = BeautifulSoup(req, "html.parser")


    title_tags = soup.find_all('span', class_ = "search-result__title")
    price1_tags = soup.find_all('span', class_ = "inventory__price-with-shipping")
    price2_tags = soup.find_all('span', class_ = "search-result__market-price--value")

    for titles, price1, price2 in zip(title_tags, price1_tags, price2_tags):
        row = []
        row.append(titles.text)
        row.append(price1.text)
        row.append(price2.text)
        price_list.append(row)           
    
    browser.find_by_xpath('/html/body/div[2]/div/div/section[2]/section/section/section/div[2]/div[1]/a[2]').click()
    time.sleep(3)
print(price_list)

# determine percent under market top 20 and covert to int
#listed_price = []

#for i in price_list:
    #dollar = price_list[i][1]
    
    