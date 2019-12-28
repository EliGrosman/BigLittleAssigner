import numpy as np
import csv

matrix_1 = np.loadtxt('littles.csv', delimiter=',')
matrix_2 = np.loadtxt('bigs.csv', delimiter=',')

shape = (matrix_1.shape[0], matrix_2.shape[0])
A = np.zeros(shape)

for i in range(matrix_1.shape[0]):
  for j in range(matrix_2.shape[1]):
    A[j,i] = (matrix_1[j][i]*matrix_2[i][j])

np.savetxt('results (v1).csv', A, fmt="%i", delimiter=",")
print(A)

