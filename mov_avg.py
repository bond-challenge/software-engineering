##Script Name: mov_avg.py
##Created By:Vinay K

from abc import ABC, abstractmethod
class Interface(ABC):
    """
        This program is to calculate moving average for N elements. 
        Elements are defined as numeric values in this program.
        The data structure used to store the elements is a list. 
    """
    @abstractmethod
    def data_struct(self):
       "method to add elements"
       pass
    @abstractmethod
    def get_access(self,elist):
       "method to access elements"
       pass
    @abstractmethod
    def run_avg(self, elist):
       "method to calculate running average"
       pass
class calc(Interface):
    
    elementslist = list()

    def data_struct(self):
        
        while (True):
            inputvalue1 = input('Add a numeric value to the list: \n To stop enter exit: ')
            
            if inputvalue1 == 'exit': break
            try:
                value1 = float(inputvalue1)
            except ValueError:
                print("Value entered in Invalid. Enter numeric value only")
                continue
            self.elementslist.append(value1)
        print(self.elementslist)
        
    def get_access(self,elementslist):
        print("Contents of the data structure is:\n",elementslist)
        while (True):
            inputvalue2 = input('Enter a integer value to the access the elements of the list: \n To stop enter exit: ')
            if inputvalue2 == 'exit': break
            try:
                value2 = int(inputvalue2) - 1
            except ValueError:
                print("Value entered in Invalid. Enter integer value only")
                continue
            if len(elementslist) > 0: 
                try:
                    print("Accessed value is",elementslist[value2])
                except IndexError:
                    print("Entered index is out of range")
                    continue
            else:
                print("Data Structure is empty")
                s.data_struct()
    
    def run_avg(self,elementslist):
        
        while(True):
            inputvalue3 = input('Enter a N value to calculate average: \n To stop enter exit: ')
            if inputvalue3 == 'exit': break
            try:
                value3 = int(inputvalue3) + 1
            except ValueError:
                print("Value entered in Invalid. Enter integer value only")
                continue
            if len(elementslist) > 0:
                average = sum(elementslist[-1:-value3:-1]) / len(elementslist[-1:-value3:-1])
                print('Average of Last N elements added:', average)
            else:
                print("list is empty. Add values")
                s.data_struct()
        
s = calc()
s.data_struct()
s.run_avg(s.elementslist)
s.get_access(s.elementslist)