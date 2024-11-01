## aoc 2023 - day 10 ##
##     by elena d    ##

## imports
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from aoc_utils import *

def is_visited(visited):
    coord_range = []
    min_point = min(visited)
    max_point = max(visited)
    if min_point[0]==max_point[0]:
        first = min_point[1]
        last = max_point[1]
        for r in range(last-first):
            coord_range.append([min_point[0],first+r])
    else:
        first = min_point[0]
        last = max_point[0]
        for r in range(last-first):
            coord_range.append([first+r,min_point[1]])
    return (coord_range)

## part one ##
def part_one():
    for line in input: 
        if 'S' in line: y,x = [input.index(line), input[input.index(line)].index('S')]
    visited = [[y,x]]
    pipe_type = 'F'
    while pipe_type!='S':
        one,two = routes[pipe_type]
        if [y+one[0], x+one[1]] not in visited: next=one
        else: next=two
        y+=next[0]
        x+=next[1]
        pipe_type = input[y][x]
        visited.append([y,x])
    print((len(visited)-1)/2)
    return visited

## part two ##
def part_two(visited):
    grid = []
    for g in range(140): grid.append([0 for x in range(140)])
    for y,x in visited: grid[y][x]=1
    visited.sort()
    x_range = []
    y_range = []
    for i in range(140):
        visited_y = [v for v in visited if v[0]==i]
        if visited_y!=[]:y_range.append(is_visited(visited_y))
        visited_x=[v for v in visited if v[1]==i] 
        if visited_x!=[]: x_range.append(is_visited(visited_x))
    x_range = [j for sub in x_range for j in sub]
    y_range = [j for sub in y_range for j in sub]
    match_list=[v for v in x_range if v in y_range]
    ones = [(y,x) for (y,x) in match_list if grid[y][x]==0]
    print(len(ones))
    return

raw_input = read_file('input.txt')
# raw_input = read_file('test.txt')

input = [list(x) for x in raw_input]

p = [[1,0],[-1,0],[0,1],[0,-1]]
routes = {
    '-':(p[2],p[3]),
    'F':[p[0],p[2]],
    '7':[p[0],p[3]],
    'L':[p[1],p[2]],
    'J':[p[1],p[3]],
    '|':(p[0],p[1]),
}

visited = part_one() # 6842
part_two(visited) # 393