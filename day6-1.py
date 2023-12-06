import re
from math import prod

sample = """Time:      7  15   30
Distance:  9  40  200"""

live = """Time:        60     80     86     76
Distance:   601   1163   1559   1300"""

lines = re.split(r'\n', live)

race = {}
race['time'] = [int(t) for t in re.findall('\d+', lines[0])]
race['distance'] = [int(d) for d in re.findall('\d+', lines[1])]
race['solutions'] = []

for heat in range(len(race['time'])):
  race['solutions'].append(0)
  for t in range(race['time'][heat]):
    if (race['time'][heat] - t) * t > race['distance'][heat]:
      race['solutions'][heat] += 1
                 
part1_solution = prod(race['solutions'])
print("Part 1: {}".format(part1_solution))


part2_race = int(''.join(re.findall('\d+', lines[0])))
part2_distance = int(''.join(re.findall('\d+', lines[1])))

part2_solution = 0

for t in range(part2_race):
  if (part2_race - t) * t > part2_distance:
    part2_solution += 1

print("Part 2: {}".format(part2_solution))

