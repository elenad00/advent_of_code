''' 
if flow rate = 0:
  valve = closed
presure release = flow rate * (totaltime-time)

move to connecting tunnels one at a time
'''

def main():
  all_valves = []
  open_valves = []
  visited = []
  released_pressure = 0
  current_valve = 'AA'
  last_value = ''
  time_premium = 30
  pressures = []
  optimum_spaces = []

  f = open('input.txt','r')
  valves = f.read().split('\n')
  for valve in valves:
    name, valve = cleansevalve(valve)
    all_valves.append(name)
    all_valves.append(valve)
    if valve[0] not in pressures:
      pressures.append(valve[0])
    if valve[0]>0:
      optimum_spaces.append(name)
  
  pressures = sorted(pressures)
  #exit(0)
  i = int(len(pressures)/2)
  c = 0
  for m in range(0,31):
    print(m, current_valve, last_value, released_pressure)
      
    time_premium = 29-m
    vi = all_valves.index(current_valve)
    valve = all_valves[vi+1]
    if valve[0] >= pressures[i] and current_valve not in open_valves:
      open_valves.append(current_valve)
      released_pressure += valve[0]*time_premium
      c+=1
      if c > i:
        i-=1
    else:
      tv = valve[1][0].replace(',','')
      if len(valve[1]) == 1:
        last_value = current_valve
        current_valve = tv
      elif len(valve[1]) == 2:
        tv1 = tv
        tv2 = (valve[1][1]).replace(',','')
        if tv1 != last_value and tv1 not in open_valves and tv1 not in visited:
          last_value = current_valve
          current_valve = tv1
        elif tv2 != last_value and tv2 not in open_valves and tv2 not in visited:
          last_value = current_valve
          current_valve = tv2
        else:
          if tv1!=last_value:
            last_value = current_valve
            current_valve = tv1
          else:
            last_value = current_valve
            current_valve = tv2 
      elif len(valve[1]) == 3:
        tv1 = tv
        tv2 = (valve[1][1]).replace(',','')
        tv3 = (valve[1][2]).replace(',','')
        if tv1 != last_value and tv1 not in open_valves and tv1 not in visited:
          last_value = current_valve
          current_valve = tv1
        elif tv2 != last_value and tv2 not in open_valves and tv2 not in visited:
          last_value = current_valve
          current_valve = tv2
        elif tv3 != last_value and tv3 not in open_valves and tv3 not in visited:
          last_value = current_valve
          current_valve = tv3
        else:
          last_value = current_valve
          current_valve = tv1
      elif len(valve[1]) == 4:
        tv1 = tv
        tv2 = (valve[1][1]).replace(',','')
        tv3 = (valve[1][2]).replace(',','')
        tv4 = valve[1][3]
        if tv1 != last_value and tv1 not in open_valves and tv1 not in visited:
          last_value = current_valve
          current_valve = tv1
        elif tv2 != last_value and tv2 not in open_valves and tv2 not in visited:
          last_value = current_valve
          current_valve = tv2
        elif tv3 != last_value and tv3 not in open_valves and tv3 not in visited:
          last_value = current_valve
          current_valve = tv3
        elif tv4 != last_value and tv4 not in open_valves and tv4 not in visited:
          last_value = current_valve
          current_valve = tv4
        else:
          last_value = current_valve
          current_valve = tv1
      elif len(valve[1]) == 5:
        tv1 = tv
        tv2 = (valve[1][1]).replace(',','')
        tv3 = (valve[1][2]).replace(',','')
        tv4 = valve[1][3].replace(',','')
        tv5 = valve[1][4].replace(',','')
        if tv1 != last_value and tv1 not in open_valves and tv1 not in visited:
          last_value = current_valve
          current_valve = tv1
        elif tv2 != last_value and tv2 not in open_valves and tv2 not in visited:
          last_value = current_valve
          current_valve = tv2
        elif tv3 != last_value and tv3 not in open_valves and tv3 not in visited:
          last_value = current_valve
          current_valve = tv3
        elif tv4 != last_value and tv4 not in open_valves and tv4 not in visited:
          last_value = current_valve
          current_valve = tv4
        elif tv5 != last_value and tv5 not in open_valves and tv5 not in visited:
          last_value = current_valve
          current_valve = tv5
        else:
          last_value = current_valve
          current_valve = tv1
      else:
        print("Not Caught")
        exit(0)
      visited.append(current_valve)

def cleansevalve(valve):
  valve = valve.split(' ')
  name = valve[1]
  fr = valve[4][5:-1]
  tunnels = valve[9:]
  return name, [int(fr), tunnels]

main()