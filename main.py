import numpy as np
import copy
import math 
import time
from calculate import calculate

# Start timer
starttime = time.time()

# Import data
# In the littles file, each row is a little and each entry is how they rated the big that corresponds to that column
# In the bigs file, each row is a big and each entry is how they rated the little that corresponds to that column
matrix_1 = np.loadtxt('littles.csv', delimiter=',')
matrix_2 = np.loadtxt('bigs.csv', delimiter=',')

shape = (matrix_1.shape[0], matrix_2.shape[0])
list_a = np.zeros(shape)

# Multiply sets together
# Each row of list_a will be a little 
# Each column of list_a will be a big
# for example, list_a[1][3] will be the energy for little 2 and big 4
# i.e., the energy is how well a big and little match
for i in range(shape[0]):
  for j in range(shape[1]):
    list_a[i][j] = (matrix_1[i][j]*matrix_2[j][i])

# Initialize sets
# Set dupes is the most optimal big-little matching if you allow for duplicate bigs
# I.e., You allow for a big to have two littles
# Set noDupes is the most optimal combination if you do not allow duplicate bigs 
# The "optimal combination" is based off of the energy of each big-little pair
dupes = np.zeros(shape[0])
noDupes = np.zeros(shape[0])

dupes.fill(-1)
noDupes.fill(-1)

# Calculate set dupes and noDupes
for i in range(shape[0]):
  calculate(list_a, dupes, i, 2)
  calculate(list_a, noDupes, i, 1)

# Set answer will be the best possible combination
# There may be duplicate bigs, but there may not be
answer = np.zeros(shape[0])

# Compare set dupes and noDupes
# If they agree on a big-little pair, that pair will be in the final set
# If they do not agree, they will be compared on which big-little pair is the most optimal
for i in range(shape[0]):
  if(dupes[i] == noDupes[i]):
    answer[i] = dupes[i]
  else:
    ansCp1 = copy.copy(answer)
    ansCp2 = copy.copy(answer)
    ansCp1[i] = dupes[i]
    ansCp2[i] = noDupes[i]
    sumDupes = 0
    sumNoDupes = 0
    for j in range(shape[0]):
      sumDupes += list_a[j][int(ansCp1[j])]
      sumNoDupes += list_a[j][int(ansCp2[j])]
    bleDupes = sumDupes/len(set(dupes))
    blenoDupes = sumNoDupes/len(set(noDupes))
    if(int(bleDupes) > int(blenoDupes)):
      answer[i] = noDupes[i]
    else:
      answer[i] = dupes[i]

print(answer + 1)

# Calculate sum of energies in final set
sum = 0
for i in range(shape[0]):
  sum += list_a[i][int(answer[i])]

print("Total energy:",sum)
print("Distinct bigs:", len(set(answer)))
print("BLE:", math.sqrt(sum/len(set(answer))))

print("Took", time.time() - starttime, "seconds")