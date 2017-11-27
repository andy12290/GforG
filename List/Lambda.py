# filter function and lambda function
# we have to used th list and filter function in python3 version
lst = list(filter(lambda x : x % 2 == 1, range(1, 20)))
print (lst)

# filter function
lst = list(filter(lambda x : x % 5 == 0,
      [x ** 2 for x in range(1, 11) if x % 2 == 1]))
print (lst)

# reduce function
list1 = [1,3,4,56,2,3]
print((reduce(lambda a,b: a if(a>b) else b, list1 )))
