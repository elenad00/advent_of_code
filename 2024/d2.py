""" 
--- Day 2: Red-Nosed Reports ---
-- Part One --
The data consists of many reports, one report per line. 
Each report is a list of numbers called levels that are separated by spaces. 
A report only counts as safe if both of the following are true:
    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:
    7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
    1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
    9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
    1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
    1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?
""" 
"""
--- Part Two ---
The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:
    7 6 4 2 1: Safe without removing any level.
    1 2 7 8 9: Unsafe regardless of which level is removed.
    9 7 6 2 1: Unsafe regardless of which level is removed.
    1 3 2 4 5: Safe by removing the second level, 3.
    8 6 4 4 1: Safe by removing the third level, 4.
    1 3 6 7 9: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
"""

REASONS = ['gap not between 3 and -3',
           'increasing but values decreasing',
           'decreasing but values increasing',
           'current val == next val']

import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
import aoc_utils

def check_value(cv: int, nv: int, increasing: bool):
    if not (-3<=cv-nv<=3):
        return False, REASONS[0]
    if increasing and cv>nv:
        return False, REASONS[1]
    if not increasing and nv>cv:
        return False, REASONS[2]
    if cv==nv:
        return False, REASONS[3]
    return True, ''

def check_report(report:str)->int:
    report = trim_report(report)
    increasing = False if report[0] > report[1] else True
    for v in range(len(report)-1):
        valid, _ = check_value(report[v], report[v+1], increasing)
        if valid: continue
        else: return 0
    return 1

def trim_report(report: str) -> list:
    return [int(v) for v in report.split(' ')]

def comb_report(raw_report: str):
    faults = 0
    report = trim_report(raw_report)
    increasing = False if report[0] > report[1] else True
    v = 0
    while v < len(report)-1:
        valid, reason = check_value(report[v], report[v+1], increasing)
        if not valid:
            print(report, reason)
            faults+=1
            if reason == REASONS[0]:
                if (-3<=report[v-1]-report[v+1]<=3):
                    print(f"may be fixable by removing {report[v]}")
            elif reason == REASONS[1] or reason == REASONS[2]:
                print(f"May be fixable by reversing the order of the table or removing {report[v]}")
            else:
                print(f"May be fixable by removing {report[v]}")
                report = report[0:v] + report[v+1:]
                v-=1
                valid, reason = check_value(report[v], report[v+1], increasing)
                if not valid:
                    return 0
            v+=1
        else:
            v+=1
    return 1
    
def refine_report(report:str, recheck=0):
    increasing = False if report[0] > report[1] else True
    checked = False
    for v in range(len(report)-1):
        try:
            valid, reason = check_value(report[v], report[v+1], increasing)
        except IndexError:
            valid, reason = check_value(report[v-1], report[v], increasing)
        if reason!='' and not checked: 
            try:
                valid, reason = check_value(report[v-1], report[v+1], increasing)
            except IndexError:
                valid, reason = check_value(report[v-2], report[v-1], increasing)
            if reason == REASONS[0]:
                # check to see if the next value is less than -3/3
                valid, reason = check_value(report[v-1], report[v+1], increasing)
                if valid:
                    report.pop(v)
                    checked = True
                else:
                    return 0
            elif reason == REASONS[1] or reason == REASONS[2]:
                # check to see if removing val makes the values right
                if valid:
                    report.pop(v)
                    checked = True
                else:
                    valid, reason = check_value(report[v-1], report[v+1],increasing)
                    if valid:
                        report.pop(v)
                        checked = True
                    else:
                        valid, reason = check_value(report[v-1], report[v+1], not increasing)
                        if valid:
                            report.pop(v)
                            increasing = not increasing
                            checked = True
                        else:
                            return 0
            elif reason == REASONS[3]:
                valid, reason = check_value(report[v-1], report[v+1], not increasing)
                if valid:
                    report.pop(v)
                    checked = True
                else:
                    return 0
            else:
                report.pop(v)
                checked = True
    
    if not recheck:
        valid = refine_report(report, recheck=1)
    if not valid:
        return 0
    else: 
        return 1
    
def part_one():
    safe = 0
    for report in input:
        safe+=check_report(report)
    print(safe) # 299      
    return

def part_two():
    safe = 0
    for report in input:
        res = check_report(report)
        if not res:
            report = trim_report(report)
            res = refine_report(report)
            print(res)
        safe+=res
    print(safe) # 364  
    return

input = aoc_utils.read_file('data/d2.txt')
part_one()
part_two()