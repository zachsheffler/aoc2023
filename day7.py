from collections import Counter

sample_data = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''


cards = list()
bids = list()
hands = dict()

for i, line in enumerate(sample_data.split('\n')):
  hands[i] = line.split()

ranked_cards = dict()

# 5 of a kind
s5 = []
# 4 of a kind
s4 = []
# full house
s32 = []
# 3 of a kind
s3 = []
# two pair
s22 = []
# pair
s2 = []
# high card
s1 = []
  
# place rank
def calc_rank(cards):
  '''Takes string and puts it in a list in order to rank'''
  count = Counter(cards)

  most_common = count.most_common(5)

  
  if most_common[0][1] == 5: # five of a kind
    s5.append(cards)
  elif most_common[0][1] == 4: # four of a kind
    s4.append(cards)
  elif most_common[0][1] == 3 and most_common[1][1] == 2:
    s32.append(cards)
  elif most_common[0][1] == 3:
    s3.append(cards)
  elif most_common[0][1] == 2 and most_common[1][1] == 2:
    s22.append(cards)
  elif most_common[0][1] == 2:
    s2.append(cards)
  else: # high card
    s1.append(cards)

    return dict([('s5',s5),('s4',s4),('s32',s32),('s3',s3),('s22',s22),('s2',s2),('s1',s1)])


# calc bid * rank

