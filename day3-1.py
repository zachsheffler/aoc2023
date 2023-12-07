import re
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

symbols = r'[\!\@\#\$\%\^\&\*\(\)_\-\=\+\\\/]'

line_num = 0
part_num = 0
parts = list()

max_lines = len(split_lines)
max_width = len(split_lines[0])

for line in range(len(split_lines)):
  parts.append([])
  numbers = re.finditer('\d+', split_lines[line])


  for number in numbers:
    # get all characters in a box around the number
    span = number.span()
    value = number.group()
    
    bounds = {'up': max(line - 1, 0),
              'down': min(line + 1, max_lines),
              'left': max(span[0] - 1, 0),
              'right': min(span[0] + len(value) + 1, max_width)} # janky

    for row in range(bounds['up'], min(bounds['down'] + 1, max_lines)):
      if re.findall(symbols,split_lines[row][bounds['left']:bounds['right']]):
        part_num += int(value)
        parts[line].append(int(value))
        
        break

with open('day3-out.txt','w') as f:
  
  for i in range(len(parts)):
    f.write("{} | {}\n".format(split_lines[i], parts[i]))


def get_pos(number, line):
  pass
  

  
ic(part_num)


