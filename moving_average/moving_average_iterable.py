from abc import ABC, abstractmethod
from numbers import Number
from typing import Iterable, Optional


class MovingAverageIterable(ABC):
    """
    Abstract collection representing an iterable group of numbers with a computed moving average of the last n added
    elements.
    """

    @abstractmethod
    def append(self, last: Number) -> None:
        """
        Appends the specified element to the end of the elements
        :param last: to be appended.
        :return: None
        """
        pass

    @abstractmethod
    def get_elements(self) -> Iterable[Number]:
        """
        :return: returns the iterable elements.
        """
        pass

    @abstractmethod
    def get_moving_average(self) -> Optional[Number]:
        """
        :return: the arithmetic mean of the last n elements or None if the elements collection is empty.
        """
        pass
