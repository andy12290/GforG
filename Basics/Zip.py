# zip we used to iterate throghe the tuple
matrix=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
print(matrix)
for row in matrix:
    print(row)

t_matrix = zip(*matrix)
for row in t_matrix:
    print(row)

# if we need data in list
t_mat = list(map(list,zip(*matrix)))
print(t_mat)

# You need to install numpy in order to import it
# Numpy transpose returns similar result when
# applied on 1D matrix
import numpy
matrix=[[1,2,3],[4,5,6]]
print(matrix)
print("\n")
print(numpy.transpose(matrix))
