import random
 

class movingavg:
 
    
    def __init__(self):
         
        
        self.list1 = []
 
        
        self.hashd = {}

    
    def add(self, x):
         
        
        if x in self.hashd:
            return
 
        
        s = len(self.list1)
        self.list1.append(x)
 
        
        self.hashd[x] = s
 
    
    def remove(self, x):
         
        
        index = self.hashd.get(x, None)
        if index == None:
            return
        
        del self.hashd[x]
 
        
        size = len(self.list1)
        last = self.list1[size - 1]
        self.list1[index], \
        self.list1[size - 1] = self.list1[size - 1], \
                             self.list1[index]
 
        
        del self.list1[-1]
 
        
        self.hashd[last] = index
 
    
    def getRandom(self):
         
         
        
        index = random.randrange(0, len(self.list1))
 
        
        return self.list1[index]
 
   
    def search(self, x):
        return self.hashd.get(x, None)
 

if __name__=="__main__":
    res = movingavg()
    res.add(10)
    res.add(20)
    res.add(30)
    res.add(40)
    print(res.search(30))
    res.remove(20)
    res.add(50)
    print(sum(res.list1)/int(input("enter the N elements for moving average: ")))
