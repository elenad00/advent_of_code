file = 'input.txt'
#file = 'test.txt'

def main():
  all_valves = []
  optimum_valves = []
  pres = []
  f = open(file,'r')
  valves = f.read().split('\n')
  
  for valve in valves:
    name, pressure, vs = cleansevalve(valve)
    if pressure>=20:
      optimum_valves.append(name)
    all_valves.append(name)
    if pressure not in pres: pres.append(pressure)
    all_valves.append((pressure, vs))

  movevalve(all_valves, optimum_valves, sorted(pres))
  

def movevalve(av, ov, p):
  rp = 0
  cv = 'AA'
  open = []
  visited = []
  v = round(len(p)/2)-1
  i = 0
  pv = ''
  for m in range(31):
    print(m, cv, pv)
    tp = 29-m
    cm = av[av.index(cv)+1]
    
    pres = cm[0]
    valves = cm[1]
    nv = False 
    if pres >= p[int(v)] and cv not in open:
      rp+=(tp*pres)
      print(rp)
      open.append(cv)
      i+=1
      if i>v and v!=0:v-=1

    else:
      for valve in valves:
        if valve not in open and valve not in visited and valve!=pv:
          if valve in ov:
            print('in ov')
            nv = valve
            break
          else:
            nv = valve
            break
      if not nv: 
        for valve in valves:
          if valve!=pv: 
            nv = valve
            break
          else: nv = pv
      
      pv = cv
      cv = nv
      if cv not in visited: visited.append(cv)

  
  print(rp)


def cleansevalve(valve):
  ts = []
  valve = valve.split(' ')
  tunnels = valve[9:]
  for tunnel in tunnels:
    ts.append(tunnel.strip(','))
  return valve[1], int(valve[4][5:-1]), ts

main()