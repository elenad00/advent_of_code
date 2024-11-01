'''
we have one ore collecting robot
one minute to collect resource
one minute to build a robot 
  + consumes resources

in 24 minutes, which blueprint opens
  the most geodes?

quality level = blueprint id * opened geodes
answer = sum of all quality levels

'''

def main(file):
  f = open(file, 'r')
  blueprints = f.read().split('\n')
  blueprints = strip_blueprints(blueprints)
  output = 0
  for b in range(len(blueprints)):
    geodes = run_blueprint(blueprints[b])
    output+=geodes*(b+1)
  print(output)

def strip_blueprints(blueprints):
  simplified = []
  for blueprint in blueprints:
    bp = blueprint.split('. ')
    ore = int(bp[0].split(' ')[-2])
    clay = int(bp[1].split(' ')[-2])
    obsidian = (int(bp[2].split(' ')[-5]), int(bp[2].split(' ')[-2]))
    geode = (int(bp[3].split(' ')[-5]), int(bp[3].split(' ')[-2]))
    new_bp = (ore, clay, obsidian, geode)
    simplified.append(new_bp)
  return simplified

def run_blueprint(b):
  
  ore, clay, obsidian, geodes = 0,0,0,0
  ore_robots = 1
  clay_robots, obsidian_robots, geode_robots = 0,0,0
  for i in range(1,25):
    o,c,ob,g = 0,0,0,0
    # build geode robot
    if ore>=b[3][0] and obsidian>=b[3][1]:
      geode_robots+=1
      ore-=b[3][0]
      obsidian-=b[3][1]
      g=1

    # build obsidian robot
    #elif ore>=b[2][0] and clay>=b[2][1] and obsidian_robots<2:
    elif ore>=b[2][0] and clay>=b[2][1] and obsidian_robots<(b[3][1]/4):
      obsidian_robots+=1
      ore-=b[2][0]
      clay-=b[2][1]
      ob=1
    
    # build clay robot
    #elif ore>=b[1] and clay_robots<3+obsidian_robots<5:
    elif ore>=b[1] and clay_robots<3+obsidian_robots<(b[2][1]/4):
      clay_robots+=1
      ore-=b[1]
      c=1
    
    # elif ore>=b[0] and ore_robots<2:
    #   ore_robots+=1
    #   ore-=b[1]
    #   o=1
    
    # collect resources
    print("Minute",i)
    ore += ore_robots-o
    clay += clay_robots-c
    obsidian += obsidian_robots-ob
    geodes += geode_robots-g

    print(ore_robots, clay_robots, obsidian_robots, geode_robots)
    print(ore, clay, obsidian, geodes)
  
  return(geodes)


main("test.txt")