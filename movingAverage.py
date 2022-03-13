class MovingAverages:
    def add(self, ele: int):
        """add element"""
        pass

    def get(self):
        """returns underlying ds"""
        pass

    def averageLastMoving(self, lastN: int):
        """returns undelying list"""
        pass

import queue

class MovingAverageswithQueue(MovingAverages):

    #Use LIFO Queue
    def __init__(self):
        self.que = queue.LifoQueue()
    
    def add(self,  ele: int):
        self.que.put(ele)

    def get(self):
        return self.que

    def averageLastMoving(self, lastN: int):
        movingSum = 0
        for i in range(lastN):
            movingSum += self.que.get()
        return (movingSum/lastN)



def main():
    print("Test Queue")
    mv = MovingAverageswithQueue()
    mv.add(11)
    mv.add(12)
    mv.add(13)
    mv.add(14)
    print(mv.averageLastMoving(2))

if __name__ == "__main__":
    main()