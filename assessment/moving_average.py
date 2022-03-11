from abc import ABC, abstractmethod
from typing import List

class IMovingAverageCalculator(ABC):
    '''
    Provides the interface to implement moving average of the 
    last N elements
    '''

    @abstractmethod
    def __init__(self):
        '''
            Initializes list of elements, use it as a queue
        '''
        self.__elements: List = []

    @property
    @abstractmethod
    def elements(self):
        '''
            Implement this as the getter of the elements
        '''
        pass

    @abstractmethod
    def add_element(self, element: int) -> None:
        '''
            Implement this to add an element to the existing list of elements
        '''
        raise NotImplementedError
    
    @abstractmethod
    def get_moving_average(self, n: int) -> int:
        '''
            Implement this to calculate/retrieve the moving average based on the last N elements
        '''
        raise NotImplementedError


# Time complexity: O(1) (considering list.append and list.pop as O(1))
# Space complexity: O(n)
class MovingAverageCalculator(IMovingAverageCalculator):
    '''
    Implementation of the IMovingAverageCalculator
    '''

    # O(n) Space
    def __init__(self, n) -> None:
        '''
            Initialzes the class with the properties
        '''
        self.__n: int = n
        self.__average: float = 0
        self.__elements: List = []
    
    @property
    def elements(self):
        '''
            Getter of the elements list
        '''
        return self.__elements

    # O(1) time
    def add_element(self, element: float) -> None:
        '''
            Adds a new element to the list and calculates the new moving average
        '''
        queue_size = len(self.__elements)
        previous_sum = self.__average * queue_size

        if self.__n == queue_size:
            previous_element = self.__elements.pop(0)
            self.__elements.append(element)
            previous_sum -= previous_element
        else:
            self.__elements.append(element)
            queue_size += 1                

        self.__average = (previous_sum + element)/queue_size

    # O(1) time
    def get_moving_average(self) -> float:
        '''
            Retrieves the moving average of last N elements
        '''
        return round(self.__average, 2)