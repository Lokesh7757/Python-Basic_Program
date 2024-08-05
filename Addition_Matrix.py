import numpy
import numpy as np

x = [[10,16,12],
    [20,11,18],
    [4,8,2]]

y = [[3,7,9],
     [14,17,18],
     [10,13,15]]

result = [[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range (len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]
for r in result:
    print(r)