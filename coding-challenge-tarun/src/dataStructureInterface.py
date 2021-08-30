from interface import implements, Interface


class MovingAverageInterface(Interface):
    """create an interface for moving average OF N Numbers
     MovingAverageInterface contains methods  to call average and other helper methods
     Returns the moving average of the last size values of the list."""

    def __init__(self, size: int):
        pass

    def add_next(self, val: int) -> float:
        """Interface to add next element in list"""
        pass

    def access_element(self, n: int) -> int:
        """Interface to access given element in list"""
        pass

    def calculate_average(self, val: int) -> float:
        """Interface to calculate moving average based on requirements"""
        pass
