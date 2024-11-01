## aoc 2023 - day 7 ##
##    by elena d    ##

## imports
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from aoc_utils import *

def split_cards(hand, part=1):
    hand_types = [
        [5], [4,1], [3,2],
        [3,1,1], [2,2,1],
        [2,1,1,1], [1,1,1,1,1]
    ]
    if part == 2:
        ord_hand = [hand.count(card) for card in set(hand) if card != 'J'] or [0]  # only jokers
        ord_hand.sort(reverse=True)
        ord_hand[0] += hand.count('J')
    else:
        ord_hand = [hand.count(card) for card in set(hand)]
        ord_hand.sort(reverse=True)
    return hand_types.index(ord_hand)

def c_to_i(hand, part=1):
    if part == 1: 
        labels = 'AKQJT98765432'
    else: 
        labels = 'AKQT98765432J'
    ordered = (labels.index(card) for card in hand)
    return ordered

# part one
def part_one():
    hands = []
    for line in input:
        hand, bid = line.split(' ')
        encoded = (
            split_cards(hand),
            *c_to_i(hand),
            int(bid)
        )
        hands.append(encoded)
    hands.sort(reverse=True)
    winnings = sum(
        rank*hand[-1] for rank, hand in enumerate(hands, start=1)
    )
    print(winnings)

## part two ##
def part_two():
    hands = []
    for line in input:
        hand, bid = line.split(' ')
        encoded = (
            split_cards(hand, part=2),
            *c_to_i(hand, part=2),
            int(bid)
        )
        hands.append(encoded)
    hands.sort(reverse=True)
    winnings = sum(
        rank*hand[-1] for rank, hand in enumerate(hands, start=1)
    )
    print(winnings)

input = read_file('input.txt')


part_one() 
    # 246795406
part_two() 
    # 249356515
    # 249545115 (wrong)
    # 248836746 (too low)