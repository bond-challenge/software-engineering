from dataStructureImplementation import MovingAverage
import unittest


class TestMovingAvg(unittest.TestCase):

    def test01_addNextCheckList(self):
        MovingAverage().add_next(10)
        values = self.numbers
        self.assertTrue(all(type(x) is int for x in values))

    def test02_checkifListhasStrings(self):
        MovingAverage().add_next(10)
        values = self.numbers
        self.assertFalse(all(type(x) is int for x in values))


if __name__ == '__main__':
    unittest.main()
