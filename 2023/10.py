""" --- Day 10: Pipe Maze ---

Scanning the area, you discover that the entire field you're standing on is densely packed with pipes; it was hard to tell at first because they're the same metallic silver color as the "ground". You make a quick sketch of all of the surface pipes you can see (your puzzle input).

The pipes are arranged in a two-dimensional grid of tiles:
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
Based on the acoustics of the animal's scurrying, you're confident the pipe that contains the animal is one large, continuous loop.

For example, here is a square loop of pipe:
    .....
    .S-7.
    .|.|.
    .L-J.
    .....
In the above diagram, the S tile is still a 90-degree F bend: you can tell because of how the adjacent pipes connect to it.

Unfortunately, there are also many pipes that aren't connected to the loop! This sketch shows the same loop as above:
    -L|F7
    7S-7|
    L|7||
    -L-J|
    L|-JF
In the above diagram, you can still figure out which pipes form the main loop: they're the ones connected to S, pipes those pipes connect to, pipes those pipes connect to, and so on. 
Every pipe in the main loop connects to its two neighbors (including S, which will have exactly two pipes connecting to it, and which is assumed to connect back to those two pipes).

Here is a sketch that contains a slightly more complex main loop:
    ..F7.
    .FJ|.
    SJ.L7
    |F--J
    LJ...
Here's the same example sketch with the extra, non-main-loop pipe tiles also shown:
    7-F7-
    .FJ|7
    SJLL7
    |F--J
    LJ.LJ
If you want to get out ahead of the animal, you should find the tile in the loop that is farthest from the starting position. Because the animal is in the pipe, it doesn't make sense to measure this by direct distance. Instead, you need to find the tile that would take the longest number of steps along the loop to reach from the starting point - regardless of which way around the loop the animal went.

In the first example with the square loop:
    .....
    .S-7.
    .|.|.
    .L-J.
    .....
You can count the distance each tile in the loop is from the starting point like this:
    .....
    .012.
    .1.3.
    .234.
    .....
In this example, the farthest point from the start is 4 steps away.

Here's the more complex loop again:
    ..F7.
    .FJ|.
    SJ.L7
    |F--J
    LJ...
Here are the distances for each tile on that loop:
    ..45.
    .236.
    01.78
    14567
    23...
Find the single giant loop starting at S. How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?

--- Part Two ---

You quickly reach the farthest point of the loop, but the animal never emerges. 
Maybe its nest is within the area enclosed by the loop?

To determine whether it's even worth taking the time to search for such a nest, 
you should calculate how many tiles are contained within the loop. For example:
    ...........
    .S-------7.
    .|F-----7|.
    .||.....||.
    .||.....||.
    .|L-7.F-J|.
    .|..|.|..|.
    .L--J.L--J.
    ...........
The above loop encloses merely four tiles - the two pairs of . in the southwest 
and southeast (marked I below). The middle . tiles (marked O below) are not in the loop. 
Here is the same loop again with those regions marked:
    ...........
    .S-------7.
    .|F-----7|.
    .||OOOOO||.
    .||OOOOO||.
    .|L-7OF-J|.
    .|II|O|II|.
    .L--JOL--J.
    .....O.....
In fact, there doesn't even need to be a full tile path to the outside for tiles to 
count as outside the loop - squeezing between pipes is also allowed! 
Here, I is still within the loop and O is still outside the loop:
    ..........
    .S------7.
    .|F----7|.
    .||OOOO||.
    .||OOOO||.
    .|L-7F-J|.
    .|II||II|.
    .L--JL--J.
    ..........
In both of the above examples, 4 tiles are enclosed by the loop.

Here's a larger example:
    .F----7F7F7F7F-7....
    .|F--7||||||||FJ....
    .||.FJ||||||||L7....
    FJL7L7LJLJ||LJ.L-7..
    L--J.L7...LJS7F-7L7.
    ....F-J..F7FJ|L7L7L7
    ....L7.F7||L7|.L7L7|
    .....|FJLJ|FJ|F7|.LJ
    ....FJL-7.||.||||...
    ....L---J.LJ.LJLJ...
The above sketch has many random bits of ground, some of which are in the loop (I) and some of which are outside it (O):
    OF----7F7F7F7F-7OOOO
    O|F--7||||||||FJOOOO
    O||OFJ||||||||L7OOOO
    FJL7L7LJLJ||LJIL-7OO
    L--JOL7IIILJS7F-7L7O
    OOOOF-JIIF7FJ|L7L7L7
    OOOOL7IF7||L7|IL7L7|
    OOOOO|FJLJ|FJ|F7|OLJ
    OOOOFJL-7O||O||||OOO
    OOOOL---JOLJOLJLJOOO
In this larger example, 8 tiles are enclosed by the loop.

Any tile that isn't part of the main loop can count as being enclosed by the loop. Here's another example with many bits of junk pipe lying around that aren't connected to the main loop at all:
    FF7FSF7F7F7F7F7F---7
    L|LJ||||||||||||F--J
    FL-7LJLJ||||||LJL-77
    F--JF--7||LJLJ7F7FJ-
    L---JF-JLJ.||-FJLJJ7
    |F|F-JF---7F7-L7L|7|
    |FFJF7L7F-JF7|JL---7
    7-L-JL7||F7|L7F-7F7|
    L.L7LFJ|||||FJL7||LJ
    L7JLJL-JLJLJL--JLJ.L
Here are just the tiles that are enclosed by the loop marked with I:
    FF7FSF7F7F7F7F7F---7
    L|LJ||||||||||||F--J
    FL-7LJLJ||||||LJL-77
    F--JF--7||LJLJIF7FJ-
    L---JF-JLJIIIIFJLJJ7
    |F|F-JF---7IIIL7L|7|
    |FFJF7L7F-JF7IIL---7
    7-L-JL7||F7|L7F-7F7|
    L.L7LFJ|||||FJL7||LJ
    L7JLJL-JLJLJL--JLJ.L
In this last example, 10 tiles are enclosed by the loop.

Figure out whether you have time to search for the nest by calculating the area within the loop. 
How many tiles are enclosed by the loop?

"""

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