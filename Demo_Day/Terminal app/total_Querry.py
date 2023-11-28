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

price =  Path(r"C:\Users\pc\OneDrive\Desktop\portfolio_project\Demo_Day\Resources\inventory.db")
con = sqlite3.connect(price)
cur = con.cursor()
#cur.execute("create view total as SELECT * FROM BRO union select * from DMU union select * from '10E' union select * from DGM union select * from MOM union select * from NEO union select * from ONE union select * from SNC union select * from VOW union  select * from WOE union select * from ELD union select * from GTC union select * from MAT union select * from MID union select * from RTR")

print("use total as table")

x ="y"
while x == "y":
    querry = input("type querry SQL string")
    querry_df = pd.read_sql_query(querry, con)
    with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.width', 1000,
                       'display.precision', 3,
                       'display.colheader_justify', 'left'):
        print(querry_df)
    x = input("qeurry more y/n")