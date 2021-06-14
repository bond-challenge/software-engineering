from CodingQuestion.Interface import LastNElements
import numpy
from pyspark.sql import SparkSession, toPandas
import time
import sys


class RunLastN(LastNElements):

    def __init__(self, tbl_name):
        self._spark = (SparkSession.builder
                    .appName('Bond Challenge')
                    .config("hive.exec.dynamic.partition", "true")
                    .config("hive.exec.dynamic.partition.mode", "nonstrict")
                    .config("spark.driver.memory", "15g")
                    .config("spark.sql.autoBroadcastJoinThreshold", -1)
                    .enableHiveSupport()
                    .getOrCreate()
                    )
        self.tbl = tbl_name

    def moving_avg(self, element: str, N: int) -> float:
        '''provide the moving average of the last N elements added'''

        #Query element
        df = self._spark.sql('''select element from %s'''%self.tbl)

        #Transfer the result to a python list
        lst = df.toPandas()['element'].values.tolist()

        #Calculate the moving average of the last N elements
        cumsum = numpy.cumsum(numpy.insert(lst, 0, 0)) 
        result = (cumsum[N:] - cumsum[:-N]) / float(N)

        _index = lst.index(element)
        return (result[_index])
    
    def add_element(self, element: str) -> None:
        '''add elements to the structure'''

        add_year = time.strftime("%Y")
        add_month = time.strftime("%m")
        add_day = time.strftime("%d")

        query = '''insert into table %s
                partition (add_year=%s, add_month=%s, add_day=%s)
                VALUES (%s, current_timestamp());''' %(self.tbl, add_year, add_month, add_day, element)
        self._spark.sql(query)

        print ('Element %s inserted at time %s' %(x, time.strftime("%Y-%m-%d-%H-%M-%S")))

    def read_element(self, x: str) -> None:
        '''get access to the elements'''
        query = '''select * from %s where element = %s''' %(self.tbl, x)
        self._spark.sql(query)

        print ('Query the elemenet from table %s' %(self.tbl))


if __name__ == '__main__':
    if sys.argv[3]:
        N = sys.argv[3]
    if sys.argv[2]:
        element = sys.argv[2]
    
    tbl_name = 'Bond_table' #This should not be hard coded in real case.
    run_N = RunLastN(tbl_name)

    if sys.argv[1] == 'avg':
        run_N.moving_avg(element, N)
    elif sys.argv[1] == 'add':
        run_N.add_element(element)
    elif sys.argv[1] == 'read':
        run_N.read_element(element)