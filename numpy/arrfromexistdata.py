# convert list to ndarray 
import numpy as np 

x = [1,2,3] 
a = np.asarray(x) 
print (a)

# dtype is set 
import numpy as np 

x = [1,2,3]
a = np.asarray(x, dtype = float) 
print (a)

# ndarray from tuple 
import numpy as np 

x = (1,2,3) 
a = np.asarray(x) 
print (a)

# ndarray from list of tuples 
import numpy as np 

x = [(1,2,3),(4,5)] 
a = np.asarray(x) 
print (a)

# create list object using range function 
import numpy as np 
list = range(5) 
print (list)

# obtain iterator object from list 
import numpy as np 
list = range(5) 
it = iter(list)  

# use iterator to create ndarray 
x = np.fromiter(it, dtype = float) 
print (x)


import numpy as np 
s = 'Hello World' 
a = np.frombuffer(s, dtype = 'S1') 
print (a)