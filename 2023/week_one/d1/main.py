## aoc 2023 - day 1 ##
##    by elena d    ##

## imports
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from aoc_utils import *

## part one ##
def part_one():
    test_input = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
    sum = 0
    for group in input:
        ints = [v for v in group if v in INTS]
        #print(ints)
        ints = int(ints[0]+ints[-1])
        sum+=ints
    print(sum)
    return

## part two ##
def part_two():
    test_input=['two1nine','eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']
    sum = 0
    for group in input:
        ng = []
        for i in range(len(group)):
            if group[i] in INTS: 
                ng.append(group[i])
            
            elif group[i] == 'o':
                if group[i:i+3] == 'one':
                    ng.append('1')
                    i+=3
            elif group[i] == 't':
                if group[i:i+3] == 'two':
                    ng.append('2')
                    i+=3
                elif group[i:i+5] == 'three':
                    ng.append('3')
                    i+=5
            elif group[i] == 'f':
                if group[i:i+4] == 'four':
                    ng.append('4')
                    i+=4
                if group[i:i+4] == 'five':
                    ng.append('5')
                    i+=4
            elif group[i] == 's':
                if group[i:i+3] == 'six':
                    ng.append('6')
                    i+=3
                elif group[i:i+5] == 'seven':
                    ng.append('7')
                    i+=5
            elif group[i] == 'e':
                if group[i:i+5] == 'eight':
                    ng.append('8')
                    i+=5
            elif group[i] == 'n':
                if group[i:i+4] == 'nine':
                    ng.append('9')
                    i+=4
            elif group[i] == 'z':
                if group[i:i+4] == 'zero':
                    ng.append('0')
                    i+=4
            #print(group, ng)
            i+=1
            
        ints = int(ng[0]+ng[-1])
        print(ints)
        sum+=ints
    print(sum)
    return

input = read_file('input.txt')
part_one() # 55971
part_two() # 54719