import pandas as pd
from pathlib import Path
import sqlite3
import numpy as np
from sklearn.datasets import load_iris

price =  Path("..\Resources\inventory.db")
con = sqlite3.connect(price)
cur = con.cursor()
#cur.execute("create view total as SELECT * FROM BRO union select * from DMU union select * from '10E' union select * from DGM union select * from MOM union select * from NEO union select * from ONE union select * from SNC union select * from VOW union  select * from WOE union select * from ELD union select * from GTC union select * from MAT union select * from MID union select * from RTR")

print("'select * from total' given")

x ="y"
while x == "y":
    ans = input("type querry SQL string")
    querry = f"select * from total {ans}"
    querry_df = pd.read_sql_query(querry, con)
    #data = load_iris(querry_df)
    #df = pd.DataFrame(data.data, columns=data.feature_names)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None,  'display.width', 1000,):
        print(querry_df)
    
    print(len(querry_df))
    x = input("qeurry more y/n")

    #select * from total where subtypes like '%vampire%'