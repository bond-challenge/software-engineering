class BaseInterface:
    def addElement(self, ele: int):
        """add element to the DS"""
        pass

    def getDataStructure(self):
        """returns underlying DS"""
        pass

    def avgLastMoving(self, lastN: int):
        """returns moving average of last N elements"""
        pass


class MovingAverageInterface(BaseInterface):

    def __init__(self):
        self.vallist = []

    def addElement(self,  ele: int):
        self.vallist.append(ele)

    def getDataStructure(self):
        return self.vallist

    def avgLastMoving(self, lastN: int):
        return (sum(self.vallist[-lastN:])/lastN)



def main():
    print("Test Interface")
    test = MovingAverageInterface()
    test.addElement(1)
    test.addElement(2)
    test.addElement(3)
    test.addElement(4)
    print(test.getDataStructure())
    print(test.avgLastMoving(2))
    print(test.avgLastMoving(3))
    print(test.avgLastMoving(1))
    test.addElement(5)
    print(test.getDataStructure())
    print(test.avgLastMoving(2))

if __name__ == "__main__":
    main()
