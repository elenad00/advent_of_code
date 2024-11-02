"""
--- Day 2: Rock Paper Scissors ---

The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. 
The second column is what you should play in response: X for Rock, Y for Paper, and Z for Scissors. 

Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. 
Your total score is the sum of your scores for each round. 
The score for a single round is the score for the shape you selected 
    (1 for X, 2 for Y, and 3 for Z) 
    plus the score for the outcome of the round 
    (0 if you lost, 3 if the round was a draw, and 6 if you won).

For example, suppose you were given the following strategy guide:
    A Y
    B X
    C Z
This strategy guide predicts and recommends the following:
    In the first round, your opponent will choose Rock (A), and you should choose Paper (Y).
        This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
    In the second round, your opponent will choose Paper (B), and you should choose Rock (X). 
        This ends in a loss for you with a score of 1 (1 + 0).
    The third round is a draw with both players choosing Scissors, 
        giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?

-- Part Two --

The second column says how the round needs to end: 
    X means you need to lose, 
    Y means you need to end the round in a draw, 
    Z means you need to win. 

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), 
    and you need the round to end in a draw (Y), 
    so you also choose Rock. 
    This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B),
    and you choose Rock so you lose (X) 
    with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with 
    Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?


Paper (BY) beats rock (AX)
Scissors (CZ) beats paper (BY)
Rock (AX) beats scissors (CZ)

rock = A, X
paper = B, Y
scissors = C, Z
X = lose
Y = draw
Z = win
"""

import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
import aoc_utils

def get_outcome(opp: str, me: str) -> int:
    if opp == "A":
        if me=="X": return 3
        elif me=="Y": return 6
        else: return 0
    if opp=="B":
        if me=="X": return 0
        elif me=="Y": return 3
        else: return 6
    if opp=="C":
        if me=="X": return 6
        elif me=="Y": return 0
        else: return 3
    return

def calculate_outcome(opp: str, me: str) -> list[int, str]:
    if opp == "A":
        if me=="X": return 0, "Z"
        elif me=="Y": return 3, "X"
        else: return 6, "Y"
    if opp=="B":
        if me=="X": return 0, "X"
        elif me=="Y": return 3, "Y"
        else: return 6, "Z"
    if opp=="C":
        if me=="X": return 0, "Y"
        elif me=="Y": return 3, "Z"
        else: return 6, "X"
    return

def get_my_choice(mine) -> int:
    if mine == 'X': return 1
    elif mine == 'Y': return 2
    elif mine == "Z": return 3


def part_one():
    score = 0
    for game in input:
        opp, mine = game
        choice_score = get_my_choice(mine)
        outcome_score = get_outcome(opp, mine)
        score+=(choice_score+outcome_score)
    print(score)
    return

def part_two():
    score = 0
    for game in input:
        opp, mine = game
        outcome_score, choice = calculate_outcome(opp, mine)
        choice_score = get_my_choice(choice)
        score+=(outcome_score+choice_score)
    print(score)
    return

input = aoc_utils.read_file('data/d2.txt', listify=True, list_delim=" ")
part_one() # 12855
part_two() # 13726