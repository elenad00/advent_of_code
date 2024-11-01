## aoc 2023 - day 11 ##
##     by elena d    ##

## imports
import sys
import os
from math import sqrt
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from aoc_utils import *

## part one ##
def part_one():
    x_empties = []
    i = 1
    # add rows
    y_empties = [l for l in range(len(input)) if input[l].count('.') == len(input[l])]
    # add columns
    i = 0
    while i < len(input):
        line = [input[v][i] for v in range(len(input))]
        if '#' not in line:
            x_empties.append(i)
            i+=1
        i+=1

    # print input
    points = []
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x]=='#': points.append([y,x])    
    
    s = 0
    for i in range(len(points)):
        cy,cx = points[i]
        for y,x in points[i+1:]:
            y_r = range(y,cy) if y<cy else range(cy,y)
            x_r = range(x,cx) if x<cx else range(cx,x)
            add_y = len([v for v in y_empties if v in y_r])
            add_x = len([v for v in x_empties if v in x_r])
            add=(add_y+add_x)*100
            s+=abs(y-cy)+abs(x-cx)+add
    print(s)
    print(s-len(points)**2)
    return

## part two ##
def part_two():
    return

test_input = []
input = read_file('test.txt')
part_one() # 9543156
           # 9543074
part_two() # 625243917839 (too high)
           # 625243729565 (too high)