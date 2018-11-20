# Program to demonstrate working set

# Creating two sets
set1=set()
set2=set()

# Adding elements to set1
for i in range(1,6):
    set1.add(i)

# Adding elements to set2
for i in range(3,8):
    set2.add(i)

print("Set1=",set1)
print("Set2=",set2)
print("\n")

# Union of set1 and set2
set3=set1 | set2

print("union of set1 and set2 = ",set3)
print("\n")

# Intersection of set1 and set2
set4=set1 & set2

print("Intersection of set1 and set2 = ",set4)

# Checking relation between set3 and set4
if set3>set4:
    print("set3 is superset of set4")
    print("\n")
elif set3<set4:
    print("set3 is subset of set4")
    print("\n")
else:
    print("set3 is same as set4")
    print("\n")

# Displaying relation between set3 and set4
if set4<set3:
    print("set4 is subset of set3")
print("\n")

# Difference between set3 and set4
set5=set3-set4
print("Elements in set3 not in set4",set5)
print("\n")

# Check if set5 and set4 are disjoint
if set4.isdisjoint(set5):
    print("set4 and set5 have nothing in common")
print("\n")

# Removing all the value of set5
set5.clear()
print("After applying clear onm set5:")
print("set5=",set5)

