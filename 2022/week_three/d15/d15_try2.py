import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize, linewidth=1000)

row = 10

def main():
  f = open('d15_test.txt','r')
  coords = f.read().split('\n')
  sb = getsb(coords)
  linecount = 0
  
  beacons = []
  for s, b in sb:
    if s[1]==row:
      if b not in beacons:
        beacons.append(b)
        linecount+=1
    elif b[1]==row:
      if b not in beacons:
        beacons.append(b)
        linecount+=1
    
  sb, coords = mapranges(sb, beacons)
  coords = sorted(list(set(coords)))
  print(coords)
  print(len(coords))

# a = 26

def mapranges(sb, coords):
  for sensor, beacon in sb:
    totaldif = gettotaldif(sensor, beacon)
    co = 0
    for c in range(1-totaldif, totaldif+1):
      for d in range(co):
        if sensor[1]+d == row:
          coords.append((sensor[0],sensor[1]+d))
        elif sensor[1]-d == row:
          coords.append((sensor[0],sensor[1]-d))
      co+=1
  return (sb, coords)

def getsb(coords):  
  sb = []
  for coord in coords:
    coord = coord.split(' ')
    sensor = (int(coord[2][2:-1]), int(coord[3][2:-1]))
    beacon = (int(coord[8][2:-1]), int(coord[9][2:]))
    sb.append((sensor, beacon))
  return(sb)

def gettotaldif(sensor, beacon):
  x_dif = sensor[0]-beacon[0]
  y_dif = sensor[1]-beacon[1]

  if x_dif < 0: x_dif = 0-x_dif
  if y_dif < 0: y_dif = 0-y_dif

  totaldif = x_dif+y_dif
  return totaldif

main()