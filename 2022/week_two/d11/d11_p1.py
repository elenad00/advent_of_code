def main():
  f = open("d11_test.txt",'r')
  f = open("d11_input.txt",'r')
  monkeys = f.read()
  monkeys = monkeys.split('\n-\n')

  cycles = 0

  mval = 1

  orderly_monkeys = []

  for monkey in monkeys:
    monk = getmonkey(monkey)
    orderly_monkeys.append(monk)
    mval=mval*monk[3]
  
  print(mval)

  while cycles < 10000:
    for monkey in orderly_monkeys:
      s_range = len(monkey[0])
      for s in range(s_range):
        monkey[6]+=1
        
        item = monkey[0][0]
        mod_by = monkey[3]

        if monkey[2] == False:
          value = item
        else:
          value = monkey[2]

        if monkey[1] == '*':
          item = item * value
        else:
          item = item + value

        modded = int(round(item%mod_by, 0))

        item = item%mval

        if modded == 0:
          orderly_monkeys[monkey[4]][0].append(item)
        else:
          orderly_monkeys[monkey[5]][0].append(item)
        monkey[0].remove(monkey[0][0])
    cycles += 1
    if cycles%1000 == 0:
      print(cycles)
      for m in orderly_monkeys:
        print('  '+str(m[6]))
  
  ms = []

  for m in orderly_monkeys:
    ms.append(m[6])
  ms = sorted(ms)
  print(ms)
  print(ms[-1]*ms[-2])

def getmonkey(monkey):
  monkey = monkey.split('\n')
  
  items = (monkey[1].split(':'))[1].split(', ')
  for i in range(len(items)):
    items[i]=int(items[i])

  operation = monkey[2].split(' ')
  operand = operation[-2]

  value = operation[-1]
  if value == 'old':
    value = False
  else:
    value = int(value)

  mod_by = int((monkey[3].split(' '))[-1])

  true_monkey = int((monkey[4].split(' '))[-1])
  false_monkey = int((monkey[5].split(' '))[-1])
  #print(monkeynum, (items), operand, value, mod_by, true_monkey, false_monkey)

  monkeh = [items, operand, value, mod_by, true_monkey, false_monkey, 0]
  return monkeh

main()

'''
monkey[0] = items
monkey[1] = operation
monkey[2] = value
monkey[3] = mod value
monkey[4] = if true monkey
monkey[5] = if false monkey
monkey[6] = inspected count
'''

# worry = 2,713,310,158

# 101436