""" 
--- Day 3: Gear Ratios ---

if you can add up all the part numbers in the engine schematic,
it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual
representation of the engine. 

Any number adjacent to a symbol, even diagonally, is a 
"part number" and should be included in your sum.
(Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114.. 0
...*...... 1
..35..633. 2
......#... 3
617*...... 4
.....+.58. 5
..592..... 6
......755. 7
...$.*.... 8
.664.598.. 9
0123456789

In this schematic, two numbers are not part numbers because they
are not adjacent to a symbol: 114 (top right) and 58 (middle
right). Every other number is adjacent to a symbol and so is a
part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is
the sum of all of the part numbers in the engine schematic?

--- Part Two ---

The missing part wasn't the only issue - one of the gears in the 
    engine is wrong. A gear is any * symbol that is adjacent to 
    exactly two part numbers. Its gear ratio is the result of 
    multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add 
    them all up so that the engineer can figure out which gear 
    needs to be replaced.

Consider the same engine schematic again:
    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..
In this schematic, there are two gears. The first is in the top 
    left; it has part numbers 467 and 35, so its gear ratio is 
    16345. The second gear is in the lower right; its gear ratio 
    is 451490. (The * adjacent to 617 is not a gear because it 
    is only adjacent to one part number.)
Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your
    engine schematic?

"""
## imports
from aoc_utils import *
#  012
#0123456

def check_str(pos,d):
    n=1
    if len(pos)==1 or pos=='...':
        if pos=='.' or pos=='...':
            return n
        else:return int(d.strip('.'))
    if pos[0] in INTS and pos[2] in INTS:
        if pos[1] == '.':
            first = int(d[0:3].strip('.'))
            second = int(d[4:].strip('.'))
            return [first, second]
        else:
            n=pos
    elif pos[0] in INTS:
        if pos[1]=='.':
            n=d[0:3]
        elif pos[2]=='.':
            n=d[1:4]
        else: 
            n=d[2:5]
    elif pos[1] in INTS:
        if pos[0]=='.'and pos[2]=='.':
            n=pos[1]
        elif pos[0]=='.':
            n=d[3:6]
        elif pos[2]=='.':
            n=d[1:4]
        else:
            print('pos: ',pos)
            n=pos
    elif pos[2] in INTS:
        if pos[1]=='.':
            n=d[4:]
    else:
        print(pos, d)
        exit(0)
    if n == 1:
        print(pos,d)
    n=int(str(n).strip('.'))
    return n
    
def symbol_points(symbols):
    symbol_points = []
    for line in range(len(input)):
        for character in range(len(input[line])):
            cv = input[line][character]
            if cv in symbols:
                symbol_points.append([line, character])
    return symbol_points

def udlr(x,y):
    up = input[y-1][x-1:x+2]
    down = input[y+1][x-1:x+2]
    left = input[y][x-1]
    right = input[y][x+1]
    return up, down, left, right

def get_points(up,down,left,right,x,y):
    points=[]
    up_p = check_points(up,input[y-1][x-3:x+4])
    down_p= check_points(down,input[y+1][x-3:x+4])
    left_p = check_points(left,input[y][x-3:x].strip('.'))
    right_p = check_points(right,input[y][x+1:x+4].strip('.'))
    print(up_p+down_p+left_p+right_p)
    points = up_p+down_p+left_p+right_p
    return points
    
def check_points(dir, coords):
    points = []
    o = check_str(dir,coords)
    if type(o) == list:
        points=o
    else:
        points=[o]
    return points
   

## part one ##
def part_one():
    symbols = get_symbols(input)
    sps = symbol_points(symbols)
    total=0
    for point in sps:
        y,x = point
        up,down,left,right = udlr(x,y)
        points = get_points(up,down,left,right,x,y,[0,0,0,0])
        total+=sum(points)
    print(total)    
    return

## part two ##
def part_two():
    pointsum = 0
    sps = symbol_points(['*'])
    for point in sps:
        y,x = point
        points=udlr(x,y)
        up, down, left, right = points
        p = get_points(up,down,left,right,x,y)
        if len(p)==5:
            rt=(p[0]*p[1]*p[2]*p[3]*p[4])
        else:
            oc = [str(i) for i in p].count('1')
            if oc <=2:
                rt=(p[0]*p[1]*p[2]*p[3])
            else:
                rt=0
        pointsum+=rt
    print(pointsum)
    return

input = read_file('data/d3.txt')
part_one() # 528799
part_two() # 84907174
