import numpy as np
# array = np.array([1,2,3,4])
# array*=2
# print(array)
# print(type(array))
""" MultiDimensional Array
array =np.array(
[
    [['A', 'B','C'],['D','E','F'],['G','H', 'I']],
                 [['J', 'K','L'],['M','N','O'],['P','Q', 'R']],
                 [['S', 'T','U'],['V','W','X'],['Y','Z', ' ']]

                ])
word = array[0,0,0] + array[2,0,0] +array[2,0,0]
print(word)

"""
## array slicing
array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

#array[start;end:step]
print(array[0:4:2])



