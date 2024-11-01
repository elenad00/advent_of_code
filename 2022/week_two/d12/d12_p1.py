# d12_p1
# reach E in as few steps as possible
# you can only move places if the elevation is e+1 or <e

x = 0
y = 0

f = open('d12_test.txt', 'r')
#f = open('d12_data.txt', 'r')
heightmap = f.read().split('\n')
for i in range(len(heightmap)):
  heightmap[i] = list(heightmap[i])
  row = heightmap[i]
  for v in range(len(row)):
    if row[v] == 'E':
      print(f"End is at {i}, {v}")
    if row[v] == 'S':
      print(f"Start is at {i}, {v}")
      x = i
      y = v
    row[v] = ord(row[v])

value = ord('a')

visited = ['']

xm = len(heightmap)
ym = len(heightmap[0])

E = False
sc = 1




#print(north, south, east, west)


while not E:
  north = (x-1, y)
  east = (x, y+1)
  south = (x+1, y)
  west = (x, y-1)
  if x-1 >= 0 and heightmap[x-1][y] == value+1 and north not in visited:
    x-=1
  elif y+1<ym and heightmap[x][y+1] == value+1 and east not in visited:
    y+=1
  elif x+1<xm and heightmap[x+1][y] == value+1 and south not in visited:
    x+=1
  elif y-1>=0 and heightmap[x][y-1] == value+1 and west not in visited:
    y-=1
  
  elif x-1>=0 and heightmap[x-1][y] == value and north not in visited:
    x-=1
  elif y+1<ym and heightmap[x][y+1] == value and east not in visited:
    y+=1
  elif x+1<xm and heightmap[x+1][y] == value and south not in visited:
    x+=1
  elif y-1>=0 and heightmap[x][y-1] == value and west not in visited:
    y-=1
  
  elif 69 in (heightmap[x][y+1], heightmap[x+1][y], heightmap[x-1][y], heightmap[x][y-1]):
    E = True
    break

  else:
    print("Not Caught")
    print(x, y, value, sc)
    exit(0)
  
  print(x, y, chr(value), sc)
  value = heightmap[x][y]
  visited.append((x,y))
  sc+=1

  if sc>xm*ym:
    print(visited)
    print("Over max")
    print(x, y, value, sc)
    exit(0)

print(sc)