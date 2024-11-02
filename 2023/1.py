""" 
You try to ask why they can't just use a weather machine ("not powerful enough") 
    and where they're even sending you ("the sky") and why your map looks mostly blank 
    ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, 
    where do you think snow comes from") when you realize that the Elves are already loading 
    you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document 
    (your puzzle input) has been amended by a very young Elf who was apparently just 
    excited to show off her art skills. Consequently, the Elves are having trouble 
    reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally
    contained a specific calibration value that the Elves now need to recover. On each 
    ine, the calibration value can be found by combining the first digit and the
    last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding
    these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with 
    letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each
    line. For example:

two 1 nine
eight wo three
abc one 2 three xyz
x two ne 3 four
4 nine eight seven 2
z one ight 2 3 4
7 pqrst six teen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together 
    produces 281.

What is the sum of all of the calibration values?
"""

## imports
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from aoc_utils import *

## part one ##
def part_one():
    test_input = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
    sum = 0
    for group in input:
        ints = [v for v in group if v in INTS]
        #print(ints)
        ints = int(ints[0]+ints[-1])
        sum+=ints
    print(sum)
    return

## part two ##
def part_two():
    test_input=['two1nine','eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']
    sum = 0
    for group in input:
        ng = []
        for i in range(len(group)):
            if group[i] in INTS: 
                ng.append(group[i])
            
            elif group[i] == 'o':
                if group[i:i+3] == 'one':
                    ng.append('1')
                    i+=3
            elif group[i] == 't':
                if group[i:i+3] == 'two':
                    ng.append('2')
                    i+=3
                elif group[i:i+5] == 'three':
                    ng.append('3')
                    i+=5
            elif group[i] == 'f':
                if group[i:i+4] == 'four':
                    ng.append('4')
                    i+=4
                if group[i:i+4] == 'five':
                    ng.append('5')
                    i+=4
            elif group[i] == 's':
                if group[i:i+3] == 'six':
                    ng.append('6')
                    i+=3
                elif group[i:i+5] == 'seven':
                    ng.append('7')
                    i+=5
            elif group[i] == 'e':
                if group[i:i+5] == 'eight':
                    ng.append('8')
                    i+=5
            elif group[i] == 'n':
                if group[i:i+4] == 'nine':
                    ng.append('9')
                    i+=4
            elif group[i] == 'z':
                if group[i:i+4] == 'zero':
                    ng.append('0')
                    i+=4
            #print(group, ng)
            i+=1
            
        ints = int(ng[0]+ng[-1])
        print(ints)
        sum+=ints
    print(sum)
    return

input = read_file('input.txt')
part_one() # 55971
part_two() # 54719