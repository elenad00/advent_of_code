'''
To approximate the surface area, count the number of sides of each 
cube that are not immediately connected to another cube.
So, if your scan were only two adjacent cubes like 1,1,1 and 2,1,1, 
each cube would have a single side covered and five sides exposed,
a total surface area of 10 sides.

test answer is 64
'''

import numpy as np

np.set_printoptions(threshold=10000)

def main():
  new_droplets = []
  f = open("input.txt", 'r')
  #f = open("test.txt", 'r')
  droplets = f.read().split('\n')

  for d in droplets:
    d = d.split(',')
    new_droplets.append((int(d[0]),int(d[1]),int(d[2])))
    
  droplets = sorted(new_droplets, key=lambda x:x[2])
  drop = np.zeros((21,21,21), dtype=int)
  #drop = np.zeros((20,20,20), dtype=int)

  for d in droplets:
    drop[d[2]][d[1]][d[0]] = 1
  #print(drop)
  #part_one(drop, 1)
  part_two(drop) 

def part_two(drop):
  p = 0
  airgaps = []
  for z in range(20):
    for y in range(20):
      inner = False
      ag = []
      for x in range(20):
       #print(drop[z][y][x], inner)
        if drop[z][y][x]==1 and not inner: inner=True
        elif drop[z][y][x]==0 and inner: ag.append((x,y,z))
        elif drop[z][y][x]==1 and inner: inner = False
      print(ag)
      if len(ag)>0 and not inner:
        airgaps+=ag
  
  #print("Airgaps:", airgaps)
  ags = np.zeros((21,21,21), dtype=int)
  for d in airgaps:
    ags[d[2]][d[1]][d[0]] = 1
  #print(ags)
  # for i in range(len(ags)):
  #   print(f"{i}")
  #   print(drop[i])
  #   print(ags[i])
  p = part_one(ags,1)
  print(3432-p)

def part_one(drop, v):
  p = 0
  for z in range(20):
    for y in range(20):
      for x in range(20):
        if drop[z][y][x] == v:
          possides = 6
          if drop[z+1][y][x] == v:possides-=1
          if drop[z-1][y][x] == v:possides-=1
          if drop[z][y+1][x] == v:possides-=1
          if drop[z][y-1][x] == v:possides-=1
          if drop[z][y][x+1] == v:possides-=1
          if drop[z][y][x-1] == v:possides-=1
          if possides<=5:
            p+=possides
  print(p) 
  return(p)
  # 3434 - too high
  # 3432 #
  # 3430 - too low

# 2618 - too high
# 2446 - incorrect
# 2420 - incorrect
# 2354 - incorrect
# 2174 - incorrect
# 2045 - incorrect
# 2042 - correct
# 2000 - too low

main()