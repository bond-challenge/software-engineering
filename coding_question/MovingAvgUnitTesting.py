import unittest

from MovingAverageOfLastN import MovingAverageOfLastN

class TestMovingAvg(unittest.TestCase):

    def test_addElements_checkIntergerList(self):
        print('test_addElements_checkIntergerList')
        test = MovingAverageOfLastN().addElements()
        self.assertTrue(all(type(x) is int for x in test))

    def test_addElements_checkAlphaNumericList(self):
        print('test_addElements_checkAlphaNumericList')
        test = MovingAverageOfLastN().addElements()
        self.assertFalse(all(type(x) is int for x in test))


    def test_getLastN_NegativeValueInput(self):
        print('test_getLastN_NegativeValueInput')
        elementsList = [4,3,2,1]
        test = MovingAverageOfLastN()
        if test.getLastN(elementsList) != None:
            self.assertTrue(str(test.getLastN(elementsList)).isnumeric(), "Value is not an Integer")
            self.assertTrue(test.getLastN(elementsList) > 0)

  
    def test_getLastN_MoreThanElementCountInput(self):
        print('test_getLastN_MoreThanElementCountInput')
        elementsList = [4,3,2,1]
        test = MovingAverageOfLastN()
        if test.getLastN(elementsList) != None:
            self.assertTrue(str(test.getLastN(elementsList)).isnumeric(), "Value is not an Integer")
            self.assertTrue(test.getLastN(elementsList) <= len(elementsList))

        self.assertTrue(str(test.getLastN(elementsList)).isnumeric(), "Value is not an Integer")
        self.assertTrue(test.getLastN(elementsList) < len(elementsList))

    def test_getMovingAvg_LastNValue3_AllInt(self):
        print('test_getMovingAvg_LastNValue3_AllInt')
        elementsList = [5,4,3,2,1]
        lastN = 3
        test = MovingAverageOfLastN()
        self.assertEqual(test.getMovingAvg(lastN,elementsList), [4.0, 3.0, 2.0])
    
    def test_getMovingAvg_LastNValue3_AlphaNumeric(self):
        print('test_getMovingAvg_LastNValue3_AlphaNumeric')
        elementsList = [5,4,'C',2,1]
        lastN = 3
        test = MovingAverageOfLastN()
        self.assertNotEqual(test.getMovingAvg(lastN,elementsList), [4.0, 1.0, 2.0], "")


if __name__ == '__main__':
    unittest.main()
    