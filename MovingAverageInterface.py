class MovingAverageInterface:
    """Data Structure Interface for Moving Average"""

    def __init__(self):
        """Initialize Moving Average data structure"""
        pass

    def getElements(self):
        """Get access to the elements of structure"""
        pass

    def addElements(self, element):
        """Add element to the structure.
        :param element
        """
        pass

    def calculateMovingAverage(self, lastN):
        """Moving average of the last 'N' elements added to the structure
        :type lastN: object
        """
        pass
