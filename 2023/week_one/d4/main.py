## aoc 2023 - day   ##
##    by elena d    ##

## imports
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from aoc_utils import *

# functions
def get_wins_lines(line):
    winning, card_numbers = line.split(': ')[1].split(' | ')  
    winning = get_list(winning)
    card_numbers = get_list(card_numbers)
    return winning, card_numbers

def get_match_count(winning, card_numbers):
    return len([c for c in winning if c in card_numbers])

def get_list(input_str):
    inp_list = input_str.replace('  ',' ').split(' ')
    if '' in inp_list: inp_list.remove('')
    return inp_list 

def gen_blank_list(x):
    return [x for g in range(len(inp_text))]

def get_card_points(line):
    wins,nums = get_wins_lines(line)
    card_points = get_match_count(wins,nums)
    return card_points

# part one
def part_one():
    stack_points = 0
    for line in inp_text:
        card_points = get_card_points(line)
        if card_points!=0:
            card_points=2**(card_points-1)
        stack_points+=(card_points)
    print(stack_points) 

# part two
def part_two():
    card_runs=gen_blank_list(1)
    gen_cards=[]
    for line in inp_text:
        card_points = get_card_points(line)
        gen_cards.append(card_points)
    print('---')
    i=0
    for run in card_runs:
        for r in range(run):
            new_cards = gen_cards[i]
            for c in range(1,(new_cards+1)):
                card_runs[i+c]+=1
        i+=1  
    print(sum(card_runs))
        
test_input = [
    'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'
]
inp_text = read_file('input.txt')
#inp_text=test_input

part_one() # 25010
part_two() # 9924412

