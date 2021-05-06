import unittest

from coding_question.interface import IntegerList


class TestIntegerList(unittest.TestCase):
    def test_instantiate_class(self):
        test = IntegerList()
        self.assertIsInstance(test, IntegerList)

    def test_add_element(self):
        test = IntegerList()
        element = 1
        test.add(element)
        self.assertIn(element, test.elements)

    def test_get_element(self):
        test = IntegerList()
        element = 1
        test.add(element)
        self.assertEqual(element, test.get(0))

    def test_get_remove_element(self):
        test = IntegerList()
        element = 1
        test.add(element)
        res = test.get_remove(0)
        self.assertEqual(element, res)
        self.assertFalse(test.elements)

    def test_insert_element(self):
        test = IntegerList()
        test.add(-1)
        index = len(test.elements)
        ins_element = 1
        test.insert(index, ins_element)
        self.assertEqual(ins_element, test.get(index))

    def test_remove_element(self):
        test = IntegerList()
        test.add(9)
        test.remove(0)
        self.assertFalse(test.elements)

    def test_clear_elements(self):
        test = IntegerList()
        test.add(9)
        test.clear()
        self.assertEqual(0, len(test.elements))

    def test_moving_average(self):
        test = IntegerList()
        test.elements = [1, 2, 3]
        last_n = len(test.elements)
        self.assertEqual(test.moving_average(last_n), 2)

    def test_moving_average_with_empty_structure(self):
        test = IntegerList()
        test.elements = []
        with self.assertRaises(IndexError):
            test.moving_average(1)

    def test_moving_average_with_lastn_zero(self):
        test = IntegerList()
        test.elements = [1, 2, 3]
        with self.assertRaises(ZeroDivisionError):
            test.moving_average(0)

    def test_moving_average_lastn_greater_structure_length(self):
        test = IntegerList()
        test.elements = [1, 2, 3]
        with self.assertRaises(ValueError):
            test.moving_average(4)
