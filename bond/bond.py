
class MovingAverage:
    def __init__(self, N):
        """
        Initialize 
        return: None
        """
        self.elements = []
        self.average = 0
        self.N = N

    def add(self, element):
        """
        Apply the moving average and add
        the elements to the list
        return: None
        """
        if len(self.elements) == self.N:
            self.average = (self.N * self.average - self.elements[0] + element) / self.N
            self.elements = self.elements[1: len(self.elements)]
        else: 
            self.average = (len(self.elements) * self.average + element) / (len(self.elements) + 1)
        self.elements.append(element)   

    def lastNelements(self, n):
        """
        Get the last 'N' elements 
        return: List
        """
        if n > len(self.elements):
            raise ValueError("invalid input !")
        else:
            return self.elements[len(self.elements) - n: len(self.elements)]
    
    def calculate(self):
        """
        Return the moving average.
        return: integer
        """
        return self.average

if __name__ == '__main__':
    ma_3 = MovingAverage(3)
    ma_3.add(1)
    print(ma_3.calculate())
    ma_3.add(2)
    print(ma_3.calculate())
    ma_3.add(4)
    print(ma_3.calculate())
    ma_3.add(5)
    print(ma_3.calculate())