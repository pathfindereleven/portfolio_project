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
from splinter import Browser
from selenium.webdriver.chrome.service import Service

my_service = Service(executable_path=r'C:\Users\pc\OneDrive\Desktop\TCG-scraper\chromedriver.exe')
browser = Browser('chrome', service=my_service)
sset = ['innistrad-midnight-hunt', '10th-edition', 'the-brothers-war', 'dragons-maze', 'dominaria-united', 'throne-of-eldraine', 'gatecrash', 'march-of-the-machine-the-aftermath', 'march-of-the-machine', 'kamigawa-neon-dynasty', 'phyrexia-all-will-be-one', 'return-to-ravnica', 'streets-of-new-capenna', 'innistrad-crimson-vow', 'wilds-of-eldraine', 'kaldheim', 'ixalan', 'war-of-the-spark']

for x in sset:
    url =f"https://shop.tcgplayer.com/price-guide/magic/{x}"
    browser.visit(url)
    browser.driver.maximize_window()
    time.sleep(7)
    req = browser.html
    soup = BeautifulSoup(req, "html")
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
    price_list= zip(names, prices)
    mkt_df = pd.DataFrame(price_list,) 
    mkt_df = mkt_df.reset_index(drop=True)
    mkt_df.columns = ['Name', 'Market Price']
    mkt_df['date']= datetime.today().strftime('%Y-%m-%d')
    d = datetime.today().strftime('%Y-%m-%d')                        # prvent duplicate conditional
    mkt_df['Unnamed: 0']= 2
    mkt_df = mkt_df[['Unnamed: 0', 'Name', 'Market Price', 'date']]
    price =  Path(r"C:\Users\pc\OneDrive\Desktop\portfolio_project\Demo_Day\Resources\price.db")
    con = sqlite3.connect(price)
    cur = con.cursor()
    cur.execute(f"select * from '{x}_priceData' where date = '{d}'")
    if cur.fetchone():
        print(f"duplicate prvented for {x}")
    else:
        for row in mkt_df.itertuples():
            insert_sql = f''' INSERT INTO '{x}_priceData' ('Unnamed: 0', Name, 'Market Price', date) VALUES ('{row[1]}',"{row[2]}",'{row[3]}','{row[4]}')'''
            cur.execute(insert_sql)
        print(f'{x} updated sucesfully')
    #con.commit()
    
con.close()