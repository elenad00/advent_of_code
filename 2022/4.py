def process(line):
    first, second = line.split(',')
    start1, end1 = map(int, first.split('-'))
    start2, end2 = map(int, second.split('-'))
    return start1, end1, start2, end2
        
def part_one():
    ans = 0
    for line in lines:
        start1, end1, start2, end2 = process(line)
        if start1 <= start2 <= end2 <= end1:
            ans += 1
        elif start2 <= start1 <= end1 <= end2:
            ans += 1
    print(ans)

def part_two():
    ans = len(lines)
    for line in lines:
        start1, end1, start2, end2 = process(line)
        if start1 > end2 or start2 > end1:
            ans -= 1
    print(ans)
    
with open('data/d4.txt') as file:
    lines = file.read().splitlines()
    
part_one() # 441
part_two() # 861