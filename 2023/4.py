""" 
--- Part Two ---

There's no such thing as "points". Instead,
    scratchcards only cause you to win more
    scratchcards equal to the number of 
    winning numbers you have.

Specifically, you win copies of the 
    scratchcards below the winning card 
    equal to the number of matches.

So, if card 10 were to have 5 matching 
    numbers, you would win one copy each 
    of cards 11, 12, 13, 14, and 15.

Copies of scratchcards are scored like 
    normal scratchcards and have the same 
    card number as the card they copied. 

So, if you win a copy of card 10 and it has 
    5 matching numbers, it would then win a 
    copy of the same cards that the original 
    card 10 won: cards 11, 12, 13, 14, and 
    15. This process repeats until none of 
    the copies cause you to win any more 
    cards. (Cards will never make you copy 
    a card past the end of the table.)

This time, the above example goes differently:
    Card 1: 
        41 48 83 86 17
        83 86  6 31 17  9 48 53
    Card 2: 
        13 32 20 16 61
        61 30 68 82 17 32 24 19
    Card 3:  
        1 21 53 59 44
        69 82 63 72 16 21 14  1
    Card 4: 
        41 92 73 84 69
        59 84 76 51 58  5 54 83
    Card 5: 
        87 83 26 28 32
        88 30 70 12 93 22 82 36
    Card 6: 
        31 18 13 56 72
        74 77 10 23 35 67 36 11

Card 1 has four matching numbers,
    so you win one copy each of the next 
    four cards: cards 2, 3, 4, and 5.

Your original card 2 has two matching 
    numbers, so you win one copy each of cards 
    3 and 4.

Your copy of card 2 also wins one copy each 
    of cards 3 and 4.

Your four instances of card 3 (one original 
    and three copies) have two matching 
    numbers, so you win four copies each of 
    cards 4 and 5.

Your eight instances of card 4 (one 
    original and seven copies) have one 
    matching number, so you win eight 
    copies of card 5.

Your fourteen instances of card 5 (one 
    original and thirteen copies) have no 
    matching numbers and win no more cards.

Your one instance of card 6 (one original) 
    has no matching numbers and wins no more 
    cards.

Once all of the originals and copies have
   been processed, you end up with 
   
1 instance of card 1
2 instances of card 2
4 instances of card 3
8 instances of card 4
14 instances of card 5
1 instance of card 6

In total, you have 30 scratchcards!

Process all of the original and copied 
    scratchcards until no more scratchcards 
    are won. Including the original set of 
    scratchcards, how many total scratchcards
    do you end up with?
    
"""
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
import aoc_utils

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
        
inp_text = aoc_utils.read_file('data/d4.txt')

part_one() # 25010
part_two() # 9924412

