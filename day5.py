import re
from itertools import chain

txt = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

with open('day5.txt','r') as f:
  txt = f.read()


def lookup(value, mapping):
  _, *ranges = mapping
  for r in ranges:
    dest, src, n = map(int, r.split())
    if src <= value < src + n:
      return (value - src) + dest
  return value

seeds, *maps = [group.split('\n') for group in txt.split('\n\n')]

seed_list = re.findall(r'\d+', seeds[0])
seed_list_pt2 = re.findall(r'\d+ \d+', seeds[0])

seeds = [int(seed) for seed in seed_list]
seeds_pt2 = [seed.split() for seed in seed_list_pt2]

all_seeds_pt2 = list()
for group in [list(range(int(seed[0]),int(seed[0]) + int(seed[1]))) for seed in seeds_pt2]:
  all_seeds_pt2.extend(group)


## Part 1

soil = [lookup(s, maps[0]) for index, s in enumerate(seeds)]
fert = [lookup(s, maps[1]) for index, s in enumerate(soil)]
water = [lookup(s, maps[2]) for index, s in enumerate(fert)]
light = [lookup(s, maps[3]) for index, s in enumerate(water)]
temp = [lookup(s, maps[4]) for index, s in enumerate(light)]
humi = [lookup(s, maps[5]) for index, s in enumerate(temp)]
loc = [lookup(s, maps[6]) for index, s in enumerate(humi)]
    
print(f"Part 1: {min(loc)}")

## Part 2


soil = [lookup(s, maps[0]) for index, s in enumerate(all_seeds_pt2)]
fert = [lookup(s, maps[1]) for index, s in enumerate(soil)]
water = [lookup(s, maps[2]) for index, s in enumerate(fert)]
light = [lookup(s, maps[3]) for index, s in enumerate(water)]
temp = [lookup(s, maps[4]) for index, s in enumerate(light)]
humi = [lookup(s, maps[5]) for index, s in enumerate(temp)]
loc = [lookup(s, maps[6]) for index, s in enumerate(humi)]
    
print(f"Part 2: {min(loc)}")

