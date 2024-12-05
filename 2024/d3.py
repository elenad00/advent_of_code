""" 
--- Day 3: Mull It Over ---
The computer appears to be trying to run a program, but its memory is corrupted. All of the instructions have been jumbled up!

It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

For example, consider the following section of corrupted memory:
    xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Only the four sections 
    mul(2,4)
    mul(5,5)
    mul(11,8)
    mul(8,5)
are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?
""" 
"""
--- Part Two ---
If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.

There are two new instructions you'll need to handle:
    The do() instruction enables future mul instructions.
    The don't() instruction disables future mul instructions.

Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

For example:
    xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))

This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are disabled because there is a don't() instruction before them. The other mul instructions function normally, including the one at the end that gets re-enabled by a do() instruction.

This time, the sum of the results is 48 (2*4 + 8*5).

Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?
"""

import re
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
import aoc_utils

def part_one(input:str):
    sum = 0
    regex = r"mul\((\d{1,3}),(\d{1,3})\)"
    search_res = re.findall(regex, input)
    for x, y in search_res:
        sum+=int(x)*int(y)
    print(sum) # 175700056
    return sum

def part_two(input: str):
    count = 0
    input = re.findall(r"do\(\).*?don't\(\)", input)
    for ret in input:
        print(len(ret))
        count += part_one(ret)
    print(count)
    # 128096826
    # 175700056
    # 83524390 too high
    # 71668682
    return

input = aoc_utils.read_file('test_data/d3.txt')[0]
# part_one(input)
input = aoc_utils.read_file('data/d3.txt', delim='\n\n')
part_two(input)