# root yells 152
# human yells humn

def main(input):
  f=open(input)
  monkeys = f.read().split('\n')
  sum = ''
  dict_monkeys = {}
  for monkey in monkeys:
    monkey=monkey.split(': ')
    try: calc = int(monkey[1])
    except: calc = monkey[1].split(' ')
    if monkey[0] == 'root':
      sum = calc
    dict_monkeys[monkey[0]] = calc
  
  part_one(dict_monkeys, sum)

def part_two(dm, sum):
  sum = sum[0], sum[2]
  one = find_int(sum[0], dm)
  two = find_int(sum[1], dm)
  print(one, two)
  

def part_one(dict_monkeys, sum):
  one = find_int(sum[0], dict_monkeys)
  two = find_int(sum[2], dict_monkeys)
  if sum[1] == '-': s = one - two
  elif sum[1] == '+': s = one + two
  elif sum[1] == '/': s = one / two
  elif sum[1] == '*': s = one * two
  print(one, two, int(s))

def find_int(key, dict_monkeys):
  one = None
  two = None
  if key == 'x':
    return key
  found = dict_monkeys[key]
  if type(found)!=int:
    while one == None:
      one = find_int(found[0], dict_monkeys)  
    while two == None:
      two = find_int(found[2], dict_monkeys)
  else:
    return found

  if found[1] == '-': sum = one - two
  elif found[1] == '+': sum = one + two
  elif found[1] == '/': sum = one / two
  elif found[1] == '*': sum = one * two
  return sum
 
# one - 158661812617812 #

main("input.txt")
#main('test.txt')