import re

test_data_pt1 = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
test_answers_pt1 = [12, 38, 15, 77]

test_data_pt2 = ['two1nine', 'eightwothree','abcone2threexyz',
                 'xtwone3four','4nineeightseven2','zoneight234',
                 '7pqrstsixteen']
test_answers_pt2 = [29, 83, 13, 24, 42, 14, 76]


numbers_re = r'(\d|zero|one|two|three|four|five|six|seven|eight|nine)'
numbers_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
                'seven', 'eight', 'nine']


def prepass_codes(code):
  code = re.sub(r'one','o1e', code)
  code = re.sub(r'two','t2o', code)
  code = re.sub(r'three','t3e', code)
  code = re.sub(r'four','f4r', code)
  code = re.sub(r'five','f5e', code)
  code = re.sub(r'six','s6x', code)
  code = re.sub(r'seven','s7n', code)
  code = re.sub(r'eight','e8t', code)
  code = re.sub(r'nine','n9e', code)
  code = re.sub(r'zero','z0o', code)

  return code


def extract_numbers(code):
  numbers = re.findall(r'\d', code)

  return int(numbers[0] + numbers[-1])
      
with open('day1-1.txt','r') as f:
  day_one = []
  [day_one.append(line) for line in f.readlines()]

