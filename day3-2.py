import re
from math import prod
from icecream import ic

sample = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

with open('day3.txt','r') as f:
  live = f.read()

#split_lines = re.split('\n',live)
split_lines = re.split('\n', live) #test_1)

symbols = r'\*'

line_num = 0
part_num = 0
parts = list()

max_lines = len(split_lines)
max_width = len(split_lines[0])

for line_num in range(len(split_lines)):

  line = line_num + 1
  # find stars
  parts.append([])
  stars = re.finditer(r'[*]', split_lines[line])

  # define boundaries
  ic(line)
  # ic([star.span() for star in stars])
  for star in stars:
    # get all characters in a box around the number
    span = star.span()
    
    numbers = list()
    
    bounds = {'up': line - 1,
              'down': line + 1,
              'left': span[0] - 1,
              'right': span[0] + 1}
  
    ic(span)
    ic(bounds)
    # find numbers which touch boundaries

    for row in range(bounds['up'], bounds['down'] + 1):
      for number in re.finditer(r'\d+',split_lines[row]):
        if bounds['left'] <= number.span()[1]-1 and bounds['right'] >= number.span()[0]:
          numbers.append(number.group())

    ic(numbers)    
    if len(numbers) == 2:
      gear_ratio = prod([int(number) for number in numbers])
      parts.append(gear_ratio)
      part_num += gear_ratio
      ic( gear_ratio)
      
    elif len(numbers) < 2:
      continue
    else:
      ic(numbers)
      



with open('day3-out.txt','w') as f:
  
  for i in range(len(parts)):
    #f.write("{} | {}\n".format(split_lines[i], parts[i]))
    pass

  

  
ic(part_num)


