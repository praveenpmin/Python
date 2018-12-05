# The term broadcasting refers to the ability of NumPy to treat arrays of different shapes during 
# arithmetic operations. Arithmetic operations on arrays are usually done on corresponding elements. 
# If two arrays are of exactly the same shape, then these operations are smoothly performed.

import numpy as np 

a = np.array([1,2,3,4]) 
b = np.array([10,20,30,40]) 
c = a * b 
print (c)

import numpy as np 
a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]]) 
b = np.array([1.0,2.0,3.0])  
   
print ('First array:') 
print (a) 
print ('\n') 
   
print ('Second array:')
print (b)
print ('\n')  
   
print ('First Array + Second Array')
print (a + b)