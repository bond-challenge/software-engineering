Created an interface named Data structure with 4 methods as follows

       void addElement(int element); 
       
       Double averageOfLastNElementsAdded(int n);
       
       Integer getElement(int index);
   
       List<Integer> getAllElements();
Will be maintaining an array with the size given at the time of creating the object for DataStructure Impl

**Method 1 :** `void addElement(int element); `

Will add the element to the data array and increment the index

**Method 2 :** `Integer getElement(int index) `

Will check whether the given index is grater than 1 and less than the last index of the data array, id it satifies then will 
get the element exists for the given index if not will print an error.

**Method 3 :** `List<Integer> getAllElements() `

Will return a list of integer from the data array up the last index 

**Method 4 :** `Double averageOfLastNElementsAdded(int n) `

1. Will check whether the given n is in the range of the current index, if doesn't exists then will print error in console and return null
2. Will get the last N elements lastly added and find the average and return the average

**TO Execute the DataStructure implementation provided a Runner with main method** 