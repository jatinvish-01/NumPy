'''
array_name[index]  for id
array_name[row, column] 2d
'''


import numpy as np

arr = np.array([1,2,3,4,5,6])
print(arr[3])
print(arr[-1]) # last element


# Slicing 
'''
syntax:  array_name[start: stop: step]
arr[start: end] -> start to end -1
negative  step -1 reverse
'''

arr2 = np.array([2,4,6,8,10,12,14])
print(arr2[0:4])
print(arr2[:5]) #start form 0 to 4
print(arr2[::2]) # every second element
print(arr2[::-1]) # reverse the element