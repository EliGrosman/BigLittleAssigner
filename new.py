import numpy as np
import copy
import math 

matrix_1 = np.loadtxt('littles.csv', delimiter=',')
matrix_2 = np.loadtxt('bigs.csv', delimiter=',')

shape = (matrix_1.shape[0], matrix_2.shape[0])
list_a = np.zeros(shape)

for i in range(shape[0]):
  for j in range(shape[1]):
    list_a[j,i] = (matrix_1[j][i]*matrix_2[i][j])

def cartesianProduct(a, b): 
    result =[] 
    for i in range(len(a)): 
        for j in range(len(b)): 
            if type(a[i]) != list:          
              temp = [i+1]
            else:
              temp = copy.copy(a[i])
            temp.append(j+1)  
            doAdd = True   
            for n in range(len(temp)):
              if list_a[n][temp[n]-1] == 0:
                doAdd = False
            if(doAdd):
              result.append(temp)   
    return result 


def PermutateAllSets(list_a, n): 
    temp = list_a[0] 
    for i in range(1, n): 
        temp = cartesianProduct(temp, list_a[i]) 
    result = []
    for i in range(len(temp)):
      sum = 0
      for j in range(len(temp[i])):
        sum += list_a[j][temp[i][j]-1]
      result.append((temp[i], sum, len(set(temp[i])), math.sqrt(sum/len(set(temp[i])))))
    return(result) 
   
p = PermutateAllSets(list_a, len(list_a))

energy = []
for i in p:
  energy.append((i[3],i))

energy.sort()
print(energy[0:5])

with open('resultsnew.txt', 'w') as fp:
    fp.write('\n'.join('%s %s' % x for x in energy))