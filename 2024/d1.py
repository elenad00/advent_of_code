""" 
--- Day 1: Historian Hysteria ---
-- Part One --

Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. 

Your actual left and right lists contain many location IDs. What is the total distance between your lists?

-- Part Two --
This time, you'll need to figure out exactly how often each number from the left list appears in the right list. Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.

For these example lists, here is the process of finding the similarity score:
    The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
    The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
    The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).
    The fourth number, 1, also does not appear in the right list.
    The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
    The last number, 3, appears in the right list three times; the similarity score again increases by 9.
So, for these example lists, the similarity score at the end of this process is 31 (9 + 4 + 0 + 0 + 9 + 9).

Once again consider your left and right lists. What is their similarity score?
"""

import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
import aoc_utils

def get_l_and_r():
    left = []
    right = []
    for i in input:
        i = i.split('  ')
        left.append(i[0])
        right.append(i[1])
    left = sorted([int(i) for i in left])
    right = sorted([int(i) for i in right])
    return left, right

def part_one():
    sum = 0
    left, right = get_l_and_r()
    for i in range(len(left)):
        diff=(left[i]-right[i])
        if diff<0:
            diff=0-diff
        sum+=diff
    print(sum) # 1873376
    return

def part_two():
    sum = 0
    left, right = get_l_and_r()
    for i in left:
        count = right.count(i)
        sum+=count*i
    print(sum) # 18997088
    return

input = aoc_utils.read_file('data/d1.txt')
part_one()
part_two()