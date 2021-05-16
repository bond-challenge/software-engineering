import unittest

from moving_average.moving_average_iterable import MovingAverageIterable
from moving_average.moving_average_list import MovingAverageList


class TestMovingAverageList(unittest.TestCase):

    def test_get_class_instance(self):
        actual = MovingAverageList(2)
        self.assertIsInstance(actual, MovingAverageIterable)
        self.assertIsInstance(actual, MovingAverageList)

    def test_n_last_elements_must_be_higher_than_zero(self):
        with self.assertRaises(ValueError):
            MovingAverageList(0)

    def test_append_and_get_one_element(self):
        actual = MovingAverageList(2)
        actual.append(10)
        expected_len = 1
        self.assertEqual(expected_len, len(actual.get_elements()))

    def test_append_and_get_multiple_elements(self):
        actual = MovingAverageList(2)
        actual.append(10)
        actual.append(20)
        expected_len = 2
        elements = actual.get_elements()
        self.assertEqual(expected_len, len(elements))
        self.assertEqual(elements, [10, 20])

    def test_get_moving_average_of_no_elements(self):
        actual = MovingAverageList(1)
        self.assertIsNone(actual.get_moving_average())

    def test_get_moving_average_of_one_element(self):
        actual = MovingAverageList(1)
        element = 10
        actual.append(element)
        self.assertEqual(element, actual.get_moving_average())

    def test_get_moving_average_of_less_than_n_last_elements(self):
        n_last_elements = 5
        actual = MovingAverageList(n_last_elements)
        element1 = 10
        element2 = 20
        expected_moving_average = (element1 + element2) / 2
        actual.append(element1)
        actual.append(element2)
        self.assertEqual(expected_moving_average, actual.get_moving_average())

    def test_get_moving_average_of_multiple_elements(self):
        n_last_elements = 2
        actual = MovingAverageList(n_last_elements)
        element1 = 10
        element2 = 20
        element3 = 30
        expected_moving_average = (element2 + element3) / n_last_elements
        actual.append(element1)
        actual.append(element2)
        actual.append(element3)
        self.assertEqual(expected_moving_average, actual.get_moving_average())
