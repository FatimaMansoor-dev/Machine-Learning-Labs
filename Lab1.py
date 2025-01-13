'''  Question 1: Create an ndarray using the following data. Write the code and outputs.
 Data1 = 1 3 9 12 18, Data2 = 1 5 2 0  ,  Data3 = '7' '6' ,  Data4 = 11 52 20 50
                              3 6 4 7             '5' '4'            34 61 43 17
                                                  '3' '2'

'''

import numpy as np

d1 = [1, 3, 9, 12, 18]
d2 [[1, 5, 2, 0],[3, 6, 4, 7]]
d3 = [[['7', '6'], ['5', '4'], ['3', '2']]]
d4 = [[11, 52, 20, 50], [34, 61, 43, 17]]

dataset = [d1, d2, d3, d4]

def create_ndarray(data):
  return np.array(data)
  
for data in dataset:
  create_ndarray(data)
