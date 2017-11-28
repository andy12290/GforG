def checkdivisibility(a,b):
    if a % b == 0 :
        print("A divided by B True")
    else:
        print("Not divided by B")

print(checkdivisibility(4,2))

# transpose to matrix
m = [[1,2],[3,4],[5,6]]
print(m[0]) # matrix
rez = [[ m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print('\n')
for row in rez:
    print(row)

# same we can do in the for loop
for i in range(len(m[0])):
    for j in range(len(m)):
        print(m[j][i])
