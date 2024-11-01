## aoc 2023 - day 9 ##
##    by elena d    ##

## imports
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from aoc_utils import *

def find_differences(line):
    differences = []
    for i in range(1, len(line)):
        differences.append(line[i]-line[i-1])
    return differences

## part one ##
def part_one():
    ex_list = []
    for line in test:
        end = []
        in_line = [int(x) for x in line.split()]
        differences = in_line
        while differences.count(0) != len(differences):
            differences = find_differences(differences)
            end.append(differences[-1])
        print(sum(end))
        extrapolated = (int(in_line[-1])+sum(end))
        ex_list.append(extrapolated)
        print('---')
    print(sum(ex_list))
    return

## part two ##
def part_two():
    ex_list = []
    for line in input:
        starts = []
        in_line = [int(x) for x in line.split()]
        differences = in_line
        while differences.count(0) != len(differences):
            differences = find_differences(differences)
            starts.append(differences[0])
        starts.reverse()
        s=0
        for i in range(1,len(starts)):
            s = starts[i]-s
        start = in_line[0] - s
        ex_list.append(start)
        print('---')
    print(sum(ex_list))
    return

# -3, 0, 5

test_input = []
input = read_file('input.txt')
test = ['0 3 6 9 12 15',
'1 3 6 10 15 21',
'10 13 16 21 30 45']
#part_one()
part_two()