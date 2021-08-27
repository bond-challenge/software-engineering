'''
Class to calculate moving average of last N elements assed to a data structure
Data Structure used: List
Adding elements: by appending elements to the list in a loop
Access to elements: by providing numeric ocation of the element
Display List: Listing all values in the list
Moving Average: Creating a faux ring that loops through the elements > calculates the average for each set of 3 elements from element[0] to element[n]
'''

# import Interface Class
import DataStructureInterface


#implement Class
class MovingAverageOfLastN(DataStructureInterface.DataStructureInterface):
    listElements = []

    def addElements(self):
        try:
            print('How many elements would you like to add???')
            listSize = int(input('Total number of elements to be added: '))
            if listSize > 0:
                i = 0
                while i < listSize:
                    elementInput = int(input('Add element value' + str([i])+': '))
                    MovingAverageOfLastN.listElements.append(elementInput)
                    i += 1
                print(str(listSize) + ' elements are added to the list. \n')
                print('List is ready for calculating Moving Average. List Value: ' +  str(MovingAverageOfLastN.listElements))
                return MovingAverageOfLastN.listElements
            else:
                print('Please enter a positive integer value')
        
        except ValueError as err :
            print(str(err).capitalize() + '. Not a valid entry. Review Code where elements are being added to the List [addElements()]. Exiting...' )
            exit()

    def getLastN(self, elementsList):
            lastN = int(input('Enter LastN elements window to calculate moving average (should be <= ' + str(len(elementsList)) + ') : '))
            if lastN > 0 and lastN <= len(elementsList):
                return lastN
            else: 
                print('Oops! A positive integer value is required that is less than '+ str(len(elementsList)) + ' the count of elements in the list. Exiting...')
                exit()
        

    def getMovingAvg(self, N, listElements):
        try:
            i = 0
            movingAverageOfLastNElements = []
            while i < len(listElements) - N + 1:
                selectedElements = listElements [i : i + N]
                selectedElementsAvg = sum(selectedElements) / N
                movingAverageOfLastNElements.append(selectedElementsAvg)
                i += 1
            return movingAverageOfLastNElements
        except:
            print('Please review your list.')

    def accessElement(self, listElements):
        try:
            print('Length of available list: '+ str(len(listElements)))
            elementLocation = int(input('Enter which element you want to access. (Integer value that is <= ' + str(len(listElements)) + ') : '))
            if elementLocation >= 1 and elementLocation <= len(listElements):
                return listElements[elementLocation - 1]
            else:
                raise ValueError (
                'Value entered is not between 1 - ' + str(len(listElements))
            )
        except:
            print('Value entered is not between 1 - ' + str(len(listElements)))

#Instatiation of class
obj = MovingAverageOfLastN()

#Call method to add X elements to the list
elementsList = obj.addElements()
#Call method to get the Window of Last N elements
windowForLastNElements = obj.getLastN(elementsList)

#Call method to calculate the moving Average (rolling average)
movingAverageOfLastNElements = obj.getMovingAvg(windowForLastNElements,elementsList)
print('Moving Average List for cumulative window of Last N Elements : ' +  str(movingAverageOfLastNElements))

#Call to access a particulat element from the list
accessedElementValue = obj.accessElement(elementsList)
if accessedElementValue != None:
    print('Element found at the entered location is ' + str(accessedElementValue))

