## aoc 2023 - day 5 ##
##    by elena d    ##

## imports
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from aoc_utils import *

def clean_block(block):
    return (block.replace(':','').replace('\n', ',')).split(',')[1:]

def handle_blocks():
    blocks = list(map(clean_block, input))
    block_ranges = list()
    for block in blocks[1:]:
        dtos = dict()
        for line in block:
            dest, source, length = [int(x) for x in line.split(' ')]
            difference = dest-source
            d_range = range(source,source+length)
            dtos[d_range] = difference
        block_ranges.append(dtos)
    return block_ranges

def get_seeds():
    seeds=[int(x) for x in (input[0].split(': ')[1].split(' '))]
    i = 0
    new_seeds = list()
    for i in range(0,len(seeds),2):
        new_seeds.append(range(seeds[i],seeds[i]+seeds[i+1]))
    return new_seeds

def map_location(source):
    for i in range(len(blocks)):
        block = blocks[i]
        val_range=[b for b in block if source in b]
        if val_range!=[]:
            difference=block[val_range[0]]
            source=source+difference
    return source

def part_one():
    locations=list()
    seeds = [int(x) for x in (input[0].split(': ')[1].split(' '))]
    for seed in seeds:
        locations.append(map_location(seed))
    print(min(locations))
    
def part_two():
    seeds = get_seeds()
    for seed_block in seeds:
        mini = map(map_location,seed_block)
        mini = filter(lambda x:(x<86430059), mini)
        

test_input = read_file('test.txt','\n\n')
input = read_file('input.txt', '\n\n')
# input=test_input

blocks = handle_blocks()
#part_one() #  261668924
part_two() # 2988525823 (too high)
           #   86430059 (too high)
           #   60295510 (incorrect)
           #   24261545 