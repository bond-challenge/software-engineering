from abc import ABCMeta, abstractmethod
from numbers import Number
from typing import Any, List, Optional


class BaseList(metaclass=ABCMeta):
    """
    Interface for a custom data structure that can add, get access, and provide
    the moving average of the last N elements added.
    """

    def __init__(self, elements: Optional[List[Number]] = None):
        if elements:
            self.elements = list(elements)
        else:
            self.elements = []

    def add(self, element: Number) -> None:
        """
        Add an element to the end of the structure.

        :param element: Element to be added to the structure.
        """
        self.elements.append(element)

    def get(self, index: int) -> Number:
        """
        Return a element from the structure based on index, if index is greater
        than data structure length it raises IndexError.

        :param index: Position in the structure, starting from 0.
        """
        return self.elements[index]

    @abstractmethod
    def moving_average(self, last_n: Any) -> None:
        """
        Calculate the moving average of the last_n elements of the structure.
        """
        raise NotImplementedError


class IntegerList(BaseList):
    """
    Class that can add, get access, and provide the moving average of the last N integer
    added to a list.
    """

    def add(self, element: int) -> None:
        """
        Add an integer to the end of the structure.

        :param element: Integer to be added to the structure.
        """
        self.elements.append(element)

    def insert(self, index: int, element: int):
        """
        Insert an integer to the structure at a given index.

        :param index: Position in the structure, starting from 0.
        :param element: Integer to be added to the structure.
        """
        self.elements.insert(index, element)

    def moving_average(self, last_n: int) -> Number:
        """
        Calculate the moving average of the last_n elements of the structure.
        If the data structure is empty will raise an exception, if the last_n is greater
        than the structure length will raise an IndexError.
        """
        if len(self.elements) == 0:
            raise IndexError("Data structure is empty.")
        if last_n <= 0:
            raise ZeroDivisionError("Last_n has to be greater than zero. ")
        elif last_n > len(self.elements):
            raise ValueError(
                "Last_n is greater than data structure length, "
                "an average cannot be calculated."
            )

        return sum(self.elements[-last_n:]) / last_n
