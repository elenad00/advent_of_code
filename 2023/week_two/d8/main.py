## aoc 2023 - day 8 ##
##    by elena d    ##

## imports
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from aoc_utils import *

## part one ##
def part_one(place):
    c = 0
    while place[2]!='Z':
        for pos in rl:
            place = coords[place][int(pos)]
            c+=1
    print(c)
    return c

## part two ##
def part_two():
    steps = []
    for val in start_vals:
        steps.append(part_one(val))
    return

test_input = [
    'LR',
    '11A = (11B, XXX)',
    '11B = (XXX, 11Z)',
    '11Z = (11B, XXX)',
    '22A = (22B, XXX)',
    '22B = (22C, 22C)',
    '22C = (22Z, 22Z)',
    '22Z = (22B, 22B)',
    'XXX = (XXX, XXX)'
]
input = read_file('input.txt')
input = test_input

coords = {}
rl = input[0]
rl = rl.replace('L','0').replace('R','1')
print(rl)
raw_coords = input[1:]
for line in raw_coords:
    x,y = line.split(' = ')
    coords[x]=(y.strip('(').strip(')')).split(', ')
start_vals = [v for v in coords if v[2] == 'A']
print(start_vals)    
#part_one('AAA') # 11309
part_two() # 13740108158591