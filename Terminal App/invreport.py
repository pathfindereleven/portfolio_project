#imports
import pandas as pd
import time
from pathlib import Path
from datetime import datetime
import sqlite3
import matplotlib.pyplot as plt
import os
from scipy.stats import linregress
sset_list = ['STX' ,'RNA','GRN','WAR','THS', 'BNG','THB' , 'MID', '10E', 'BRO', 'DGM', 'DMU', 'ELD', 'GTC', 'MAT', 'MOM', 'NEO', 'ONE', 'RTR', 'SNC', 'VOW', 'WOE','AFR']

print("Inventory Price Report [1]      Card Set Regresion[2]")
choice = input("select by index")
if (choice == "1"):
# build db conection
    price =  Path("..\Resources\inventory.db")
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
    report_df['date']= datetime.today().strftime('%Y-%m-%d') 
    print(report_df)
    x = report_df['totalprice'].sum()
    print(f' total inventory market price is {x}')
   
   # save price report as daily values in price db
    price =  Path("../Resources/price.db")
    con = sqlite3.connect(price)
    cur = con.cursor()
    x = datetime.today().strftime('%Y-%m-%d')
    cur.execute(f"select * from inv_priceData where date = '{x}'")   # prevent duplicate data
    if cur.fetchone():
        print("duplicate prvented")
    else:                                                           # write data to db
        for row in report_df.itertuples():
            insert_sql = f''' INSERT INTO 'inv_priceData' ( 'set', cards, price, date) VALUES ('{row[1]}',"{row[2]}",'{row[3]}','{row[4]}')'''
            cur.execute(insert_sql)
            con.commit()
        print('price report recorded')
   
    # create pie graph df of top 7 and combine all other data to other
    pie_df = report_df.sort_values(by='totalprice', ascending=False)
    pie_df2 = pie_df.iloc[0:7] 
    other = pie_df.iloc[7:len(pie_df)]
    otherprice= other["totalprice"].sum()
    othercards = other["cards"].sum()
    pie_df2.loc[-1] = ['other', othercards, otherprice, datetime.today() ]
    my_data = pie_df2['totalprice']
    my_labels = pie_df2['set'] 
    plt.pie(my_data, labels=my_labels, autopct="%1.1f%%", radius =1.4)

    plt.savefig("..\Resources\pie.png")
    os.startfile("..\Resources\pie.png")
    plt.figure().clear()

    ###### Create inventory value vs time line graph
    db_df = pd.read_sql_query(f"SELECT * FROM 'inv_priceData'", con)
    day_df =  db_df.drop('set', axis=1)
    day_df = day_df.groupby(['date']).sum()
    df = day_df.copy()
    df.rename(columns={df.columns[1]: 'date'})
    df["Date"]= df.index
    plt.plot(df['Date'], df['price'], color='red', label= "Total Inventory Value")
    plt.savefig('..\Resources\invreg.png')
    os.startfile("..\Resources\invreg.png")
### regresion report
if (choice == "2"):
    dbtable = ['innistrad-midnight-hunt', '10th-edition', 'the-brothers-war', 'dragons-maze', 'dominaria-united', 'throne-of-eldraine', 'gatecrash', 'march-of-the-machine-the-aftermath', 'march-of-the-machine', 'kamigawa-neon-dynasty', 'phyrexia-all-will-be-one', 'return-to-ravnica', 'streets-of-new-capenna', 'innistrad-crimson-vow', 'wilds-of-eldraine']
    count = 0
    for i in dbtable:
        print( f"{i}  {count}")
        count = count + 1
    select = int(input("Select set table to report by entering index value"))
    dbtable = dbtable[select]
    price =  Path("..\Resources\price.db")
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
    plt.savefig("..\Resources\setreg.png")
    os.startfile("..\Resources\setreg.png")
    slope, intercept, r, p, se  = linregress(mkt_df['price'], mkt_df['Date Numeric'])
    print(mkt_df)
    print(f'the regresion value for {dbtable} is {r}')