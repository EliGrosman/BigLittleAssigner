import numpy as np

def calculate(list_a, array, i, maxDupes):
  for b in range(len(list_a[i])):
    if list_a[i][b] != 0:
      if (array == b).sum() == maxDupes:
        otherLs = np.where(array == b)[0]
        for l in otherLs:
          if(list_a[l][b] > list_a[i][b]): 
            array[i] = b
            array[l] = 0
            calculate(list_a, array, l, maxDupes)
      else: 
        array[i] = b
        break