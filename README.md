There are three requirements specified:

1. provide the moving average of the last N elements added
2. add elements to the structure
3. get access to the elements

Assumptions made:

1. Incoming elements are all integers for the possibility to calculate average. A check_input_type() method is implemented to ensure this.
2. The order of elements does not matter, so if 1 comes after 10, the order stays [10, 1]. No sorting is required.
3. Accessing elements means returning the positions (or keys) of the elements and the elements themselves. Note if the elements are repeating, their respective indices will also be returned.
4. "Moving average of the last N elements added" can differ depending on what state the current array is in. Interpretation of the requirement is illustrated below in an example:

    
    time 1: array = [1, 2, 3, 4, 5], N = 2
    
    current_last_2_element_average = average of [4, 5] = 4.5
    
    time 2: array = [1, 2, 3, 4, 5, 6, 7, 8], N = 2
    
    current_last_2_element_average = average of [7, 8] = 7.5
    
Because the state of the array is changing, we will record the "N" being requested at the time, the last N elements that corresponds to, and their average.

If the requirement was "moving average of every 2 elements", then the rolling average of every 2 elements would've been calculated, so for example:


    array = [1, 2, 3, 4, 5], N = 2

    moving_average_of_2_elements = [1.5, 2.5, 3.5, 4.5]


For ease of accessing and potential need to sort the order of elements in the future, the data type, array, is chosen.

Unit testing is included to test edge cases when the data structure is not being used as intended.

Anticipating future requirements:
> * remove elements from the data structure
> * create a timestamp for each record in the moving average snapshot (currently, the higher the index of an entry, the more recent it is)
> * change the current method of calculating a moving average
