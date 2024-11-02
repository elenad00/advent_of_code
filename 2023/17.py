'''
--- Day 17: Clumsy Crucible ---

The Elves here have a map that uses traffic patterns, ambient temperature, and hundreds of other parameters to calculate exactly how much heat loss can be expected for a crucible entering any particular city block.

Each city block is marked by a single digit that represents the amount of heat loss if the crucible enters that block. 
The starting point, the lava pool, is the top-left city block
The destination, the machine parts factory, is the bottom-right city block. 
(Because you already start in the top-left block, you don't incur that block's heat loss unless you leave that block and then return to it.)

Because it is difficult to keep the top-heavy crucible going in a straight line for very long, it can move at most three blocks in a single direction before it must turn 90 degrees left or right. The crucible also can't reverse direction; after entering each city block, it may only turn left, continue straight, or turn right.

One way to minimize heat loss is this path:
    2>>34^>>>1323
    32v>>>35v5623
    32552456v>>54
    3446585845v52
    4546657867v>6
    14385987984v4
    44578769877v6
    36378779796v>
    465496798688v
    456467998645v
    12246868655<v
    25465488877v5
    43226746555v>
This path never moves more than three consecutive blocks in the same direction and incurs a heat loss of only 102.

Directing the crucible from the lava pool to the machine parts factory, but not moving more than three consecutive blocks in the same direction, what is the least heat loss it can incur?

'''
'''
2413432311323  2>>34^>>>1323
3215453535623  32v>>>35v5623
3255245654254  32552456v>>54
3446585845452  3446585845v52
4546657867536  4546657867v>6
1438598798454  14385987984v4
4457876987766  44578769877v6
3637877979653  36378779796v>
4654967986887  465496798688v
4564679986453  456467998645v
1224686865563  12246868655<v
2546548887735  25465488877v5
4322674655533  43226746555v>

- start top left
- finish bottom right
- cant go more than three three blocks in one direction
- cant reverse 
- what is the least heat loss
'''

from aoc_utils import Grid_Navigator

class HeatMapper(Grid_Navigator):
    start = [0,0]
    end = [12,12]
    heatloss = 0
    steps = 0
    
    def __init__(self, testing=False):
        if testing:
            file="2023/d17/test.txt"
        else:
            file="2023/d17/input.txt"
        self.heatmap = self.generate_grid(file)
    
    
    
heatmap = HeatMapper(True)
print(heatmap.check_around())