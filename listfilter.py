#  filtering odd numbers
lst = filter(lambda x : x % 2 == 1, range(1, 20))
print (lst)
 
#  filtering odd square which are divisble by 5
lst = filter(lambda x : x % 5 == 0, 
      [x ** 2 for x in range(1, 11) if x % 2 == 1])
print (lst)
 
#   filtering negative numbers
lst = filter((lambda x: x < 0), range(-5,5))
print (lst)
 
#  implementing max() function, using
print (reduce(lambda a,b: a if (a > b) else b, [7, 12, 45, 100, 15]))