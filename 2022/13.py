from data.d13 import input

def main(input):
  sum = 0
  for i in range(150):
    ind = i*2
    left = input[ind]
    right = input[ind+1]

    false = checklr(left, right, False)
    if false: print(int(ind/2)+1, "- not right")
    else:
      print(int(ind/2)+1, "- right")
      sum+=i+1
  print(sum)

def checklr(left, right, nested):
  false = False
  lens = (len(left), len(right))
  if len(left) > len(right) and not nested: return True
  if len(left) == 0: return false
  
  if nested and len(right) == 0: return True

  for v in range(min(lens)):
    l = left[v]
    r = right[v]
    if type(l) == int and type(r) == int:
      if l > r: return True
    elif type(l) == list and type(r)== int: r = [r]
    elif type(l) == int and type(r) == list: l = [l]
    if type(l) == list and type(r) == list:
      false = checklr(l, r, True)
      
  return false
 
main(input)