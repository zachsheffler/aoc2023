import re

test_data = '''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''

with open('day8.txt', 'r') as f:
  live_data = f.read()

seq, edges = live_data.split('\n\n')

regex = r'(?P<loc>[A-Z]{3}) = \((?P<lt>[A-Z]{3})\, (?P<rt>[A-Z]{3})\)\n' 

mapping = {loc: {'left': lt, 'right': rt} for (loc, lt, rt) in re.findall(regex, edges)}


def move(location, move):
  if move == 'R':
    return(location['right'])
  if move == 'L':
    return(location['left'])


def part1(mapping, seq):
  counter = 0

  location = 'AAA'

  while 1:
    for direction in seq:
      counter += 1
      location = move(mapping[location], direction)
      if location == 'ZZZ':
        return counter
        break


def part2(mapping, seq):
  from icecream import ic
  counter = 0

  locations = list()
  
  for i in mapping.keys():
    if(i[-1] == 'A'):
      locations.append(i)
      
  while True:
    for direction in seq:
      counter += 1
      
      locations = [move(mapping[location], direction) for location in locations]
      
      if sum([location[-1] == 'Z' for location in locations]) == len(locations):
        return counter
        break
  

part2(mapping, seq)
    
