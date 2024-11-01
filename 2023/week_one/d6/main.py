## aoc 2023 - day 6 ##
##    by elena d    ##

## imports
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from aoc_utils import *

times=[58996469]
records=[478223210191071]
for i in range(len(times)):
    c = 0
    record = records[i]
    time=times[i]
    for i in range(time):
        distance = i*(time-i)
        if distance>record:c+=1
    print(c) # 128700, 39594072
