# String are immutable in python
A = "Aniket Kale"
print(A)

# List are array and mutable and we can add different data types
list1 = ['A', 123, "10"]
print(list1)

# looping in list1
for row in list1:
    print("Looping",row)

# tuple
# we cannot change the tuple.
# tuples are faster than the list
tup = (1, "a", "string", 1+2)
for row in tup:
    print('tup', row)
