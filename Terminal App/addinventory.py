#imports
import pandas as pd
from pathlib import Path
import sqlite3

#build db conection
print("Table list")
price =  Path("../Resources/inventory.db")
con = sqlite3.connect(price)
cur = con.cursor()

# print table list
q = cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
for name in q.fetchall():
    print(name[0])
x = 'y'
y = "y"
while y == 'y':
    ans1 = input('What set')
    while x == 'y':
            ans2 = input('what is card name "LIKE"')  # search card name
            name_qry = pd.read_sql_query(f"SELECT * from {ans1} WHERE name LIKE '%{ans2}%'", con)
            print(name_qry)

            # confirm card
            confirm = int(input('enter card index to confirm'))
            cardname = name_qry.iloc[confirm, 1] 
            condition = input( 'enter condition; nm , lp, p, foil' )
            quantity = input("enter quantity to add to db")
            q = cur.execute(f'UPDATE {ans1} set {condition} = {condition} + {quantity} Where name = "{cardname}"')
            v = cur.execute(f'UPDATE {ans1} set quantity = quantity + {quantity} Where name = "{cardname}"')
            con.commit()
            
            x = input('continue working with set? y/n')
    y = input("add more Inventory? y/n")
con.close()