# human yells 301

def main(input):
  f=open(input)
  monkeys = f.read().split('\n')
  same = ''
  dm = {}
  for monkey in monkeys:
    monkey=monkey.split(': ')
    try: calc = int(monkey[1])
    except: calc = monkey[1].split(' ')
    if monkey[0] == 'humn':
      calc = 3352886133834
    dm[monkey[0]] = calc

  i=0
  while i<37:
    for m in dm:
      cv = dm[m]
      if 'x' == cv:
       continue
      elif type(cv) != int:
        if type(cv[0]) != int and type(dm[cv[0]]) == int: cv[0] = dm[cv[0]]
        if type(cv[2]) != int and type(dm[cv[2]]) == int: cv[2] = dm[cv[2]]
        if type(cv[0]) == int and type(cv[2]) == int:
          if cv[1] == '-': sum = cv[0] - cv[2]
          elif cv[1] == '+': sum = cv[0] + cv[2]
          elif cv[1] == '/': sum = cv[0] / cv[2]
          elif cv[1] == '*': sum = cv[0] * cv[2]
          if m=='root':
            print(cv[0], cv[2])
            if cv[2] == cv[0]:
              print("SAME!")
          dm[m] = int(sum)
    i+=1

#main('test.txt')
main('input.txt')

# 3352886133834 too high
# 3352886133833
# 3352886133832 incorrect
# 
# 3352886133830 too low