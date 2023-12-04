The purpose of this project is to create an inventory database for magic the gathering card sellers,
	 create tools to manage the inventory, and analyze market data.

Important! - path to updated chromedriver is set to "../Resources/chromedriver.exe". Path to chromediver may have to be updated. 
		for file to run properly

This file contains;

	Resources- Contains the sqlite databases for Inventory and another db for collected market data.
			Also contains saved graphics and csv reports.
			A copy of chromdriver.exe

	Tools-  Price_Collector - a notebook that loops through cards sets and records individual card
		prices attached to today’s date and records to the "price" database. records thousands of rows 
		of data for future use.
	
		Add Inventory - a notebook used to connect to inventory data base and add inventory.
		
		Inventory Update - a notebook that uses web scraping to update columns in the inventory database to the current 
					TCG player market price
	

	Seller_Scan - contains a notebook to scrape the listed card price of a seller’s inventory on TCG player and compare it to market price, saves data and reports the cards most under market price.
		API and selenium versions.
	

	Reports - Set Regression is a notebook used to access collected price data and show how a card set is moving in price. shows graphs and r values.

		  Inventory_Report is a notebook used to report inventory market price, records total inventory value to price db for time analysis.
					calculates total cards in inventory and total prices.

	Machine_learning - folder contains a machine learning project to make price predictions. 

	Terminal App - a command terminal interface used to query the data bases, and run the tools created in notebooks. to run program
			  python command.py

		  