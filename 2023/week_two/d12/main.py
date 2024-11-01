## aoc 2023 - day 12 ##
##     by elena d    ##

## imports
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from aoc_utils import *

## part one ##
def part_one():
    for line in input:
        springs, config = line.split(' ')
        config = [int(c) for c in config.split(',')]
        total = sum(config)
        broken = springs.count('#')
        working = springs.count('.')
        unknown = springs.count('?')
        print(line)
        print(total,broken,working,unknown,config)
        '''
        we have 5 broken pipes
        3 are already mapped
        we have two points to map
        we have three unknown slots
        they must be mapped #.#
        there is only one place for them
        '''
        exit()
    return

## part two ##
def part_two():
    return

input = read_file('input.txt')
part_one()
part_two()

'''
1
4
1
1
4
10
'''