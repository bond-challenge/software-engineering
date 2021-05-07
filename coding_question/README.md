# Custom data structure
    BaseList: Interface for a custom data structure that can add, get access, and provide the moving average of the last N elements added and some more methods.
    IntegerList: Implementation of BaseList that can add, get access, and provide the moving average of the last N elements with type Integer added to a list.

## More on BaseList
Here are all the methods of the interface BaseList. 
### BaseList.add(x)
    Add an element `x` to the end of the structure.

### BaseList.get(i)
    Return a element from the structure based on index `i`, if index is greater than data structure length it raises IndexError.

### BaseList.get_remove(i)
    Returns and removes a element from the structure based on index `i` and remove it, if index is greater than data structure length it raises IndexError, if no index is specified, returns and removes the last item in the list.

### BaseList.insert(i, x)
    Insert an element `x` to the structure at a given index `i`.

### BaseList.remove(i)
    Remove an element from the structure at a given index `i`.
    
### BaseList.clear()
    Remove all items from the structure.
    
### BaseList.moving_average()
    Abstract method that needs to be implemented by child class. 

## More on IntegerList
Here are all the override methods of the implementation IntegerList.
### IntegerList.add(x)
    Add an element `x` to the end of the structure.

### IntegerList.insert(i, x)
    Insert an element `x` to the structure at a given index `i`.
    
### IntegerList.insert.moving_average(n)
    Calculate the moving average of the last elements `n` of the structure. If the data structure is empty will raise an exception, if the last_n is greater than the structure length will raise an IndexError.