import re

test_data_pt1 = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
test_answers_pt1 = [12, 38, 15, 77]

test_data_pt2 = ['two1nine', 'eightwothree','abcone2threexyz',
                 'xtwone3four','4nineeightseven2','zoneight234',
                 '7pqrstsixteen']
test_answers_pt2 = [29, 83, 13, 24, 42, 84, 76]

numbers_re = r'(:[0-9]|one|two|three|four|five|six|seven|eight|nine)'
numbers_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
                'seven', 'eight', 'nine']



def extract_numbers(code):
  numbers = re.findall(numbers_re, code)

  if numbers[0].isnumeric():
    first_number =  int(numbers[0])
  else:
    first_number =  numbers_list.index(numbers[0])

  if numbers[-1].isnumeric():
    last_number =  int(numbers[-1])
  else:
    last_number =  numbers_list.index(numbers[-1])

  return int(first_number + last_number)
      
with open('day1-1.txt','r') as f:
  day_one = []
  [day_one.append(line) for line in f.readlines()]

