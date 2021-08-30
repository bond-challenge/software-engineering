from interface import implements, Interface
from dataStructureInterface import MovingAverageInterface


class MovingAverage(implements(MovingAverageInterface)):
    """Implement the interface for moving average problem"""

    def __init__(self, size: int):
        """
        Initialize our data structure which includes list and sie of moving average.
        """
        self.numbers = []
        self.size = size

    def add_next(self, val: int):
        """Add the next integer here and return the moving average"""
        self.numbers.append(val)
        pass

    def calculate_average(self, val: int) -> float:
        try:
            self.add_next(val)

            if len(self.numbers) > self.size:
                return sum(self.numbers[-self.size:]) / self.size

            return sum(self.numbers) / len(self.numbers)
        except TypeError:
            print("Bad Type Entered Error")

    def access_element(self, n) -> int:
        try:
            if 1 <= n <= len(self.numbers):
                return self.numbers[n - 1]
            else:
                raise ValueError(
                    'element is not between 1 - ' + str(len(n))
                )
        except ValueError:
            print('element is not between 1 - ' + str(len(n)))


if __name__ == '__main__':
    """Main module run input array is 1,2,5,10,15
        output would be 1.0,1.5,2.66,5.66,10.0"""
    p_size = 3
    moving_avg = MovingAverage(p_size)
    print('Add to the list for calculating moving average')
    val_1 = moving_avg.calculate_average(1)
    val_2 = moving_avg.calculate_average(2)
    val_3 = moving_avg.calculate_average(5)
    val_4 = moving_avg.calculate_average(10)
    val_5 = moving_avg.calculate_average(15)

    print(val_5)
    access_value = moving_avg.access_element(1)

    print(access_value)
