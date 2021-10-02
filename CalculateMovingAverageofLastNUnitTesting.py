import unittest
from CalculateMovingAverageofLastN import CalculateMovingAverageofLastN


class TestCalculateMovingAverageofLastN(unittest.TestCase):

    def test_add_element_for_invalid_input(self):
        expected = [[], [], []]
        inputs = [[], None, [1, 2, 3, 4, 5, 6, 7, -1, "a"]]
        test = CalculateMovingAverageofLastN()
        result = [test.add_element(i) for i in inputs]
        self.assertEqual(result, expected)

    def test_get_last_N_moving_average_for_N_out_of_bound(self):
        expected = "N is out of bound"
        test = CalculateMovingAverageofLastN()
        test.add_element([1, 2, 3, 4, 5])
        N = 6
        self.assertEqual(test.get_last_N_moving_average(N), expected)

    def test_get_last_N_moving_average_for_working_snapshot(self):
        firstN = 3
        secondN = 5
        test = CalculateMovingAverageofLastN()
        test.add_element([1, 2, 3])
        self.assertEqual(test.get_last_N_moving_average(firstN), [{'N': 3, 'Last N elemnts': [1, 2, 3], 'Avg': 2.0}])
        self.assertEqual(test.get_last_N_moving_average(secondN), "N is out of bound")
        test.add_element([4, 5, 6])
        self.assertEqual(test.get_last_N_moving_average(firstN), [{'N': 3, 'Last N elemnts': [1, 2, 3], 'Avg': 2.0},
                                                                  {'N': 3, 'Last N elemnts': [4, 5, 6], 'Avg': 5.0}])
        self.assertEqual(test.get_last_N_moving_average(secondN), [{'N': 3, 'Last N elemnts': [1, 2, 3], 'Avg': 2.0},
                                                                   {'N': 3, 'Last N elemnts': [4, 5, 6], 'Avg': 5.0},
                                                                   {'N': 5, 'Last N elemnts': [2, 3, 4, 5, 6],
                                                                    'Avg': 4.0}])

    def test_get_last_N_moving_average_for_invalid_input(self):
        firstN = 3
        secondN = 5
        test = CalculateMovingAverageofLastN()
        test.add_element([1, 2, 3])
        self.assertEqual(test.get_last_N_moving_average(firstN), [{'N': 3, 'Last N elemnts': [1, 2, 3], 'Avg': 2.0}])
        self.assertEqual(test.get_last_N_moving_average(secondN), "N is out of bound")
        self.assertEqual(test.array, [1, 2, 3])
        test.add_element([4, 5, "a"])
        self.assertEqual(test.get_last_N_moving_average(firstN), [{'N': 3, 'Last N elemnts': [1, 2, 3], 'Avg': 2.0},
                                                                  {'N': 3, 'Last N elemnts': [1, 2, 3], 'Avg': 2.0}])
        self.assertEqual(test.array, [1, 2, 3],
                         msg="Second input is invalid, so the original array stays the same with a second identical entry in the snapshot")

    def test_access_elements_for_multiple_same_value_elements(self):
        expected = [(0, 1), (1, 2), (3, 1)]
        test = CalculateMovingAverageofLastN()
        test.add_element([1, 2, 3, 1, 5])
        interested = [1, 2]
        self.assertEqual(test.access_elements(interested), expected)


if __name__ == '__main__':
    unittest.main()
