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

vals = {}

def getVariable(line):
    return line[len(line) - 2]

def sepVars(line):
    vars = []
    curr = ''
    for c in line:
        if c == ' ':
            vars.append(curr)
            curr = ''
            continue
        elif c == '-':
            break
        curr += c
    while (len(vars) < 3):
        vars.append('')

    return vars

def computeVal(line):
    # take phrase before arrow
    first, op, last = sepVars(line)

    # turn to string
    s = ''.join(line)
    assignTo = getVariable(s)

    # no operator exists
    if op == '':
        if first[0].isdigit():
          vals[assignTo] = int(first)
        elif first in vals:
          vals[assignTo] = int(vals[first])
        return
    
    # operator exists: one var
    if last == '':
        # not assigned yet
        if op not in vals:
            return
        # note first is op and op is the variable
        vals[assignTo] = ~bin(vals[op])
        return
    
    if last not in vals:
        # not assigned yet
        return
    
    # operator exists: two var
    first = bin(vals[first])
    last = bin(vals[last])
    if 'AND' == op:
        vals[assignTo] = first & last
    elif 'OR' == op:
        vals[assignTo] = first | last
    elif 'LSHIFT' == op:
        vals[assignTo] = first << last
    elif 'RSHIFT' == op:
        vals[assignTo] = first >> last
    elif 'NOT' == op:
        vals[assignTo] = ~last

for line in grid:
    computeVal(line)
           

print(vals)

result(total)