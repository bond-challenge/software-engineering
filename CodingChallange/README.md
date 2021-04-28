# Coding Question - Explanation about the interface and implementation

**Interface: **com.codingchallenge.service.MovingAverageInterface (generic type)

There are 3 methods inside this interface.

1) addElement(T element) - adding element to the data structure

2) getElements() - to access the data structure which stores all elements

3) getAverage() - calculate the the average of the last N elements

**Implementation: **com.codingchallenge.service.MovingAverage

Implemented **MovingAverage** interface with type **Double**

The constructor allows user to initialize MovingAverage with predefined "N" as windowSize. "N" should be greater than 0, otherwise, it will throw IllegalArgumentException.

1) addElement(Double element) - adding Double into an ArrayList

2) getElements() - return the list of elements which contains all added elements

3) getAverage() - return the average of the last N elements. It will return 0 if the number of elements is less than "N".



