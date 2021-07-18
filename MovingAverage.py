import random
'''
    Class implementing data structure to handle last N element and Moving average
'''
class LastN:
    '''
        Function Initializing buffer list contianing last N numbers
        Input: 
            n: number of Elements
    '''
    def __init__(self, n):
        
        self._n = n
        
        #buffer with default value zero
        self._buf = [None] * n
        
        # Current index of element last added in buffer
        self._index = 0
        
        # Track if buffer is full till n
        self._valid = 1
        
        # Moving average
        self._average = 0 
    
    '''
        Function adds Element to buffer
        Input: 
            elem: Element to be added in the buffer
    '''
    def addElement(self, elem):
        
        # check if non numeric input is added
        if str(elem).isalpha():
            print('Invalid Input')
            return False
        
        # store existing value in temp variable for average calculation
        temp =self._buf[self._index]
        
        #add Element to buffer
        self._buf[self._index] = elem
        
        #increase current index
        self._index += 1
        
        # Calculate runnning average
        self._average=(self._average*(self._valid-1)+elem)/min(self._valid,self._n)
        
        #Restart index to zero if reached max cap of N element
        if self._index == self._n:
            self._index = 0
            
        #Increment valid variable upto n
        if self._valid <= self._n:
            self._valid += 1
        
        #Average calculation
        else:
            self._average-=temp/self._n
    
            
    '''
        Function retrives element form buffer by index
        Input: 
            index: index for which element is to be found
    '''
    def getElement(self,index):
        
        # Check if input is out of bound
        if not index<self._n:
            return None
        
        # Check if input is less then buffer size 
        if self._valid<=self._n:
        
             # Check if index is out elements inserted
            if not self._index>index:
                return None
             
                # Return element
            return self._buf[index]
        
        # Return element        
        return self._buf[(self._index+self._n+index)%self._n]
    
    '''
        Function returns moving average
    '''
    
    def getAverage(self):
        return self._average
   
#*********** Testing *******************
#A = LastN(5)
#for a in [2, 1, 8, 4, 7, 3]:   
#    A.addElement(a)
#    print(f'Average {A.getAverage()}')
#    i = random.randint(0, 4)
#    print(f'Index {i}')
#    print(f'Element {A.getElement(i)}')