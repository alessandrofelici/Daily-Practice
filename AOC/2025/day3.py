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

def getVoltage(nums):
    l, r = 0, len(nums) - 1
    first, second = nums[l], nums[r]

    for i, num in enumerate(nums):
        if num > first and i != r:
            l = i
            first = num

    while l < r:
        second = max(second, nums[r])
        r -= 1
    
    combined = first + second
    return int(combined)

def part2(nums):
    windowSize = 89
    i = 0
    while windowSize > 1:
        hi = i
        for j in range(i, i + windowSize):
            if j == len(nums):
                if hi == i:
                    print(len(nums[:12]))
                    return int(''.join(nums[:12]))
                break
            if nums[j] > nums[hi]:
                hi = j
        while hi != i and windowSize > 1:
            nums.pop(i)
            windowSize -= 1
            hi -= 1
        
        i += 1
    
    return int(''.join(nums))

for line in grid:
    total += part2(line)
    # print(total)

result(total)

170147128753455
170147128753455