import numpy as np, math, itertools, hashlib, time
from functools import reduce, cache
from collections import defaultdict

def load_file(file: str) -> list:
    with open(file, 'r') as file:
        file_content = file.read().split('\n')
        if file_content[-1] == '':
            del file_content[-1]
        return file_content
        
def result(total: int = 0):
    duration_ns = time.time_ns()-start
    if duration_ns / 1_000_000_000 < 2:
        print(f'Answer: {total} Time: {round(duration_ns / 1_000_000, 2)}ms')
    else:
        print(f'Answer: {total} Time: {round(duration_ns / 1_000_000_000, 2)}s')
        
start = time.time_ns()

def print_grid(arr):
    for line in arr:
        print(''.join(str(x) for x in line))

def to_grid(grid, arr, integer):
    grid.append([int(x) if integer else x for x in arr])

#######################################################
#####                 Start Here                  #####
#######################################################

array = load_file("AOC/util/input.txt")
total = 0

grid = []
for line in array:
    to_grid(grid, line, False)


def checkValid(id):
    # print(id)

    prev = [id[0]]
    for i, num in enumerate(id):
        # print(prev)
        if i != 0:
          l = len(id) // i
          if prev[-1]*l == id:
              # print(id)
              return int(id)
        
          prev.append(prev[-1] + num)

    return 0


# first, last = res[i].split('-')
res = []
for line in grid:
  last = -1
  for i, c in enumerate(line):
      if c == ',':
          res.append(line[last+1:i])
          last = i
  
  res.append(grid[0][last+1:len(grid[0])])
  
  for i in range(len(res)):
      s = ''.join(res[i])
      first, last = s.split('-')
      first = int(first)
      last = int(last)
      
      for id in range(first, last + 1):
          total += checkValid(str(id))
          



result(total)