Understanding Problem:
Simple Moving Average is the average obtained from the data for some t period of time . 

For example, if we need moving average of last SlidingWindow=3 elements from an input = [...,35,30,25,20,15,10,5] (Note: 5 is the first element on queue, 35 is last) then when we see 15 we have reached SlidingWindow=3 numbers. 
When next number 20 comes in, we need to compute average of last 3 i.e [20,15,10]. 
Similarly for next number 25 moving average will be the average of [25,20,15], then [30,25,20] and so on.

Data Structure: 
Using queue for first in, first out ordering of elements.

Calculating Simple Moving Average:
Case 1:
If we have seen total SlidingWindow numbers so far and current average is avg then, when we add a new element the nextNum moving average would be 
	avg=(SlidingWindow*avg+nextNum)/(SlidingWindow+1)
The above formula can be used till the SlidingWindow number is reached. 

For example for an input = [...,35,30,25,20,15,10,5], when we see 15 we have reached SlidingWindow=3 in first frame [15, 10, 5] and when the next number i.e. 20 comes in, we need to calculate moving average for [20,15,10]

Case 2:
If current moving average of last SlidingWindow element is avg and the first of the elements is F then when we see last new element L the moving average would be:
	avg=(SlidingWindow*avg-F+L)/SlidingWindow

We will use Queue of size N and dequeue the first element when the queue is full.