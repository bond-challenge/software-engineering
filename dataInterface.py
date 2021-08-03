from abc import ABC, abstractmethod


class DataInterface(ABC):

    @abstractmethod
    def addElement():
        '''
        This function will add a single element to a data structure
        returns nothing'''
        pass
    
    @abstractmethod
    def getElements():
        '''
        Returns all the elements inside data structure
        '''
        pass
        
    @abstractmethod   
    def getAverage():
        '''
        Returns moving average of last N elements'''
        pass
       


