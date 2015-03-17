matrix = [[1,2,3],[4,5,6],[7,8,9]]
from pprint import pprint
transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]
pprint(transposed)