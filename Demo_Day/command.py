import os
import webbrowser
from datetime import date
import subprocess as sub
from pathlib import Path

x ="y"
while x == "y":


        print("seller report [1]                 Querry set [5]")
        print("inventory Db update [2]           Querry all inventory [6]")
        print("price collector [3]               Inventory report [7]    ")
        print("add inventory [4]")
        choice = input( "your command?")

        if (choice == "1"):
                os.system(" python scan.py")
        if (choice == "5"):
                os.system(" python set_querry.py")       
        x = input("continue y/n")