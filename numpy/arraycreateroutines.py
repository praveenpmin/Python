import numpy as np 
x = np.empty([3,2], dtype = int) 
print (x)

# array of five zeros. Default dtype is float 
import numpy as np 
x = np.zeros(5) 
print (x)

import numpy as np 
x = np.zeros((5,), dtype = np.int) 
print (x)

# custom type 
import numpy as np 
x = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])  
print (x)

# array of five ones. Default dtype is float 
import numpy as np 
x = np.ones(5) 
print (x)

import numpy as np 
x = np.ones([2,2], dtype = int) 
print (x)