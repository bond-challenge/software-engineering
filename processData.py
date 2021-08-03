
import pandas as pd
from dataInterface import DataInterface 


# create a class to implement the inteface
class ProcessData(DataInterface):
    
    ''' The data structure from POS API is a list of json objects as shown below:-     
        {
          "POS_Transaction_ID": 3872073028328,
          "Transaction_Date": "2021-02-08 11:11:11",
          "Store_ID": 1234,
          "Dollar Quantity": 10,
          "Dollar Amount": 10
        }
    '''  
          
    data = []        
        
    def addElement(self, value):
        try:
            self.data.append(value)
            print('An event payload is added to the data structure')
        except Exception as e:
            print(e)

    def getElements(self):
        try:
            if len(self.data) == 0:
                raise IndexError("Data structure is empty.")
            else:
                return self.data
        except Exception as e:
            print(e)
    
    def getAverage(self, n):
        try:
            df = pd.DataFrame(self.data)
            df_sorted_date = df.sort_values(by=['Transaction_Date'])
            sales_list = df_sorted_date['Dollar Amount'].tolist()
            if len(sales_list) == 0:
                raise IndexError("Data structure is empty.")
            elif n > len(sales_list):
                raise ValueError("The number of elements in less than the N value supplied, an average cannot be calculated")
            elif n <= 0:
                raise ZeroDivisionError("n has to be greater than zero. ")
            else:
                #average = sum(self.data[(n * (-1))::1]) / n
                average = sum(sales_list[-n:]) / n
                print('\nAverage of last %d sales transaction is  $%.2f' %(n,average ))
        except Exception as e:
            print(e)



#create class instance 
myObject = ProcessData()
event1 = {
        "POS_Transaction_ID" : 3872073028328,
        "Transaction_Date" : "2021-02-08 11:11:11",
        "Store_ID":123484,
        "Dollar Quantity":10,
        "Dollar Amount": 55
         }
   
event2 = {
        "POS_Transaction_ID" : 4543872073028328,
        "Transaction_Date" : "2021-02-08 12:11:11",
        "Store_ID":123434,
        "Dollar Quantity":10,
        "Dollar Amount": 20
         }
   
event3 = {
        "POS_Transaction_ID" : 4543872073028328,
        "Transaction_Date" : "2021-02-08 13:11:11",
        "Store_ID":100145,
        "Dollar Quantity":10,
        "Dollar Amount": 30
         }
   
event4 = {
        "POS_Transaction_ID" : 4543872073028328,
        "Transaction_Date" : "2021-02-08 13:30:11",
        "Store_ID":100145,
        "Dollar Quantity":5,
        "Dollar Amount": 100
         }
   
event5 = {
        "POS_Transaction_ID" : 4543872073028328,
        "Transaction_Date" : "2021-02-08 15:30:11",
        "Store_ID":100145,
        "Dollar Quantity":15,
        "Dollar Amount": 50
         }
myObject.addElement(event1)
myObject.addElement(event2)
myObject.addElement(event3)
myObject.addElement(event4)
myObject.addElement(event5)
print("\nReading the elements: ", myObject.getElements())
myObject.getAverage(3)
