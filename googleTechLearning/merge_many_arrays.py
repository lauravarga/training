import sys
import heapq

def pick_min_and_advance(array1, array2, pos1, pos2):
  if pos1 < len(array1) and pos2 < len(array2):
    if array1[pos1] <= array2[pos2]:
      result = array1[pos1]
      pos1 += 1
    else:
      result = array2[pos2]
      pos2 += 1
  elif pos1 >= len(array1):
    result = array2[pos2]
    pos2 += 1
  else:
    result = array1[pos1]
    pos1 += 1
  return result, pos1, pos2

def merge(array1, array2):
  pos1 = pos2 = 0
  result = []
  while pos1 < len(array1) or pos2 < len(array2):
    next_value, pos1, pos2 = pick_min_and_advance(array1, array2, pos1, pos2)
    result.append(next_value)

  return result

def multiple_merge(arrays, n):
    i = n
    while i > 0:
        arrays[0] = merge(arrays[0], arrays[i])
        i -= 1
    return arrays[0]

def heap_merge(arrays):
    result = []
    for array in arrays:
        for el in array:
            heapq.heappush(result, el)
    return result

file = open("in.txt")
n = int(file.readline())
lengths = [int(el) for el in file.readline().split()]
arrays = [[int(el) for el in file.readline().split()]
          for length in lengths]
merged_heap = heap_merge(arrays)
while len(merged_heap) > 0:
    sys.stdout.write(str(heapq.heappop(merged_heap)) + ' ')

