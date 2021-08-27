# Bond Challenge

## Coding Question

###Interface (DataStructureInterface.py) provided with:
1. addElements() class method - Add elements to a list
2. getLastN() class method - Get Last N elements, parameterized with listE
3. getMovingAvg() class method - Get the Moving Average parameterized with the N elements and the list
4. accessElement() class method - Access Element in the list

###Class (MovingAverageOfLastN) is provided utilizing the interface class:
###Member Variables:
listElements - to store the values (elements) that are added to the list
###Member methods:
####addElements()
Params: NA
User inputs: 2 -> Number of Elements and Value of each element
Return: the List of elements entered

Takes user input for how many elements should be added to the list (Must be a positive integer value)
Takes user input to enter as many elements as mentioned by user (Only takes integer input)

Scope of improvement (Not implemented):
I can ask the user to initialize a list with X number of elements and then keep asking during the process if more elements needs to be added dynamically to the same list

####getLastN()
Params: List
User input: 1 -> Last N Elements
Return: Value of N

Takes user input to get the Last N elements from the list (Must be a positive integer and less than the length of the List)

Scope of improvement (Not implemented):
Keep asking the user until a valid value is entered

####getMovingAvg()
Params: N, List
User input: NA
Return: List of Moving Average for N slected items in the list

Calculates the Moving average for the range of selected elements window
e.g. for a list with 5 elements [1,2,3,4,5], and selected last N element value as 2, this function will select 2 elements from the beginning and will give the average of 2 elements per selection like [1.5,2.5,3.5,4.5] in this example

Scope of improvement (Not implemented):
I can print only the "last N elements average" and ask the user to dynamically append elements to the list, and then provide the moving average based on the newly appended last N elements


####accessElement()
Params: List
User input: 1 -> The location of the elements to be accessed
Return: Value of elements at the given location in the list

Takes user input to enter the location of the element to be accessed

Scope of improvement (Not implemented):
Features like Changing or deleting the element from the list

##Unit tests:
A class (TestMovingAvg) is created for unit testing:
1. test_addElements_checkIntergerList() : To check only numeric data is entered in the list
2. test_addElements_checkAlphaNumericList(): Same as above asserting false for alphanumeric values in the list
3. test_getLastN_NegativeValueInput(): Checks if the value entered by user is positive and an integer, and is handled properly 
4. test_getLastN_MoreThanElementCountInput(): Checks if the value entered by user is greater than the length of the list, is handled properly
5. test_getMovingAvg_LastNValue3_AllInt(): Checks that the moving average calculation is correct as expected
6. test_getMovingAvg_LastNValue3_AlphaNumeric(): Asserts false is values in the list are non-numeric

###Known Issues with Unit tests:
Noticing the redundancy in the test cases - Elements in the list will always be numeric based on the current code handling
Test for getLastN() returns "None" when the value doesn't meet the criteria fails (greater than 0 and less than or equal to the length of list)

Unit tests are running successfully when ran isolated. When ran together, running into some issues to be troubleshooted further.

