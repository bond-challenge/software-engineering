from movingavg import MovingAverageInterface


class MovingAverage(MovingAverageInterface.MovingAverageInterface):
    """This class implements a list where numeric element can be added,
    accessed and can calculate moving average of the last added N elements.
    """

    def __init__(self, lastN: int, elements=[]):
        """Initiates:
         1. elements: list to store elements
         2. elementsLen: number of items in elements list
         3. lastN: number of elements from the end 'N' used to calculate moving average
         4. queueWindowSize: number of current items in queue. Will be less than or equal to lastN
         5. movingSumLastN: moving sum of last N element of the list. calculated using queue.

        :type lastN: int
        :type elements: list
        """
        self.elements = elements
        self.elementsLen = len(elements)
        self.lastN = lastN
        self.queueWindowSize = 0
        self.movingSumLastN = 0
        self.setInitVariables(lastN) # initializes values for queue, queueWindowSize, movingSumLastN


    def setInitVariables(self, lastNAvgWindow):
        """
        Sets values for queue, queueWindowSize and movingSumLastN
        :param lastNAvgWindow:
        """
        self.queueWindowSize = 0
        self.movingSumLastN = 0
        if self.elementsLen <= lastNAvgWindow:
            for e in self.elements:
                self.movingSumLastN += e
                self.queueWindowSize += 1
        else:
            # Stores last N elements in the queue and do sum for last N elements
            for e in self.elements[self.elementsLen - lastNAvgWindow:]:
                self.movingSumLastN += e
                self.queueWindowSize += 1
    # End setInitVariables function


    @property
    def getElements(self):
        """Returns the list of elements stored in the data structure
        :return: elements list
        """
        return self.elements
    # End getElements function


    def addElement(self, element):
        """Performs below actions in the Moving Average data structure:
            1. Append an element to list in data structure
            2. update moving window queue elements by doing push and pop
            3. updates moving sum of last N elements in the list
        :param element
        """
        if self.queueWindowSize == self.lastN:
            # If queueWindow has N elements then pop first element and push new element to the movingSumLastN
            firstElement = self.elements[self.elementsLen-self.queueWindowSize]
            self.movingSumLastN += (element - firstElement)
        else:
            # Else push operation
            self.movingSumLastN += element
            self.queueWindowSize += 1

        self.elements.append(element)
        self.elementsLen += 1
    # End addElement function


    def calculateMovingAverage(self, lastN: int):
        """Calculate the moving average of the lastN elements added to list.
        Implementation Logic:
            If lastN is equal to the lastN window size defined when object was created it will optimally calculate average.
            If the lastN (last N elements used for moving average) is different from what was specified when object was created it will have to recalculate the sum.
            To change the lastN(number of elements in moving average) use function  changeLastN. After first run it will optimally calculate moving average.
        :param lastN: int
        :return:
        """
        if lastN > self.elementsLen:
            raise IndexError("Data structure cannot calculate average as it does not have N elements. N is out of range!!")
        elif self.lastN == lastN:
            return self.movingSumLastN/lastN
        else:
            return sum(self.elements[lastN * -1:]) / lastN
    # End calculateMovingAverage function


    def changeLastN(self, newLastN: int):
        """Change the moving window length to optimally calculate average."""
        self.lastN = newLastN
        self.setInitVariables(newLastN)
    # End changeLastN function


if __name__ == "__main__":
    # pass

    sampleList = [i for i in range(1000)] # initial list of elements
    ma = MovingAverage(15, sampleList) # create object of moving average data structure which expects 2 parameters (lastNWindow, elementsList[optional])
    print(ma.calculateMovingAverage(15)) # calculates moving average for last 15 elements in the list
    print(ma.movingSumLastN)
    ma.addElement(1)
    ma.addElement(2)
    print(ma.movingSumLastN)
    print(ma.calculateMovingAverage(15))
    ma.addElement(1)
    ma.addElement(2)
    ma.addElement(5)
    print(ma.getElements)
    print(ma.calculateMovingAverage(2))
    print(ma.calculateMovingAverage(1))
    print(ma.calculateMovingAverage(3))
    ma.changeLastN(5) # changes the moving average window from 15 to 5

    print(ma.getElements)
    print(ma.calculateMovingAverage(5))
    print(ma.calculateMovingAverage(2))
