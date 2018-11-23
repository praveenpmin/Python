# Python code to demonstrate the working of array
import array

# Initializing array with array values
arr=array.array('i',[1,2,3])

# Printing original array
print("The new created array is:",end="")
for i in range(0,3):
    print(arr[i],end="")

print("\r")

# using append to insert value to end
arr.append(4)

# printing appended array
print("The appended array is:",end="")
for i in range(0,4):
    print(arr[i],end="")

# using insert to value at specific location
arr.insert(2,5)
print("\r")

# printing array after insertion
print("The after insertion is:",end="")
for i in range(0,5):
    print(arr[i],end="")
print("\r")

# using pop to remove value
print("The popped element is:",end="")
print(arr.pop(2))

#printing array after popping
print("The array after popping is:",end="")
for i in range(0,4):
    print(arr[i],end="")
print("\r")

# using remove() to remove 1st occurance value
print("The removed element is:",end="")
arr.remove(1)

# printing array after removing
for i in range(0,3):
    print(arr[i],end="")
print("\r")
# For index()
# Initializing array with array values
arr=array.array('i',[1,2,3,0,2,5])

# Using index() to print index of 1st occurence of 2
print("The index of 1st occurence of 2 is:",end="")
print(arr.index(2))

# Using reverse to reverse the array
arr.reverse()

# Printing array after reversing
print("The array after reversing is:",end="")
for i in range(0,6):
    print(arr[i],end="")

# Using typecode to print datatype of an array
print("The datatype of array is:",end="")
print(arr.typecode)

# using itemsize to print the itemsize of array
print("The itemsize of array is:",end="")
print(arr.itemsize)

# Using buffer_info to print the buffer info of array
print("The buffer info of an array is:",end="")
print(arr.buffer_info())

# Initializing array2 with values
arr2=array.array('i',[7,8,9])

# Using count() to count occurences of 1 in array
print("The occurences of 2 in array is:",end="")
print(arr.count(2))

# Using extended() to add arr2 elements to arr1
arr.extend(arr2)

print("The modified array is:",end="")
for i in range(0,9):
    print(arr[i],end="")
print("\r")

# Python code to demonstrate the working of 
# fromlist() and tolist()
  
 
# initializing list
li = [1, 2, 3]
 
# using fromlist() to append list at end of array
arr.fromlist(li)
 
# printing the modified array
print ("The modified array is : ",end="")
for i in range (0,9):
    print (arr[i],end=" ")
 
# using tolist() to convert array into list
li2 = arr.tolist()
 
print ("\r")
 
# printing the new list
print ("The new list created is : ",end="")
for i in range (0,len(li2)):
    print (li2[i],end=" ")