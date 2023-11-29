#imports
import pandas as pd
import time
from pathlib import Path
from datetime import datetime
import sqlite3
import matplotlib.pyplot as plt
import os
from scipy.stats import linregress
sset_list = ['MID', '10E', 'BRO', 'DGM', 'DMU', 'ELD', 'GTC', 'MAT', 'MOM', 'NEO', 'ONE', 'RTR', 'SNC', 'VOW', 'WOE']

print("Inventory Price Report [1]      Card Set Regresion[2]")
choice = input("select by index")
if (choice == "1"):
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
    # create pie graph df of top 7 and combine all other data to other
    pie_df = report_df.sort_values(by='totalprice', ascending=False)
    pie_df2 = pie_df.iloc[0:7] 
    other = pie_df.iloc[7:len(pie_df)]
    otherprice= other["totalprice"].sum()
    othercards = other["cards"].sum()
    pie_df2.loc[-1] = ['other', othercards, otherprice]
    my_data = pie_df2['totalprice']
    my_labels = pie_df2['set'] 
    plt.pie(my_data, labels=my_labels, autopct="%1.1f%%", radius =1.4)

    plt.savefig(r"C:\Users\pc\OneDrive\Desktop\portfolio_project\Demo_Day\Resources\pie.png")
    os.startfile(r"C:\Users\pc\OneDrive\Desktop\portfolio_project\Demo_Day\Resources\pie.png")

### regresion report
if (choice == "2"):
    dbtable = ['innistrad-midnight-hunt', '10th-edition', 'the-brothers-war', 'dragons-maze', 'dominaria-united', 'throne-of-eldraine', 'gatecrash', 'march-of-the-machine-the-aftermath', 'march-of-the-machine', 'kamigawa-neon-dynasty', 'phyrexia-all-will-be-one', 'return-to-ravnica', 'streets-of-new-capenna', 'innistrad-crimson-vow', 'wilds-of-eldraine']
    count = 0
    for i in dbtable:
        print( f"{i}  {count}")
        count = count + 1
    select = int(input("Select set table to report by entering index value"))
    dbtable = dbtable[select]
    price =  Path(r"C:\Users\pc\OneDrive\Desktop\portfolio_project\Demo_Day\Resources\price.db")
    con = sqlite3.connect(price)
    cur = con.cursor()
    db_df = pd.read_sql_query(f"SELECT * FROM '{dbtable}_priceData'", con)
    setplist= []
    date_list = list(db_df['date'].unique())
    for x in date_list:
        day_df= db_df.loc[db_df["date"]== x ]
        day_df = day_df.reset_index(drop=True)
       
        for i in  range(len(day_df)):
            x = day_df.loc[i,['Market Price']] 
            x = x['Market Price']
            x = x.replace("$", "")
            x = x.replace("None", "")
            day_df['Market Price'][i] = x
        day_df['Market Price'] = pd.to_numeric(day_df['Market Price'])
        set_price = day_df['Market Price'].sum()
        setplist.append(set_price)
    sip_list= zip(setplist, date_list)
    mkt_df = pd.DataFrame(sip_list,columns = ['price', 'date'])
    mkt_df['date'] = pd.to_datetime(mkt_df['date'])
    mkt_df['Date Numeric'] = pd.to_numeric(mkt_df['date'])
    mkt_df["price"] = pd.to_numeric(mkt_df["price"])
    plt.plot(mkt_df['date'], mkt_df['price'], color='red', label= dbtable)
    plt.savefig(r"C:\Users\pc\OneDrive\Desktop\portfolio_project\Demo_Day\Resources\setreg.png")
    os.startfile(r"C:\Users\pc\OneDrive\Desktop\portfolio_project\Demo_Day\Resources\setreg.png")
    slope, intercept, r, p, se  = linregress(mkt_df['price'], mkt_df['Date Numeric'])
    print(mkt_df)
    print(f'the regresion value for {dbtable} is {r}')