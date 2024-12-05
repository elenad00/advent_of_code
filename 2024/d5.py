"""
--- Day 5: Print Queue ---
--- Part One ---
Safety protocols clearly indicate that new pages for the safety manuals must be printed in a very specific order. The notation X|Y means that if both page number X and page number Y are to be produced as part of an update, page number X must be printed at some point before page number Y.

The Elf has for you both the page ordering rules and the pages to produce in each update (your puzzle input), but can't figure out whether each update has the pages in the right order.

For example:
    The first section specifies the page ordering rules, one per line. 
        The first rule, 47|53, means that if an update includes both page number 47 and page number 53, then page number 47 must be printed at some point before page number 53. (47 doesn't necessarily need to be immediately before 53; other pages are allowed to be between them.)
    The second section specifies the page numbers of each update. Because most safety manuals are different, the pages needed in the updates are different too. The first update, 75,47,61,53,29, means that the update consists of page numbers 75, 47, 61, 53, and 29.

To get the printers going as soon as possible, start by identifying which updates are already in the right order.
In the above example, the first update (75,47,61,53,29) is in the right order:
    75 is correctly first because there are rules that put each other page after it: 75|47, 75|61, 75|53, and 75|29.
    47 is correctly second because 75 must be before it (75|47) and every other page must be after it according to 47|61, 47|53, and 47|29.
    61 is correctly in the middle because 75 and 47 are before it (75|61 and 47|61) and 53 and 29 are after it (61|53 and 61|29).
    53 is correctly fourth because it is before page number 29 (53|29).
    29 is the only page left and so is correctly last.
    Because the first update does not include some page numbers, the ordering rules involving those missing page numbers are ignored.
    The second and third updates are also in the correct order according to the rules. Like the first update, they also do not include every page number, and so only some of the ordering rules apply - within each update, the ordering rules that involve missing page numbers are not used.
    The fourth update, 75,97,47,61,53, is not in the correct order: it would print 75 before 97, which violates the rule 97|75.
    The fifth update, 61,13,29, is also not in the correct order, since it breaks the rule 29|13.
    The last update, 97,13,75,29,47, is not in the correct order due to breaking several rules.

For some reason, the Elves also need to know the middle page number of each update being printed. Because you are currently only printing the correctly-ordered updates, you will need to find the middle page number of each correctly-ordered update. In the above example, the correctly-ordered updates are:
    75,47,61,53,29
    97,61,53,29,13
    75,29,13
    These have middle page numbers of 61, 53, and 29 respectively. Adding these page numbers together gives 143.
Of course, you'll need to be careful: the actual list of page ordering rules is bigger and more complicated than the above example.
Determine which updates are already in the correct order. What do you get if you add up the middle page number from those correctly-ordered updates?
"""
"""
--- Part Two ---
For each of the incorrectly-ordered updates, use the page ordering rules to put the page numbers in the right order. For the above example, here are the three incorrectly-ordered updates and their correct orderings:
    75,97,47,61,53 becomes 97,75,47,61,53.
    61,13,29 becomes 61,29,13.
    97,13,75,29,47 becomes 97,75,47,29,13.
After taking only the incorrectly-ordered updates and ordering them correctly, their middle page numbers are 47, 29, and 47. Adding these together produces 123.

Find the updates which are not in the correct order. What do you get if you add up the middle page numbers after correctly ordering just those updates?
"""

import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
import aoc_utils

def check_rule(rule, page):
    try:
        p_one = page.index(rule[0])
        p_two = page.index(rule[1])
    except ValueError:
        return True
    return True if p_one < p_two else False
    
def line_splitter(delim, line):
    return [r.split(delim) for r in line.split('\n')]

def part_one():
    mid_sum = 0
    for page in pages:
        rules_broken = False
        for rule in rules:
            valid = check_rule(rule,page)
            if not valid:
                rules_broken = True
        if not rules_broken:
            mid_sum += int(page[int(len(page)/2)])
    print(mid_sum)       
    return

def go_fix(rule, page):
    p_one = page.index(rule[0])
    p_two = page.index(rule[1])
    page.insert(p_two,page.pop(p_one))
    return page

def check_rules(rules, page):
    for rule in rules:
        mid_sum=0
        valid = check_rule(rule,page)
        if not valid:
            page = go_fix(rule, page)
            print(page)
            valid = check_rules(rules, page)
            if valid:
                mid_sum += int(page[int(len(page)/2)])
                print(mid_sum)
            else:
                print('still not valid')
    return mid_sum
                    
def part_two():
    mid_sum = 0
    for page in pages:
        mid_sum+=check_rules(rules, page)
    print(mid_sum)
    return

input = aoc_utils.read_file('test_data/d5.txt',delim='\n\n')
rules=line_splitter('|', input[0])
pages=line_splitter(',', input[1])
part_one() # 5064
part_two()