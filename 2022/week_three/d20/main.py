import numpy as np

def main(input):
  pos = 0
  f = open(input, 'r')
  sequence = f.read().split('\n')
  length = len(sequence)
  while pos < length:
    pos, sequence = move_numbers(sequence, pos, length)

  start = sequence.index(0)
  f = (start+(1000%length))%length
  s = (start+(2000%length))%length
  t = (start+(3000%length))%length
  
  print(sequence[f],sequence[s],sequence[t])
  print(sequence[f]+sequence[s]+sequence[t])
 
 #sum = sequence[first]+sequence[second]+sequence[third]
  #print(sum)
  # 16148 - too high
  # 6919 - incorrect
  # 5886 - incorrect
  # 4143 - incorrect
  # 3303 - incorrect
  # 2034 - too low
  # -10154 - too low

def move_numbers(sequence, pos, length):
  try:
    encrypted = sequence[pos]
  except:
    return pos, sequence
  if type(encrypted)==int: pos, sequence = move_numbers(sequence, pos+1, length)
  else:
    encrypted = int(encrypted)
    sequence.remove(str(encrypted))
    moveto = encrypted+pos
    if moveto<0:
      moveto = (length)+(moveto%-length)-1
    if moveto > length:  
      moveto = moveto%length+1
    sequence.insert(moveto, encrypted)
  return pos, sequence

#main('test.txt')
main('input.txt')