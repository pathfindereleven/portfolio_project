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
time.sleep(3)
 # add input
seller_list = [seller, 'xyz', 'abc']
browser.fill('SellerName', seller)
browser.find_by_xpath('//*[@id="maincontentinnerpadding"]/div/div/form/div/ul/li[4]/div/input').click()
#time.sleep(5)
browser.find_by_xpath('//*[@id="maincontentinnerpadding"]/div/div[2]/div[3]/div/div[3]/button').click()
time.sleep(3)

for i in range(pages):
    req = browser.html
    soup = BeautifulSoup(req, "html.parser")

    cat_tags = soup.find_all('h3', class_ ="search-result__category-name")
    set_tags = soup.find_all('h4', class_ ="search-result__subtitle")
    title_tags = soup.find_all('span', class_ = "search-result__title")
    price1_tags = soup.find_all('span', class_ = "inventory__price-with-shipping")
    price2_tags = soup.find_all('span', class_ = "search-result__market-price--value")

    for  cat, sset, titles, price1, price2 in zip( cat_tags ,set_tags, title_tags, price1_tags, price2_tags):
        row = []
        row.append(cat.text)
        row.append(sset.text)
        row.append(titles.text)
        row.append(price1.text)
        row.append(price2.text)
        price_list.append(row)           
    
    browser.find_by_xpath('/html/body/div[2]/div/div/section[2]/section/section/section/div[2]/div[1]/a[2]').click()
    time.sleep(4)
df = pd.DataFrame(price_list)
df.columns = [  "category", "set", 'Name', 'Listed Price','Market Price']

df["Market Price"] = df["Market Price"].str.replace("$", "")
df["Listed Price"] = df["Listed Price"].str.replace("$", "")
df['Market Price'] = df['Market Price'].astype(float)
df['Listed Price'] = df['Listed Price'].astype(float)
df["over_under"] = (df["Listed Price"]) - (df['Market Price'])
sorted_df = df.sort_values(["over_under"])
limit_df= sorted_df.loc[sorted_df['category'] == "Magic: The Gathering"]
limit_df= limit_df.iloc[:15]
with pd.option_context('display.max_rows', 20,
                       'display.max_columns', None,
                       'display.width', 1000,
                       'display.precision', 3,
                       'display.colheader_justify', 'left'):
    print(limit_df)

# determine percent under market top 20 and covert to int
#listed_price = []

#for i in price_list:
    #dollar = price_list[i][1]
    
    