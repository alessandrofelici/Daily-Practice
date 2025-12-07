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

nums = []

# part 1
# for i, line in enumerate(array):
#     input = line.split(' ')
#     if i == len(array) - 1:
#         input = list(filter(lambda s: s, input))
#     else:
#         input = list(map(lambda s: int(s), filter(lambda s: s, input)))
#     nums.append(input)

# part 2
ops = list(filter(lambda s: s != ' ', list(array[len(array) - 1])))

grid = []
for i in range(len(array) - 1):
    to_grid(grid, array[i], False)

nums = []
operatorIndex = len(ops) - 1
for j in range(len(grid[0]) - 1, -1, -1):
    num = ''
    for i in range(len(grid)):
        if grid[i][j] != ' ':
            num += grid[i][j]
    if num:
        nums.append(num)
    else:
        op = ops[operatorIndex]
        subtotal = 1 if op == '*' else 0
        for x in nums:
            if op == '+':
                subtotal += int(x)
            else:
                subtotal *= int(x)
        operatorIndex -= 1
        nums = []
        total += subtotal
        
op = ops[operatorIndex]
subtotal = 1 if op == '*' else 0
for x in nums:
    if op == '+':
        subtotal += int(x)
    else:
        subtotal *= int(x)
total += subtotal

# operatorIndex = len(nums) - 1
# for j in range(len(nums[0])):
#     op = nums[operatorIndex][j]
#     rowTotal = 0 if op == '+' else 1
#     for i in range(len(nums) - 1):
#         if op == '*':
#             rowTotal *= nums[i][j]
#         else:
#             rowTotal += nums[i][j]
#     total += rowTotal

result(total)