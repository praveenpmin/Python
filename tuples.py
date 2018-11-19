# Creating non-empty tuples
# One way of creation
tup='Python','Techy'
print(tup)

# Another for doing the same
tup= ('Python','Techy')
print(tup)

# Code for concatenating to tuples
tuple1=(0,1,2,3)
tuple2=('Python','Techy')
# Concatenating two tuples
print(tuple1+tuple2)

# code fore creating nested loops
tuple3=(tup,tuple1,tuple2)
print(tuple3)

# code to create a tuple with repitition

tuple3=('python',)*3
print(tuple3)

# code to test slicing
tuple1=(0,1,2,3)
print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4])

# Code for printing length of the tuple
print(len(tuple3))

# Code to convert list to tuple
list1 = [0,1,2]
print(tuple(list1))
print(tuple('Python'))

# Code for creating tuples in a loop
tup=('Techy')
n=5
for i in range(int(n)):
  tup=(tup,)
  print(tup)

# Code to demonstrate max(), cmp(), min()
def cmp(a, b):
    return (a > b) - (a < b)
 
list1, list2 = [123, 'xyz'], [456, 'abc']
print(cmp(list1, list2))
print(cmp(list2, list1))
list3 = list2 + [786];
print(cmp(list2, list3))
tuple5=('Python' , 'Techy')
tuple6=('Coder',1)
## if ( cmp(tuple1,tuple2) !=0):
  # print('not the same')
# else:
  ## print('same') 
# print('Maximum elements in tuples 1,2:'+ str(max(tuple5))+',' + str(max(tuple6)))
# print('Minimum elements in tuples 1,2:'+ str(min(tuple5))+',' + str(min(tuple6)))

# Delete a tuple
tuple4=(0,1)
del tuple4
print(tuple4)