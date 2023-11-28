import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import time
import requests
import os
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path
from datetime import datetime
import sqlite3
querry_dic = {'MID':'innistrad-midnight-hunt','10E':'10th-edition', 'BRO':'the-brothers-war', 'DGM':'dragons-maze',
 'DMU':'dominaria-united', 'ELD':'throne-of-eldraine', 'GTC':'gatecrash', 'MAT':'march-of-the-machine-the-aftermath', 
   'MOM':'march-of-the-machine', 'NEO':'kamigawa-neon-dynasty', 'ONE':'phyrexia-all-will-be-one', 'RTR':'return-to-ravnica',
  'SNC':'streets-of-new-capenna', 'VOW':'innistrad-crimson-vow', 'WOE': 'wilds-of-eldraine'}
from selenium.webdriver.chrome.service import Service
my_service = Service(executable_path=r'C:\Users\pc\OneDrive\Desktop\TCG-scraper\chromedriver.exe')
browser = Browser('chrome', service=my_service)
loop_key = list(querry_dic.keys())
loop_values = list(querry_dic.values())
for i in range(len(loop_key)):
#assign url string and set table
    dbtable = loop_key[i]
    url_string =  loop_values[i]
# visit website and make soup
    url =f"https://shop.tcgplayer.com/price-guide/magic/{url_string}"
    browser.visit(url)
    browser.driver.maximize_window()
    time.sleep(6)
    req = browser.html
    soup = BeautifulSoup(req, "html")
# scrape data
    names= []
    title_tags = soup.find_all('a', class_ = "pdp-url")
    for i in title_tags:
           names.append(i.text)
    prices =[]
    price = soup.find_all('td', class_ = "tcg-table-body__cell tcg-table-body__cell--align-right")
    count = -1
    for i in price:
        count = count +1
        if  count%2 > 0 :
            prices.append(i.text)
# make df with scraped data
    
    price_list= zip(names, prices)
    mkt_df = pd.DataFrame(price_list,columns = ['Name', 'Market Price']) 
    mkt_df['date']= datetime.today().strftime('%Y-%m-%d')
# build db conection
    price = Path(r"C:\Users\pc\OneDrive\Desktop\portfolio_project\Demo_Day\Resources\inventory.db")
    con = sqlite3.connect(price)
    cur = con.cursor()
# open inventory db to df to match names
    db_df = pd.read_sql_query(f"SELECT * FROM '{dbtable}'", con)
# loop to update scrapped price in loaded data frame
    count = 0
    while count < len(db_df): # next itteration if loop fails 
        try:
            for i in range(count , len(db_df)):
                search = db_df.loc[i,['name']]   # 
                search = search['name']
                search_df = mkt_df.loc[mkt_df['Name'] == search]
                           # break if no match
                search_df.reset_index(drop=True, inplace=True)
                search_result = search_df["Market Price"][0]
                db_df.loc[i,['MktPrice']] = search_result
                count = count + 1
        except: # if no match 
                db_df.loc[i,['MktPrice']] = "na"
                count = count + 1
# comit df to db
    for i in range(len(mkt_df)):
        search = mkt_df.loc[i,['Name']]   # 
        search = search['Name']
        x = mkt_df.loc[i,['Market Price']]  
        x = x['Market Price']
        insert_sql = f'''UPDATE  '{dbtable}'  set MktPrice ="{x}" where "name" = "{search}"'''
        cur.execute(insert_sql)
        con.commit()
    print(f'{dbtable} updated sucesfully')