## aoc 2023 - day 3 ##
##    by elena d    ##

## imports
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
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
        adjs = [p for p in points if p!='.' and p!='...']
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

test_input = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..',
    '120.78....',
    '...*......',
    '..........'
]

input = read_file('3_input.txt')
#input=test_input
#part_one() # 521778 (too low) 528799
part_two() # 80,387,047 (too low) 84,926,685 (too high) 84907174
