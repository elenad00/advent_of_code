f = open('data/d7.txt', 'r')
commands = f.read().split('\n')

dirs = []
checkeddirs = []
checked = False
dir_dex = -1
dir_sum = 0

for command in commands:
  command = command.split(' ')
  if command[0] == '$':
    cmd = command[1]
    try:
      dir = command[2]
    except:
      continue
    if cmd == 'cd' and dir!='..':
      if dir_dex>=0:
        dirs[dir_dex].append(dir_sum)
        dir_sum = 0  
        checked = False
      
      if dir not in checkeddirs:
        dirs.append([dir])
        dir_dex = len(dirs)-1
        checkeddirs.append(dir)
      else:
        checked = True

  elif not checked:
    filesize = command[0]
    if filesize == 'dir':
      filesize = command[1]
      dirs[dir_dex].append(filesize)
    else:
      dir_sum+=int(filesize)

if dir_sum > 0:
  dirs[dir_dex].append(dir_sum)

# 95437

dirs = sorted(dirs, key=len)

condir = []

for dir in dirs:
  d_length = len(dir)
  if d_length>2:
    for i in range(d_length-2):
      for j in range(len(dirs)):
        if dirs[j][0] == dir[i+1]:
          index = j 
      dir[-1]+=int(dirs[index][-1])
  condir.append([dir[0], dir[-1]])

condir = sorted(condir, key=lambda x:x[1])

over100k = 0
for dir in condir:
  if dir[1]<100000:
    over100k+=dir[1]

print(over100k)

# 1792222 