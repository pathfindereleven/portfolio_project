import pandas as pd
from pathlib import Path
import sqlite3

print("Table list")
price =  Path("..\Resources\inventory.db")
con = sqlite3.connect(price)
cur = con.cursor()
q = cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
for name in q.fetchall():
    print(name[0])
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