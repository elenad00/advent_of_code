## aoc 2023 - day 11 ##
##     by elena d    ##

## imports
import sys
import os
from math import sqrt
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from aoc_utils import *

def y_empties():
    return [l for l in range(len(input)) if input[l].count('.') == len(input[l])]

def x_empties():
    x = []
    i = 0
    while i < len(input):
        line = [input[v][i] for v in range(len(input))]
        if '#' not in line:
            x.append(i)
            i+=1
        i+=1
    return x

def check_blanks(c,cc,coords):
    r = range(c,cc) if c<cc else range(cc,c)
    return len([v for v in coords if v in r])


## part one ##
def part_one():
    y_coords = y_empties()
    x_coords = x_empties()
    points = []
    s = 0
    
    for y in range(len(input)):
        for x in range(len(input[y])): 
            if input[y][x]=='#': points.append([y,x])    
    for i in range(len(points)):
        cy,cx = points[i]
        for y,x in points[i:]:
            add_y = check_blanks(y,cy,y_coords)
            add_x = check_blanks(x,cx,x_coords)
            add=(add_y+add_x)
            s+=abs(y-cy)+abs(x-cx)+add
    return s

## part two ##
def part_two():
    return

test_input = []
input = read_file('test.txt')

print(part_one())
# 9543156
# 9543074
print(part_two())
# 625243917839 (too high)
# 625243729565 (too high)