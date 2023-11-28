#imports
import pandas as pd
import time
from pathlib import Path
from datetime import datetime
import sqlite3

sset_list = ['MID', '10E', 'BRO', 'DGM', 'DMU', 'ELD', 'GTC', 'MAT', 'MOM', 'NEO', 'ONE', 'RTR', 'SNC', 'VOW', 'WOE']

# build db conection
price =  Path(r"C:\Users\pc\OneDrive\Desktop\portfolio_project\Demo_Day\Resources\inventory.db")
con = sqlite3.connect(price)
cur = con.cursor()
totals_price =[]
total_cards = []

# work loop
for i in sset_list:
# load table to df    
    db_df = pd.read_sql_query(f"SELECT * FROM '{i}'", con)
    db_df = db_df.fillna("0")
# clean data    
    for i in  range(len(db_df)):
        x = db_df.loc[i,['MktPrice']] 
        x = x['MktPrice']
        x = x.replace("$", "")
        x = x.replace("None", "")
        db_df['MktPrice'][i] = x
    db_df["MktPrice"] = pd.to_numeric(db_df["MktPrice"])
    db_df["quantity"] = pd.to_numeric(db_df["quantity"])
# do math
    db_df['total'] = (db_df["quantity"]) * (db_df["MktPrice"])
    total = db_df['total'].sum()
    card_count = db_df['quantity'].sum()
    totals_price.append(total)
    total_cards.append(card_count)
report_df =  pd.DataFrame(zip(sset_list, total_cards, totals_price), columns=['set', 'cards', 'totalprice'])
print(report_df)
x = report_df['totalprice'].sum()
print(f' total inventory market price is {x}')