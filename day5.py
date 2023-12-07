import re
from icecream import ic
import numpy as np

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

mapping_list = [group.split('\n') for group in txt.split('\n\n')]

seed_list = re.findall(r'\d+', mapping_list[0][0])
seeds = [int(seed) for seed in seed_list]

def remap(map_list):
  mapper = list(range(1000000000))

  for line in map_list:
    maps = line.split()

    for n in range(int(maps[2])):
      mapper[int(maps[1]) + n] = int(maps[0]) + n

  return mapper


seed_soil = remap(mapping_list[1][1:])
soil_fert = remap(mapping_list[2][1:])
fert_water = remap(mapping_list[3][1:])
water_light = remap(mapping_list[4][1:])
light_temp = remap(mapping_list[5][1:])
temp_humi = remap(mapping_list[6][1:])
humi_loc = remap(mapping_list[7][1:])

locs = list()

for x in seeds:
  soil = seed_soil(x)
  fert = ic(soil_fert(soil))
  water = fert_water(fert)
  light = water_light(water)
  temp = light_temp(light)
  humi = temp_humi(temp)
  loc = humi_loc(humi)
  ic(loc)

print(min(locs))
