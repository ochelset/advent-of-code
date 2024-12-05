import sys
import re
from collections import defaultdict, Counter
D = open(sys.argv[1]).read().strip()
L = D.split('\n')

def strength(hand, part2):
  orig = hand
  hand = hand.replace('T',chr(ord('9')+1))
  hand = hand.replace('J',chr(ord('2')-1) if part2 else chr(ord('9')+2))
  hand = hand.replace('Q',chr(ord('9')+3))
  hand = hand.replace('K',chr(ord('9')+4))
  hand = hand.replace('A',chr(ord('9')+5))

  C = Counter(hand)
  if part2:
    target = list(C.keys())[0]
    for k in C:
      if k!='1':
        if C[k] > C[target] or target=='1':
          target = k
    assert target != '1' or list(C.keys()) == ['1']
    if '1' in C and target != '1':
      C[target] += C['1']
      del C['1']
    assert '1' not in C or list(C.keys()) == ['1'], f'{C} {hand}'

  if sorted(C.values()) == [5]:
    return (6, hand, orig)
  elif sorted(C.values()) == [1,4]:
    return (5, hand, orig)
  elif sorted(C.values()) == [2,3]:
    return (4, hand, orig)
  elif sorted(C.values()) == [1,1,3]:
    return (3, hand, orig)
  elif sorted(C.values()) == [1,2,2]:
    return (2, hand, orig)
  elif sorted(C.values()) == [1,1,1,2]:
    return (1, hand, orig)
  elif sorted(C.values()) == [1,1,1,1,1]:
    return (0, hand, orig)
  else:
    assert False, f'{C} {hand} {sorted(C.values())}'

for part2 in [False]: #, True]:
  H = []
  for line in L:
    hand,bid = line.split()
    H.append((hand,bid))
  H = sorted(H, key=lambda hb:strength(hb[0], part2))
  for h in H:
    print(h[0])
  ans = 0
  for i,(h,b) in enumerate(H):
    #print(i,h,b)
    ans += (i+1)*int(b)
  print(ans)
