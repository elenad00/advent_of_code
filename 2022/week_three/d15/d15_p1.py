
def main():
  f = open('d15_input.txt','r')
  coords = f.read().split('\n')
  sb = getsb(coords)
  
  xm = sb[0][0][0]
  ym = sb[0][0][1]

  row = 10

  for s, b in sb:
    if s[0] < xm: xm=s[0]
    if b[0] < xm: xm=b[0]
    if s[1] < ym: ym=s[1]
    if b[1] < ym: ym=b[1]
  
  xm=-xm
  ym=-ym

  cb = []

  for s,b in sb:
    if s[1]+ym==row: cb.append((s[0]+xm, s[1]+ym))
    if b[1]+ym==row: cb.append((b[0]+xm, b[1]+ym))
  
  cb = list(set(cb))
  ir = sorted(list(set(mapranges(sb, xm, ym, row))))
  total = len(ir)
  print(ir)
  for coord in cb:
    if coord in ir: total-=1
  print(total)
  
def mapranges(sb, xm, ym, row):
  ir = []
  for sensor, beacon in sb:
    x_dif = sensor[0]-beacon[0]
    y_dif = sensor[1]-beacon[1]

    if x_dif < 0: x_dif = 0-x_dif
    if y_dif < 0: y_dif = 0-y_dif

    totaldif = x_dif+y_dif

    sensor_x = sensor[0]+xm
    sensor_y = sensor[1]+ym

    totaldif+=1
    #if sensor_y <= row <= sensor_y+totaldif:
    for t in range(totaldif):
      ir += check(sensor_x+t,sensor_y+t, row, sensor_x, sensor_y, totaldif, t)
      ir += check(sensor_x-t, sensor_y-t, row, sensor_x, sensor_y, totaldif, t)

  return ir


def check(sx, sy, row, x, y, td, t):   
  ir = []     
  if sy==row: ir.append((x,sy))
  if y==row: ir.append((sx, y))
  
  for c in range(td-t):
    f_y = y+c
    if f_y == row: ir.append((sx,f_y))
    f_y = y-c
    if f_y == row:ir.append((sx,f_y))

  return ir

def getsb(coords):  
  sb = []
  for coord in coords:
    coord = coord.split(' ')
    sensor = (int(coord[2][2:-1]), int(coord[3][2:-1]))
    beacon = (int(coord[8][2:-1]), int(coord[9][2:]))
    sb.append((sensor, beacon))
  return(sb)

main()