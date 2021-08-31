class MovingAverageInterface():
    ''' 
        Moving average interface which defines methods such as
        addElem : add to the object
        getElem : get an object
        getMovingAvg :  get the moving averange of last N elemets

    '''
    def get_elem(self): pass
    def add_elem(self, num): pass
    def get_moving_avg(self, n_elem): pass


class MovingAverage(MovingAverageInterface):
    '''
        This class implements interfact of MovingAverageInterface
    '''
   
    def __init__(self):
        '''
            initalize stream_numbers as lis
        '''
        self.stream_numbers = []

    def add_elem(self,num)->list:
        '''
            add elements to the stream_number list
        '''
        return self.stream_numbers.append(num)

    def get_elem(self, idx=None)->list:
        '''
            get access of stream_numbers 
        '''
        if idx == None:
            return self.stream_numbers

    def get_moving_avg(self, n_elem: int)->float:
        '''
            get the average of last n_elemnts of stream_numbers. returns result as float

        '''
        if len(self.stream_numbers) > n_elem:
            return sum (self.stream_numbers[-n_elem:])/n_elem
        return sum(self.stream_numbers)/n_elem
         


if __name__ == "__main__":
    mv = MovingAverage()
    # add elements to the list
    mv.add_elem(2)
    mv.add_elem(1)
    mv.add_elem(3)
    mv.add_elem(4)
    mv.add_elem(5)
    # get access to the elements
    print(mv.get_elem())
    # checks if list is empty
    if len(mv.stream_numbers) :
        # get last element size from user input
        n_elem = int(input(f'Enter size of last N Element. Size should be between {range(1,len(mv.stream_numbers))} : '))
        # try to get user input until get the size in correct range
        while n_elem not in range (1,len(mv.stream_numbers)+1):
            n_elem = int(input(f'Enter size of last N Element. Size should be between {range(1,len(mv.stream_numbers))} : '))
        # find moving average of last N elements
        print(f'Moving avg of last {n_elem} elements - {mv.get_moving_avg(n_elem)}')
       