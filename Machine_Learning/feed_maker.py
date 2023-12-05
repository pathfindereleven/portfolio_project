import pandas as pd
from pathlib import Path
import sqlite3
import pandasql as ps

setcode = ["WAR", 'MID', 'NEO', 'VOW', "KHM", 'XLN']

price =  Path("../Resources/price.db")
con = sqlite3.connect(price)        # conect to price db
cur = con.cursor()
feed_df = pd.DataFrame()


for i in setcode:
    db_df = pd.read_sql_query(f"SELECT * FROM 'goldfish' where setcode = '{i}'", con)
    file_path = Path(f"resources\set_tables\{i}.csv")
    set_info = pd.read_csv(file_path)
    rarities_count = set_info['rarity'].value_counts()
    db_df['rare'] = rarities_count['rare']
    db_df['mythic'] = rarities_count['mythic']
    db_df['uncommon'] = rarities_count['uncommon']
    db_df['common'] = rarities_count['common']
    q1 = """SELECT subtypes FROM set_info where subtypes like '%angel%' """
    q1 = (ps.sqldf(q1, locals()))
    db_df['angel'] = len(q1)
    q2 = """SELECT subtypes FROM set_info where subtypes like '%human%' """
    q2 = (ps.sqldf(q2, locals()))
    db_df['human'] = len(q2)
    q3 = """SELECT subtypes FROM set_info where subtypes like '%zombie%' """
    q3 = (ps.sqldf(q3, locals()))
    db_df['zombie'] = len(q3)
    db_df = db_df.assign(day_int=db_df.index)
    feed_df = pd.concat([feed_df,db_df])

feed_df.to_csv("feed.csv") 