import re


sample_data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

with open('day4.txt', 'r') as f:
  live_data = f.read()

scores = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
score = 0

data = re.split(r'\n',live_data)

# parse the data

for card in data:
  card_parsed = re.split(r'[:\|]', card)

  ## card number
  
  
  ## numbers
  try:
    card_numbers = re.findall('\d+', card_parsed[1])
  except IndexError:
    continue
  
  ## winners
  card_winners = re.findall('\d+', card_parsed[2])
  
  # calculate the score
  card_score = 1
  index = 0

  for number in card_numbers:
    if number in card_winners:
      index += 1

  score += scores[index]

print(score)

  
