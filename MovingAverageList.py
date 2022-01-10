from collections import deque
from numbers import Number
from typing import List, Optional

from moving_average.moving_average_iterable import MovingAverageFun


class MovingAverageList(MovingAverageFun):
    """
    List implementation of the <MovingAverageFun> abstract class.
    """

    def __init__(self, n_last_elements: int):
        """
        Constructs list of numbers with a moving average calculated from the last n elements.
        :param n_last_elements: number of last elements to compute the moving average.
        """
        if n_last_elements <= 0:
            raise ValueError('Number of last elements must be higher than zero')
        self.n_last_elements = n_last_elements
        self.last_n_elements_sum = 0
        self.avg_queue = deque([])
        self.elements = []

    def append(self, last: Number) -> None:
        """
        Appends the specified element to the end of this list and computes the sum of the last n elements.
        :param last:
        :return:
        """
        self.last_n_elements_sum += last
        self.avg_queue.append(last)
        if len(self.avg_queue) > self.n_last_elements:
            first = self.avg_queue.popleft()
            self.last_n_elements_sum -= first
        self.elements.append(last)

    def get_elements(self) -> List[Number]:
        """
        :return: the list of elements.
        """
        return self.elements

    def get_moving_average(self) -> Optional[Number]:
        """
        :return: the arithmetic mean of the last n elements or None if the elements collection is empty.
        """
        if len(self.avg_queue) == 0:
            return None
        return self.last_n_elements_sum / len(self.avg_queue) 