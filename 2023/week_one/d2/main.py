## aoc 2023 - day 2 ##
##    by elena d    ##

## imports
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from aoc_utils import *

## part one ##
def part_one():
    possible_games = 0
    for game in input:
        minimums = {'red':0,'blue':0,'green':0}
        game_number = int(game.split(':')[0].split(' ')[-1])
        games = game.split(':')[1][1:].split('; ')
        games = [g.split(', ') for g in games]
        for round in games:
            for pull in round:
                number, colour = pull.split(' ')
                number=int(number)
                if minimums[colour]<number:
                    minimums[colour]=number
        if (
            minimums['red']<=12 and
            minimums['blue']<=14 and
            minimums['green']<=13
        ):
            possible_games+=game_number
    
    print(possible_games)
    return

## part two ##
def part_two():
    sum_games = 0
    for game in input:
        minimums = {'red':0,'blue':0,'green':0}
        game_number = int(game.split(':')[0].split(' ')[-1])
        games = game.split(':')[1][1:].split('; ')
        games = [g.split(', ') for g in games]
        for round in games:
            for pull in round:
                number, colour = pull.split(' ')
                number=int(number)
                if minimums[colour]<number:
                    minimums[colour]=number
        game_power = minimums['red'] * minimums['blue'] * minimums['green']
        sum_games+=game_power
    print(sum_games)
    return

test_input = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
]

input = read_file('input.txt')
part_one() # 3059
part_two() # 65371

# cubes are red, green or blue
# looking for the sum of the id numbers where the game is only possible if the bag
# had been loaded with 12r 13g and 14b