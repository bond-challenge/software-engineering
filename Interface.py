import abc


class Interface(abc.ABC):

    @classmethod
    def add_element(self, element=None):
        """
        Add elements to the array. Return the array's current state if the input is None or empty.
        :return:
        """
        pass

    @classmethod
    def get_last_N_moving_average(self, N):
        """
        Calculate the average of the last N elements within the non-empty array, and record the corresponding inputs
        :return:
        """
        pass

    @classmethod
    def access_elements(self, elements):
        """
        Access the elements in the array by returning a tuple of the values themselves and their indices in the array, if none found, return an empty list
        :return:
        """
        pass