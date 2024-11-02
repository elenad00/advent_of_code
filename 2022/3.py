"""
day three part one 

one rucksack = two compartments
all items must go into exactly one compartment

imput = list of figures in each rucksack

every item type is identified by a single lower or upper case item
the first half of the string represents the first compartment
the second half of the string represnts the second compartment

a-z = 1-26
A-Z = 27-52

TASK:
find the items that appear in both compartments
and then find the sum of those items
"""

f = open('data/d3.txt', 'r')
backpacks = f.read()
backpacks = backpacks.split('\n')

def part_one():
    sum_common = 0
    i = 1
    count = 0
    for i in range(0,3):
        backpack = backpacks[i+count]
        common = ''
        splitat = int(len(backpack)/2)
        comp1 = backpack[:splitat]
        comp2 = backpack[splitat:]
        for char in comp1:
            if char in comp2:
                common = char
        if ord(common) >= 97:
            val = (ord(common)-96)
        else:
            val = (ord(common)-38)
        sum_common+=val
    print(sum_common)

def part_two():
    sum_common = 0
    i = 1
    count = 0
    for i in range(0,len(backpacks),3):
        b1 = backpacks[i]
        b2 = backpacks[i+1]
        b3 = backpacks[i+2]
        common = ''
        for char in b1:
            if char in b2 and char in b3:
                common = char
        if ord(common) >= 97:
            val = (ord(common)-96)
        else:
            val = (ord(common)-38)
        sum_common+=val
    print(sum_common)
    
part_one() # 12
part_two() # 2525