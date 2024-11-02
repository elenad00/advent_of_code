""" 
--- Day 5: If You Give A Seed A Fertilizer ---

The almanac (your puzzle input) lists all of the seeds that need to be planted. It also lists what type of soil to use with each kind of seed, what type of fertilizer to use with each kind of soil, what type of water to use with each kind of fertilizer, and so on. Every type of seed, soil, fertilizer and so on is identified with a number, but numbers are reused by each category - that is, soil 123 and fertilizer 123 aren't necessarily related to each other.

For example:
    seeds: 
        79 14 55 13
    seed-to-soil map:
        50 98 2
        52 50 48
    soil-to-fertilizer map:
        0 15 37
        37 52 2
        39 0 15
    fertilizer-to-water map:
        49 53 8
        0 11 42
        42 0 7
        57 7 4
    water-to-light map:
        88 18 7
        18 25 70
    light-to-temperature map:
        45 77 23
        81 45 19
        68 64 13
    temperature-to-humidity map:
        0 69 1
        1 0 69
    humidity-to-location map:
        60 56 37
        56 93 4
The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.

The rest of the almanac contains a list of maps which describe how to convert numbers from a source category into numbers in a destination category. That is, the section that starts with seed-to-soil map: describes how to convert a seed number (the source) to a soil number (the destination). This lets the gardener and his team know which soil to use with which seeds, which water to use with which fertilizer, and so on.

Rather than list every source number and its corresponding destination number one by one, the maps describe entire ranges of numbers that can be converted. Each line within a map contains three numbers: the destination range start, the source range start, and the range length.

Consider again the example seed-to-soil map:
    50 98 2
    52 50 48
The first line has a destination range start of 50, a source range start of 98, and a range length of 2. This line means that the source range starts at 98 and contains two values: 98 and 99. The destination range is the same length, but it starts at 50, so its two values are 50 and 51. With this information, you know that seed number 98 corresponds to soil number 50 and that seed number 99 corresponds to soil number 51.

The second line means that the source range starts at 50 and contains 48 values: 50, 51, ..., 96, 97. This corresponds to a destination range starting at 52 and also containing 48 values: 52, 53, ..., 98, 99. So, seed number 53 corresponds to soil number 55.

Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.

So, the entire list of seed numbers and their corresponding soil numbers looks like this:
    seed  soil
    0     0
    1     1
    ...   ...
    48    48
    49    49
    50    52
    51    53
    ...   ...
    96    98
    97    99
    98    50
    99    51
With this map, you can look up the soil number required for each initial seed number:
    Seed number 79 corresponds to soil number 81. x+2
    Seed number 14 corresponds to soil number 14. x+0
    Seed number 55 corresponds to soil number 57. x+2
    Seed number 13 corresponds to soil number 13. x+0
The gardener would like to know the closest location that needs a seed.
Using these maps, find the lowest location number that corresponds to any of the initial seeds. To do this, you'll need to 
    S 79, soil 81, fertilizer 81, water 81, light 74, temp 78, humidity 78, location 82.
    S 14, soil 14, fertilizer 53, water 49, light 42, temp 42, humidity 43, location 43.
    S 55, soil 57, fertilizer 57, water 53, light 46, temp 82, humidity 82, location 86.
    S 13, soil 13, fertilizer 52, water 41, light 34, temp 34, humidity 35, location 35.
So, the lowest location number in this example is 35.

What is the lowest location number that corresponds to any of the initial seed numbers?

--- Part Two ---

Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

The values on the initial seeds: line come in pairs.
Within each pair, the first value is the start of the range and the second value is the length of the range. So, in the first line of the example above:
    seeds: 79 14 55 13
This line describes two ranges of seed numbers to be planted in the garden. 
The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. 
The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed number 82, soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. 
So, the lowest location number is 46.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. 
What is the lowest location number that corresponds to any of the initial seed numbers?

"""
## imports
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from aoc_utils import *

def clean_block(block):
    return (block.replace(':','').replace('\n', ',')).split(',')[1:]

def handle_blocks():
    blocks = list(map(clean_block, input))
    block_ranges = list()
    for block in blocks[1:]:
        dtos = dict()
        for line in block:
            dest, source, length = [int(x) for x in line.split(' ')]
            difference = dest-source
            d_range = range(source,source+length)
            dtos[d_range] = difference
        block_ranges.append(dtos)
    return block_ranges

def get_seeds():
    seeds=[int(x) for x in (input[0].split(': ')[1].split(' '))]
    i = 0
    new_seeds = list()
    for i in range(0,len(seeds),2):
        new_seeds.append(range(seeds[i],seeds[i]+seeds[i+1]))
    return new_seeds

def map_location(source):
    for i in range(len(blocks)):
        block = blocks[i]
        val_range=[b for b in block if source in b]
        if val_range!=[]:
            difference=block[val_range[0]]
            source=source+difference
    return source

def part_one():
    locations=list()
    seeds = [int(x) for x in (input[0].split(': ')[1].split(' '))]
    for seed in seeds:
        locations.append(map_location(seed))
    print(min(locations))
    
def part_two():
    seeds = get_seeds()
    for seed_block in seeds:
        mini = map(map_location,seed_block)
        mini = filter(lambda x:(x<86430059), mini)
        

test_input = read_file('test.txt','\n\n')
input = read_file('input.txt', '\n\n')
# input=test_input

blocks = handle_blocks()
#part_one() #  261668924
part_two() # 2988525823 (too high)
           #   86430059 (too high)
           #   60295510 (incorrect)
           #   24261545 