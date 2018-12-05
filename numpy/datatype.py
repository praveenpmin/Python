# using array-scalar type 
import numpy as np 
dt = np.dtype(np.int32) 
print (dt)

#int8, int16, int32, int64 can be replaced by equivalent string 'i1', 'i2','i4', etc. 
import numpy as np 

dt = np.dtype('i4')
print (dt)

# using endian notation 
import numpy as np 
dt = np.dtype('>i4') 
print (dt)

# first create structured data type 
import numpy as np 
dt = np.dtype([('age',np.int8)]) 
print (dt)

# now apply it to ndarray object 
import numpy as np 

dt = np.dtype([('age',np.int8)]) 
a = np.array([(10,),(20,),(30,)], dtype = dt) 
print (a)

# file name can be used to access content of age column 
import numpy as np 

dt = np.dtype([('age',np.int8)]) 
a = np.array([(10,),(20,),(30,)], dtype = dt) 
print (a['age'])

student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
print (student)

student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
print (a)