import Interface


class CalculateMovingAverageofLastN(Interface.Interface):
    def __init__(self):
        self.array = []
        self.moving_average_snapshot = []

    def _check_input_type(self, element=None):
        """
        Check the input to be a list of integers or a single integer
        :param element: List[int]
        :return: Boolean
        """
        if isinstance(element, list):
            return all([isinstance(e, int) for e in element])

    def add_element(self, element=None):
        """
        Add elements to the array only if the input is valid. Return the array's current state if the input is invalid or empty.
        :param element: List[int]
        :return: List[int]
        """
        if self._check_input_type(element) is True:
            start = 0
            while start < len(element):
                self.array.append(element[start])
                start += 1

        return self.array

    def get_last_N_moving_average(self, N):
        """
        Calculate the average of the last N elements within the non-empty array, and record the corresponding inputs
        :param N: int
        :return: int, or "N is out of bound" if invalid N
        """
        record = {}
        if N > len(self.array) or N < 1:
            return "N is out of bound"
        else:
            lastN = self.array[len(self.array) - N:]
            avg = sum(lastN) / N
            record["N"] = N
            record["Last N elemnts"] = lastN
            record["Avg"] = avg

            self.moving_average_snapshot.append(record)

            return self.moving_average_snapshot

    def access_elements(self, elements):
        """
        Access the elements in the array by returning a tuple of the values themselves and their indices in the array, if none found, return an empty list
        :param elements: List[int]
        :return: List[tuple], or "Only a list of integers or a single integer allowed!" if invalid elements
        """
        coordinates = []
        try:
            for i, v in enumerate(self.array):
                if v in elements:
                    coordinates.append((i, v))
            return coordinates
        except TypeError:
            print("Only a list of integers or a single integer allowed!")


if __name__ == '__main__':
    ds = CalculateMovingAverageofLastN()
    ds.add_element([1, 2, 3])
    # print(ds.get_last_N_moving_average(3))
    # print(ds.get_last_N_moving_average(5))
    # print(ds.array)
    ds.add_element([4, 5, "a"])
    print(ds.array)
    # print(ds.get_last_N_moving_average(3))
    # print(ds.get_last_N_moving_average(5))
    # print(ds.access_elements([1, -1]))
    # ds.add_element([2, 4, 6])
    # print(ds.get_last_N_moving_average(3))
    # print(type([1,2,3]))
