import abc
from typing import List


class DataStructureInterface(abc.ABC):
    @classmethod
    def addElements(self):
        '''
        This function is for the user to create the list with user element input

        :return: DataStructure (List)
        '''
        pass
    
    @classmethod
    def getLastN(self, listElements: list):
        '''
        This function will calculate moving average of last N elements

        :return: Nothing
        '''
        pass

    @classmethod
    def getMovingAvg(self, N: int, listElements: list):
        '''
        This function will calculate moving average of last N elements

        :return: Nothing
        '''
        pass

    @classmethod
    def accessElement(self,listElements: list):
        '''
        This function will calculate moving average of last N elements

        :return: Nothing
        '''
        pass

    
    
    