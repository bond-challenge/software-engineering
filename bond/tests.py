from bond import MovingAverage

def test_add():
    """
    Test Case: 
    Validating the insert/append new elment into the list
    """
    ma = MovingAverage(2)
    ma.add(4)
    ma.add(5)
    assert str(ma.elements) == str([4, 5])

def test_accessElements():
  """
  Test Case:
  Validting the get functionality, accessing last n elements
  """
  ma = MovingAverage(2)
  ma.add(4)
  ma.add(5)
  ma.add(6)
  assert str(ma.elements) == str([3, 6])

def test_movingAverage():
  """
  Test Case: 
  Validting the moving average
  """
  ma = MovingAverage(3)
  ma.add(1)
  ma.add(2)
  ma.add(3)
  ma.add(4)
  assert ma.calculate() == 3

try:
  test_add()
  test_accessElements()
  test_movingAverage()
  print("Test Cases Passed !!")
except:
  raise AssertionError("Test Cases Failed !!!")
