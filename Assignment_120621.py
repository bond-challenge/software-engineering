'''
Write an interface for a data structure that can
1. Provide average of last N elements added
2. Add elements to structure
3. Access the elements
'''

# import the interface/abstract class
import Assignment_Interface


# create a class to implement the inteface
class Assignment_120621(Assignment_Interface.MyInterface):
    var_List = []

    def GetAverage(self):
        try:
            var_N = int(input('To get the average of last N numbers, enter value for N : '))
            if var_N <= 0:
                print('Average = 0\n')
            else:
                print('Average of last ' + str(var_N) + ' elements is ' + str(sum(Assignment_120621.var_List[(var_N * (-1))::1]) / var_N)+'\n')
        except:
            print('\nOnly numbers are allowed')

    def AddElement(self):
        try:
            var_Add_element = int(input('Enter value to be added : '))
            Assignment_120621.var_List.append(var_Add_element)
            print('Element added to data structure\n')
        except:
            print('\nOnly numbers are allowed')

    def AccessElement(self):
        try:
            var_N = int(
                input('There are ' + str(len(Assignment_120621.var_List)) + 'elements, enter position of element you '
                                                                            'want to access : '))
            if var_N < 1 or var_N > len(Assignment_120621.var_List):
                print('No element exists at this position\n')
            else:
                print('Element at position ' + str(var_N) + ' is ' + str(Assignment_120621.var_List[var_N - 1])+'\n')
        except:
            print('\nOnly numbers are allowed')

#create class instance
obj_Assignment_120621 = Assignment_120621()

print('Options\n'
      '1 for Calculating Average of Last N numbers\n'
      '2 for Adding elements\n'
      '3 for accessing elements\n'
      '4 for displaying all elements in List\n'
      'E to exit')

val_input = 0
val_YN = ''

while val_input == 0:
    val_input = input('Enter your choice : ')

    if val_input == '1':

        if len(obj_Assignment_120621.var_List) == 0:
            print('No item has yet been added to data structure. Kindly add elements first')
            val_YN = input('Would you like to add (Y/N): ')
            if val_YN == 'Y' or val_YN == 'y':
                obj_Assignment_120621.AddElement()
            else:
                val_input = 0
        else:
            obj_Assignment_120621.GetAverage()
        val_YN = input('Would you like continue (Y/N): ')
        if val_YN == 'Y' or val_YN == 'y':
            val_input = 0
        else:
            break
    elif val_input == '2':
        obj_Assignment_120621.AddElement()
        val_YN = input('Would you like continue (Y/N): ')
        if val_YN == 'Y' or val_YN == 'y':
            val_input = 0
        else:
            break
    elif val_input == '3':
        if len(obj_Assignment_120621.var_List) == 0:
            print('No item has yet been added to data structure. Kindly add elements first')
            val_YN = input('Would you like to add (Y/N): ')
            if val_YN == 'Y' or val_YN == 'y':
                obj_Assignment_120621.AddElement()
            else:
                val_input = 0
        else:
            obj_Assignment_120621.AccessElement()
        val_YN = input('Would you like continue (Y/N): ')
        if val_YN == 'Y' or val_YN == 'y':
            val_input = 0
        else:
            break
    elif val_input == '4':
        print('\n Following are the elements in List')
        print(obj_Assignment_120621.var_List)
        print('\n')
        val_YN = input('Would you like continue (Y/N): ')
        if val_YN == 'Y' or val_YN == 'y':
            val_input = 0
        else:
            break
    elif val_input == 'E' or val_input == 'e':
        break
    else:
        val_input = 0

print('Exiting now....')
