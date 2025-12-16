import numpy as np, math, itertools, hashlib, time
from functools import reduce, cache
from collections import defaultdict, Counter
import queue

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

def euclideanDistance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)

def getNums(nums):
    nums = ''.join(nums).split(',')
    return list(map(int, nums))

pq = queue.PriorityQueue()

for i in range(len(grid)):
    nums1 = getNums(grid[i])
    x1, y1, z1 = nums1
    shortest = float('inf')
    for j in range(len(grid)):
        if i != j:
            nums2 = getNums(grid[j])
            x2, y2, z2 = nums2
            dist = euclideanDistance(x1, y1, z1, x2, y2, z2)
            pq.put((dist, [(x1, y1, z1), (x2, y2, z2)]))

circuits = {}
n = 10
for i in range(n):
    dist, coordSet = pq.get()
    if coordSet[1] in circuits:
        circuits[coordSet[0]] = circuits[coordSet[1]]
    else:
        circuits[coordSet[0]] = len(circuits) + 1
    print(circuits)

values = Counter(circuits.values()).most_common(3)
print(values)
total = values[0][1] * values[1][1] * values[2][1]
result(total)