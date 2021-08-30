# Bond Challenge

## Coding Question

###Interface (dataStrucutureInterface.py) provided with:
1. add_next() class method - Add elements to a list
2. calculate_average() class method - Get the Moving Average parameterized with the N elements and the list
3. access_element() class method - Access Element in the list

####dataStructureImplemnentation.py

###Class MovingAverage implements MovingAverageInterface:

###Member Variables:
list - to store the values (elements) that are added to the list
size - to store the size of moving average
###Member methods:

####add_next(self, val: int):
Params: NA
User inputs: 1 -> value to be added next
Return: None


####calculate_average(self, val: int) -> float
Params: N
User input: NA
Return: Moving Average value

Calculates the Moving average for the range of selected number of elements and Track the numbers added and size of numbers.
e.g. for a list with 5 elements [1,2,5,10,15], and selected last N element value as 3, this function will select 3 elements from the beginning and will give the average of 3 elements per selection like [1.0,1.5,2.66,5.66,10.0] 

####access_element(self, n) -> int
Params: List
User input: 1 -> The location of the elements to be accessed
Return: Value of elements at the given location in the list

####Constraints:

1 <= size <= 1000

-105 <= val <= 105

At most 104 calls will be made to next.

####Time Complexity: O(N).
###Space Complexity: O(N).