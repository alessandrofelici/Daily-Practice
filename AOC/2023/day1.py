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
def find_num(line):
    word_to_num = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    def wordInLine(string):
        string = ''.join(string)
        for word in word_to_num:
            # print(word, string)
            if word in string:
                return word
        return False

    l, r = 0, len(line) - 1
    inc_l = inc_r = 1
    first = last = -1
    
    while first == -1 or last == -1:
        # print(l, r)
        if line[l].isdigit():
            first = int(line[l])
            # print(first)
            inc_l = 0
        elif wordInLine(line[:l+1]): 
            first = word_to_num[wordInLine(line[:l+1])]
            # print(first)
            inc_l = 0
        if line[r].isdigit():
            last = int(line[r])
            # print(last)
            inc_r = 0
        elif wordInLine(line[r:]): 
            last = word_to_num[wordInLine(line[r:])]
            # print(last)
            inc_r = 0
        l += inc_l
        r -= inc_r
            
    sum = first*10 + last
    # print(first, last, sum)

    return sum
        

array = load_file("D:/GitHub/Daily-Practice/AOC/input.txt")
total = 0

grid = []
for line in array:
    to_grid(grid, line, False)

for line in grid:
    print(''.join(line))
    total += find_num(line)
# print_grid(grid)

result(total)

