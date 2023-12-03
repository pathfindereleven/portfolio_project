import os
import webbrowser
from datetime import date
import subprocess as sub
from pathlib import Path

x ="y"
while x == "y":


        print("seller report [1]                 Query set [5]")
        print("inventory Db update [2]           Query all inventory [6]")
        print("price collector [3]               Inventory report [7]    ")
        print("add inventory [4]")
        choice = input( "your command?")

        if (choice == "1"):
                os.system(" python scan.py")
        if (choice == "5"):
                os.system(" python set_query.py")
        if (choice == "4"):
                os.system(" python addinventory.py") 
        if (choice == "6"):
                os.system(" python total_Query.py")  
        if (choice == "2"):
                os.system(" python invDB_priceUpdate.py")
        if (choice == "3"):
                os.system(" python data_mining.py") 
        if (choice == "7"):
                os.system(" python invreport.py")     
                   
        
        
        x = input("continue y/n")