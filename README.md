###This is a README file for Implementation Details for coding question asked and comments are in line to the questions below. *

##Interface: 

**class named DataInterface in dataInterface.py

There are 3 abstract methods in this interface

1) addElement(element) - This method adds element to data structure

2) accessElement() - This method is retrives all the elements from data structure

3) getAverage() - This method gets the  average of last n elements


##Implementation

**class named ProcessData implements the interface class DataInterface

This class implemnets the abstract methods in DataInterface class.

1) getAverage():-
	This function calculates the avergae of last N sales events received from POS system. 
	It handles index error, value error and zero devision error.
	
	Using pandas, the json events are converted into pandas dataframe and sorted by transaction date. Then avergae of last n sales value is calculated.

2) getElements() 
	This function returns all the elements added to the data structure.

3) addElement() adds a number into a list data structure.
	This function adds a POS event as a json object into a list. 



