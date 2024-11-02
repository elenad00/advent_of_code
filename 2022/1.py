"""
--- Day 1: Calorie Counting ---
The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

For example, suppose the Elves finish writing their items' Calories and end up with the following list:
    1000
    2000
    3000

    4000

    5000
    6000

    7000
    8000
    9000

    10000
This list represents the Calories of the food carried by five Elves:
    The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
    The second Elf is carrying one food item with 4000 Calories.
    The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
    The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
    The fifth Elf is carrying one food item with 10000 Calories.

In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

--- Part Two ---
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

"""

import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)

import aoc_utils

def get_elf_calories():
    all_elf_cals = []
    elf_cals = 0
    for cal in input:
        if cal == '':
            all_elf_cals.append(elf_cals)
            elf_cals = 0
        else:
            elf_cals+=int(cal)
    all_elf_cals = sorted(all_elf_cals, reverse=True)
    return all_elf_cals

def part_one():
    all_elf_cals = get_elf_calories()
    print(all_elf_cals[0])
    return

def part_two():
    all_elf_cals = get_elf_calories()
    print(sum(all_elf_cals[0:3]))
    return

input = aoc_utils.read_file('data/d1.txt')
part_one() # 74198
part_two() # 209914