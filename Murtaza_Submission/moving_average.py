################################################
####### Submitted by: Murtaza Badshah ##########
############# Date: 11/30/2021 #################
################################################

import numpy as np #Importing the numpy library to help round my list values to 2 decimal places

# Defined my add values method, here the method takes the numbers list as input
def add_Values(numbers):
    # Requesting the user to define the number of values to add to array
    list = int(input("How many values would like to add to the list?: "))
    j = 1
    for i in range(list+2): # loop based on defined number
        while j < i:
            try: # Only allow int values for entry
                response = int(input(f"Add numerical value {j}: "))
                numbers.append(response) # adds the number to array list
                j += 1
            except ValueError:
                print("please enter integer value only")
                continue


# Defined the moving average calculation
# Code referenced from here: https://www.kite.com/python/answers/how-to-find-the-moving-average-of-a-list-in-python
def movingAvg(numbers):
    # allowing the user to define the N size of the window
    window_size = int(input("Please enter the window size: "))

    i = 0 #initialzied the i as 0 for loop
    moving_avg = [] # initilazed empty array list to store the avg values

    # While loop checks if i is less than the length of array list minus the window size plus 1
    while i < len(numbers) - window_size +1:
        # defined new variable that's a shallow copy of the numbers array list
        this_window = numbers[i : i + window_size]
        # this line helps in calculating the average by taking the sum of the shallow copy and dividing by window size.
        window_avg = sum(this_window) / window_size
        # add the calculated average to the empty array initialized above.
        moving_avg.append(window_avg)
        i += 1 #Increment
        results = list(np.around(np.array(moving_avg), 2)) #Numpy code used to round values in the list.

    print(results)
    input("Press enter to go back to main menu!")

# This method print the array list
def printList(numbers):
    if bool(numbers) == False:
        print("Array is empty! Please add values to array list")
    else:
        print(numbers)

    input("Press enter to go back to main menu!")

if __name__ == '__main__':
    numbers = []
# Main menu GUI Interface
    while True:
        print("=======================================================")
        print("--------Welcome to Moving Average Calculator !---------")
        print("*******************************************************")
        print("       Please read the instructions carefully.         ")
        print("********   1. Add values to list              *********")
        print("********   2. Print array list                *********")
        print("********   3. Calculate moving average        *********")
        print("********   4. Exit program                    *********")
        print("*******************************************************")

        selection = input("Please enter the appropriate number for the option: ")


        if selection == "1":
            add_Values(numbers)
        elif selection == "2":
            printList(numbers)
        elif selection == "3":
            movingAvg(numbers)
        elif selection == "4":
            exit()
            break
        else:
            print("Incorrect input please try again!")



