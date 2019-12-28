import numpy as np

# Parameter i is the index of a little
# For the given little, it will give it the big so the match has the lowest energy
# If that big already has the maximum amount of littles (maxDupes), then it will compare the given little with each of the big's littles
# If there is better energy with the match of the given little and its top big than with one of the big's littles, the given little will replace the other little
# If the energy is worse with the given little and its top big, it will repeat everything and check for its next top big
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