
Moving Average Solution:

This solution can be implemented in various ways.

1) In AWS we can use , windowAvg function which can also calculate the moving average.
2) This can be implemented with Python as well and can be used in AWS, Azure or GCP using Pandas and Boto3 library depending upon requirements. I have
currently implemented it using the Python scripts .
3) Again we can use Java , C# or any programming language and implement interface and then define the implementation on the basis of that interface.

Below are the different objects I have used in this solution:



moving_average — Iterable containers with moving average data types
This module implements specialized container data types with moving average of n elements.

MovingAverageN
Abstract collection representing an iterable group of numbers with a computed moving average of the last n added elements.

MovingAverageList
List implementation of the MovingAverageN abstract class.