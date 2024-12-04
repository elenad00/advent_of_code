""" 
--- Day 4: Ceres Search ---

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. 
  
In this word search, XMAS occurs a total of 18 times.
    ....XXMAS.
    .SAMXMS...
    ...S..A...
    ..A.A.MS.X
    XMASAMX.MM
    X.....XA.A
    S.S.S.S.SS
    .A.A.A.A.A
    ..M.M.M.MM
    .X.X.XMASX
Take a look at the Elf's word search. 
How many times does XMAS appear?

--- Part Two ---
You're supposed to find two MAS in the shape of an X. One way to achieve that is like this:
    M.S
    .A.
    M.S
Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:
    .M.S......
    ..A..MSMS.
    .M.S.MAA..
    ..A.ASMSM.
    .M.S.M....
    ..........
    S.S.S.S.S.
    .A.A.A.A..
    M.M.M.M.M.
    ..........
In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?
"""

import sys
import os

position_index = {
    0:'n',
    1:'ne',
    2:'e',
    3:'se',
    4:'s',
    5:'sw',
    6:'w',
    7:'nw'
}

parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
import grid_navigator

def check_for_xmas() -> int:
    xmas_count = 0
    directions = []
    x = wordsearch.x
    y = wordsearch.y
    
    around = wordsearch.check_around()
    for v in range(len(around)):
        if around[v]=='M': directions.append(position_index[v])
    for dir in directions:
        wordsearch.x = x
        wordsearch.y = y
        ret, c = wordsearch.traverse_grid(dir, 4)
        if ret == 'XMAS':
            print(f"added {ret} at {x},{y} with dir {dir}")
            xmas_count+=1
    return xmas_count

def check_for_mas() -> int:
    mas_count = 0
    directions = []
    x = wordsearch.x
    y = wordsearch.y
    all_mas_coords = []
    around = wordsearch.check_around()
    for v in range(len(around)):
        if around[v]=='A': 
            directions.append(position_index[v])
    for dir in directions:
        if dir not in ['n', 'e', 's', 'w']:
            wordsearch.x = x
            wordsearch.y = y
            ret, coords = wordsearch.traverse_grid(dir, 3)
            if ret == 'MAS':
                print(f"added {ret} at {x},{y} with dir {dir}")
                all_mas_coords.append(coords)
                mas_count+=1
    return mas_count, all_mas_coords

def part_one():
    for line in wordsearch.grid: print(line)
    xmas_count = 0
    for x in range(wordsearch.height):
        for y in range(wordsearch.width):
            if wordsearch.grid[x][y] == 'X':
                wordsearch.x = x
                wordsearch.y = y
                xmas_count+=check_for_xmas()
    print(xmas_count)
    return

def part_two():
    for line in wordsearch.grid: print(line)
    mas_count = 0
    all_mas_coords = []
    for x in range(wordsearch.height):
        for y in range(wordsearch.width):
            if wordsearch.grid[x][y] == 'M':
                wordsearch.x = x
                wordsearch.y = y
                mc, mas_coords=check_for_mas()
                mas_count+=mc
                if mas_coords!=[]:
                    all_mas_coords+=mas_coords
    print(all_mas_coords)
    print(mas_count)
    return

wordsearch = grid_navigator.Grid_Navigator("test_data/d4.txt")
part_one() # 2642
part_two()