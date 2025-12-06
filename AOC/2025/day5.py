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
part1 = part2 = 0

grid = []
for line in array:
    to_grid(grid, line, False)

for i, line in enumerate(grid):
    if not line:
        ranges = grid[:i]
        ids = grid[i+1:]

# Part 2
valid = []

for i in range(len(ranges)):
    ranges[i] = list(map(int, ''.join(ranges[i]).split('-')))

ranges.sort(key=lambda x: x[0])
        
current_lo, current_hi = ranges[0]
for new_lo, new_hi in ranges[1:]:
    if new_lo <= current_hi + 1:
        current_hi = max(current_hi, new_hi)
    else:
        valid.append([current_lo, current_hi])
        current_lo, current_hi = new_lo, new_hi
valid.append([current_lo, current_hi])
            
for pair in valid:
    if not pair:
        continue
    part2 += pair[1] - pair[0] + 1

# Part 1
# for i in range(len(ids)):
#     ids[i] = int(''.join(ids[i]))

# def validate(id, range_):
#     range_ = ''.join(range_)
#     lo, hi = range_.split('-')
#     lo, hi = int(lo), int(hi)
#     return id >= lo and id <= hi

# for range_ in ranges:
#     for i, id in enumerate(ids):
#       if ids[i] and validate(id, range_):
#           part1 += 1
#           ids[i] = None

result(part2)