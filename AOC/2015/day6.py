import numpy as np, math, itertools, hashlib, time
from functools import reduce, cache
from collections import defaultdict
import re

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

lights = np.zeros((1000,1000))

def turnOn(matches):
    for i in range(matches[0], matches[2] + 1):
        for j in range(matches[1], matches[3] + 1):
            lights[i][j] += 1
        
    
def turnOff(matches):
    for i in range(matches[0], matches[2] + 1):
        for j in range(matches[1], matches[3] + 1):
            if lights[i][j] != 0:
                lights[i][j] -= 1
    
def toggle(matches):
    for i in range(matches[0], matches[2] + 1):
        for j in range(matches[1], matches[3] + 1):
            lights[i][j] += 2
    
            

for line in grid:
    string = ''.join(line);
    matches = re.findall(r'-?\d*\.?\d+', string)

    for i in range(4):
        matches[i] = int(matches[i])
    
    if 'turn on' in string:
        turnOn(matches)
    elif 'turn off' in string:
        turnOff(matches)
    else:
        toggle(matches)

# Count total
for i in range(1000):
    for j in range(1000):
        total += lights[i][j]

result(total)