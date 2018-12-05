import numpy as np 
x = np.arange(5) 
print (x)

import numpy as np 
# dtype set 
x = np.arange(5, dtype = float)
print (x)

# start and stop parameters set 
import numpy as np 
x = np.arange(10,20,2) 
print (x)

import numpy as np 
x = np.linspace(10,20,5) 
print (x)

# endpoint set to false 
import numpy as np 
x = np.linspace(10,20, 5, endpoint = False) 
print (x)

# find retstep value 
import numpy as np 

x = np.linspace(1,2,5, retstep = True) 
print (x) 
# retstep here is 0.25

# default base is 10 
a = np.logspace(1.0, 2.0, num = 10) 
print (a)

# set base of log space to 2 
import numpy as np 
a = np.logspace(1,10,num = 10, base = 2) 
print (a)