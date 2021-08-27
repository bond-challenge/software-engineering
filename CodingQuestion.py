class MovingAverageInterface:
    """Interface"""

    def __init__(self):
        """Initalize data structure"""
        pass
    def getElements(self):
        """Get access to the elements in the data structure"""
        pass
    def addElement(self, e):
        """Add an element to the structure"""
        pass
    def calculateMovingAverage(self, lastN):
        """Calculate the moving average of the lastN elements added to the structure"""
        pass

class MovingAverage(MovingAverageInterface):
    """This class implements a list where numeric value element can be added, 
    accessed and can calculate moving average of the last added N elements
    """

    def __init__(self, elements=[]):
        """Initiates the list to store elements"""
        self.elements = elements

    def getElements(self):
        """Return the list of elements stored"""
        return self.elements

    def addElement(self, e):
        """Append an element to list"""
        self.elements.append(e)

    def calculateMovingAverage(self, lastN):
        """Calculate the moving average of the lastN elements added to list"""
        total_len = len(self.elements)
        if lastN > total_len:
            raise IndexError("Input number N out of range!!")
        else:
            movAvg = sum(self.elements[lastN*-1:])/lastN

        return movAvg

if __name__ == "__main__":
    pass
    # ma = MovingAverage()
    # ma.addElement(1)
    # ma.addElement(2)
    # print(ma.getElements())
    # print(ma.calculateMovingAverage(2))
    # print(ma.calculateMovingAverage(1))
    # print(ma.calculateMovingAverage(3))