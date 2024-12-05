from collections import Counter

data = open("input.data").read().strip().split("\n")

test_data = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
7777J 5
888J8 5
J9999 5
TJTTT 5
J8JJJ 5
22Q22 5
Q3333 5
5Q555 5
6666Q 5
7Q777 5
888Q8 5
5QQQQ 5
36725 0
64382 0
38427 0
78452 0
94352 0
92735 0
28693 0
25T37 0
T6427 0
T3682 0
T2769 0
4J362 0
5642J 0
2375J 0
73J26 0
325J8 0
J4852 0
2856J 0
73J28 0
""".strip().split("\n")[:5]

class Hand:
    cards = []
    values = []
    type = 0
    rank = 0
    bid = 0
    hand: Counter
    ordered = ''
    org = ''

    def __init__(self, hand, bid) -> None:
        self.cards = [x for x in hand]
        self.values = []
        self.bid = int(bid)
        self.type = 0
        self.ordered = ''
        self.org = ''

        self.__analyze__()

    def __repr__(self) -> str:
        return ''.join(self.cards)

    def __analyze__(self):
        for card in self.cards:
            if card == 'A':
                self.values.append(14)
            elif card == 'K':
                self.values.append(13)
            elif card == 'Q':
                self.values.append(12)
            elif card == 'J':
                self.values.append(11)
            elif card == 'T':
                self.values.append(10)
            else:
                self.values.append(int(card))

        self.values = sorted(self.values)[::-1]
        self.hand = Counter(self.values)

        hand = sorted(self.hand.values())
        #print("H", hand, )
        #for k in sorted(self.hand.items(), key=lambda x: -x[1]):
        #    k = k[0]
        #    for i in range(self.hand[k]):
        for k in self.cards:
            #print(k, "->", chr(k + 96))
            #print(k, ord(chr(k + 96)), chr(k + 96))
            if k == 'A':
                self.ordered += 'P'
            elif k == 'K':
                self.ordered += 'O'
            elif k == 'Q':
                self.ordered += 'N'
            elif k == 'J':
                self.ordered += 'M'
            elif k == 'T':
                self.ordered += 'L'
            else:
                self.ordered += k
            #self.ordered += chr(ord(k) + 96)
            # if k < 10:
            #     self.org += str(k)
            # if k == 10:
            #     self.org += 'T'
            # if k == 11:
            #     self.org += 'J'
            # if k == 12:
            #     self.org += 'Q'
            # if k == 13:
            #     self.org += 'K'
            # if k == 14:
            #     self.org += 'A'
        #print(self.cards, self.ordered)
        #input()

        if hand == [5]:
            self.type = 6 # Five of a kind
        elif hand == [1, 4]:
            self.type = 5 # Four of a kind
        elif hand == [2, 3]:
            self.type = 4 # Full house
        elif hand == [1,1,3]:
            self.type = 3 # Three of a kine
        elif hand == [1,2,2]:
            self.type = 2 # Two pairs
        elif hand == [1,1,1,2]:
            self.type = 1 # One pair

#
#

def sort_hands(hands: [Hand]) -> [Hand]:
    #return sorted(hands, key=lambda x: (x.type, x.values[0], x.values[1], x.values[2], x.values[3], x.values[4]))
    return sorted(hands, key=lambda x: (x.type, x.ordered))

##
##

xdata = test_data

hands = []
for line in data:
    hand, bid = line.split(" ")
    hands.append(Hand(hand, bid))

hands = sort_hands(hands)

i = 1
result_1 = 0
for hand in hands:
    hand.rank = i
    result_1 += hand.rank * hand.bid
    print(hand, '|', hand.org, hand.type, hand.rank, hand.bid, "  \t[%s]" % hand.ordered)
    i += 1

print("Part 1:", result_1, 248453531 - result_1)

#   248997354
#   248483701
# ? 248630936

# 1 248453531
# 2 248781813