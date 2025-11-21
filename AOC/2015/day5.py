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

for line in grid:
    pair = ''.join(line[:2])
    found = False
    for i, char in enumerate(line):
        if i > 1:
            if pair in ''.join(line[i:]):
                found = True
                break
            pair = pair[1] + char
        
    prev = None
    dupe = False
    for i, char in enumerate(line):
        prev = line[i-2] if i-2 >= 0 else None
        if prev == char:
            dupe = True
            break
    
    if dupe and found:
        total += 1
        
        


# bad_str = ["ab", "cd", "pq", "xy"]
# vowels = {
#     "a": True,
#     "e": True,
#     "i": True,
#     "o": True,
#     "u": True,
# }

# for line in grid:
#     vowelsCount = 0
#     prev = None
#     dupe = False
#     bad = False

#     for pair in bad_str:
#         bad = True if bad else pair in ''.join(line)
    
#     if bad:
#         continue
    
#     for char in line:
#         if char in vowels:
#             vowelsCount += 1
#         if prev and prev == char:
#             dupe = True
#         prev = char
    
#     if vowelsCount >= 3 and dupe:
#         total += 1
    

result(total)