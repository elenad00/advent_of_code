""" 
--- Day 11: Cosmic Expansion ---

The researcher has collected a bunch of data and compiled the data into a single giant image (your puzzle input). The image includes empty space (.) and galaxies (#). For example:
  ...#......
  .......#..
  #.........
  ..........
  ......#...
  .#........
  .........#
  ..........
  .......#..
  #...#.....
The researcher is trying to figure out the sum of the lengths of the shortest path between every pair of galaxies. However, there's a catch: the universe expanded in the time it took the light from those galaxies to reach the observatory.

Due to something involving gravitational effects, only some space expands. In fact, the result is that any rows or columns that contain no galaxies should all actually be twice as big.

In the above example, three columns and two rows contain no galaxies. These rows and columns need to be twice as big; the result of cosmic expansion therefore looks like this:

  ....#........
  .........#...
  #............
  .............
  .............
  ........#....
  .#...........
  ............#
  .............
  .............
  .........#...
  #....#.......

Equipped with this expanded universe, the shortest path between every pair of galaxies can be found. It can help to assign every galaxy a unique number:
  ....1........
  .........2...
  3............
  .............
  .............
  ........4....
  .5...........
  ............6
  .............
  .............
  .........7...
  8....9.......
In these 9 galaxies, there are 36 pairs. Only count each pair once; order within the pair doesn't matter. For each pair, find any shortest path between the two galaxies using only steps that move up, down, left, or right exactly one . or # at a time. (The shortest path between two galaxies is allowed to pass through another galaxy.)

For example, here is one of the shortest paths between galaxies 5 and 9:
  ....1........
  .........2...
  3............
  .............
  .............
  ........4....
  .5...........
  .##.........6
  ..##.........
  ...##........
  ....##...7...
  8....9.......
This path has length 9 because it takes a minimum of nine steps to get from galaxy 5 to galaxy 9 (the eight locations marked # plus the step onto galaxy 9 itself). Here are some other example shortest path lengths:

Between galaxy 1 and galaxy 7: 15
Between galaxy 3 and galaxy 6: 17
Between galaxy 8 and galaxy 9: 5

In this example, after expanding the universe, the sum of the shortest path between all 36 pairs of galaxies is 374.

Expand the universe, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?

--- Part Two ---

Now, instead of the expansion you did before, make each empty row or column one million times larger. 

Each empty row should be replaced with 1000000 empty rows, and each empty column should be replaced with 1000000 empty columns.

In the example above, if each empty row or column were merely 10 times larger, the sum of the shortest paths between every pair of galaxies would be 1030. 
If each empty row or column were merely 100 times larger, the sum of the shortest paths between every pair of galaxies would be 8410. However, your universe will need to expand far beyond these values.

Starting with the same initial image, expand the universe according to these new rules, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?
"""
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