Coding Question

Write an interface for a data structure that can provide the moving average of the last N elements added, add elements to the structure and get access to the elements. Provide an efficient implementation of the interface for the data structure.

For your submission, please submit a PR to the main branch of this repository.

Minimum Requirements
1. Provide a separate interface (i.e. interface/trait) with documentation for the data structure
2. Provide an implementation for the interface
3. Provide any additional explanation about the interface and implementation in a README file.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

NOTE: I am not a hardcore programmer but I have done some research online and understood the concepts to present the below code in JAVA.
Also the code below is not completely written by me. I have reused the code available.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The method calculates and returns moving average of last N element using below logic

1. Accepts new element to be added in queue from stream of input data
2. Accepts maxSize of queue as duration/period for which moving average needs to be calculated
3. Maitains the first(head) element and last(tail) element of queue
4. Removes first element entered in FIFO queue buffer, once buffer is full based on input maxSize and decrement queueTotal & queue size
5. Maintains the size of queue buffer equal to input maxSize
6. Size -> Increment and calculates current total queue/buffer size upon addition of new element
7. queueTotal -> Calculates Sum of all elements from current queue/buffer
8. Calculates moving average with time complexity-> O(1)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Working Example:

Assuming nthElement=5 which is basically period/duration of last N element we want to calculate the Moving average from given stream of data input

Data imput - [1,-8,5,3,2,6,7,0.2,0.33]

Step 1- First input goes from input stream {1} for processing, queueSize is 1, the moving average = 1/1 = 1

Step 2- Second input goes from input stream {1,-8} for processing, queueSize is 2, the moving average = (1 -8)/2 = -3.5

Step 3- Third input goes from input stream {1,-8,5} for processing, queueSize is 3, the moving average = (1 -8 + 5)/3 = -0.67

Step 4- Fourth input goes from input stream {1,-8,5,3} for processing, queueSize is 4, the moving average = (1 -8 + 5 + 3)/4 = 0.25

Step 5- fifth input goes from input stream {1,-8,5,3,2} for processing, queueSize is 5, the moving average = (1 -8 + 5 + 3 + 2)/5 = 0.6

Step 6 - sixth input goes from input stream {1,-8,5,3,2,6} for processing, now here as buffer is full so API will remove head element from queue and the calculate moving average, the queueSize is 5, the moving average = (-8 + 5 + 3 + 2 + 6)/5 = 1.6

Step 7 - Seventh input goes from input stream {1,-8,5,3,2,6,8} for processing, buffer is again full so API will remove head element from queue and the calculate moving average, the queueSize is 5, the moving average = (5 + 3 + 2 + 6 + 8)/5 = 4.8




