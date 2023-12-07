import re

opener = r'Game \d+\:'
split = r'[:;]'
cube_parse = r'(?P<number>\d+) (?P<color>\w+)'

test_data = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
             'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
             'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
             'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
             'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']

with open('day2.txt', 'r') as f:
  live_data = list()
  for line in f.readlines():
    live_data.append(line)

games = dict()


# Extract the games
for game in live_data:
  draws = list()

  split_line = re.split(split, game)

  # extract the game number
  game_number = re.findall(r'\d+',split_line[0])[0]
  games[game_number] = list()
  
  # extract contents of each draw
  for draw in split_line[1:]:
    
    split_draw = re.split(r',',draw) # split up into components
 
    draw_dict = {'blue':0, 'red':0, 'green':0}
      
    for color_draw in split_draw:
      
      parse = re.search(cube_parse, color_draw) 
      num = parse.group('number')
      color = parse.group('color')

      draw_dict[color] = int(num)

    draws.append(draw_dict)
  
  games[game_number] = draws



def find_minimum_set(game):
  bag = {'blue': 0, 'red': 0, 'green': 0}
  
  for draw in game:
    for color in draw:
      if draw[color] > bag[color]:
        bag[color] = draw[color]

  return bag


def calculate_power(min_set):
  power = 1
  for color in min_set.values():
    power *= color

  return power

all_min_sets = [find_minimum_set(games[game]) for game in games.keys()]

total_power = sum([calculate_power(min_set) for min_set in all_min_sets])
