MTG Linear Regresion Testing

Purpose:
	The purpose of this file is to use collected magic the gathering data format it to be 
read into a skylearn model and analyze the results. The machine is being trained on the first 6 
months price data after a magic the gathering set is released and the first two weeks for a tested set. 
Then the model is used to predict the entire first six months data using multiple linear regression.


Folder contains:

Resources:
	'num-feed' of numeric data to be fed to the machine model. 
	'predict.csv' numeric data for machine to make prediction on.
	'm1VOW-pre' predicted values for the testing set for each machine
	'prediction_m1' predicted values for the training data
	'Vow_actual' actual price of testing set
	'Datacleaning' - a note book to sort attribute data
	'set_tables' - atributes of card sets csv
	'prices' -card set price data
	'Images' graphs are saved here

Machine1:  Multiple Linear Regresion model using Date and attribute Data to predict price.

Machine2: Same as Machine1 but uses less attribute data

Machine3: Same as Machine one but uses more attribute data


Graphs and Calculations:  A notebook to make graphs and calculations to analyze the produced data.

