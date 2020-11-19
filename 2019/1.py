# December 1st

import math
from functools import reduce

modules = [
123457,
98952,
65241,
62222,
144922,
111868,
71513,
74124,
140122,
133046,
65283,
107447,
144864,
136738,
118458,
91049,
71486,
100320,
143765,
88677,
62034,
139946,
81017,
128668,
126450,
56551,
136839,
64516,
91821,
139909,
52907,
78846,
102008,
58518,
128627,
71256,
133546,
90986,
50808,
139055,
88769,
94491,
128902,
55976,
103658,
123605,
113468,
128398,
61725,
100388,
96763,
101378,
139952,
138298,
87171,
51840,
64828,
58250,
88273,
136781,
120097,
127291,
143752,
117291,
100023,
147239,
71296,
100907,
127612,
122424,
62942,
95445,
74040,
118994,
81810,
146408,
98939,
71359,
112120,
100630,
139576,
98998,
92481,
53510,
76343,
125428,
73447,
62472,
91370,
73506,
126539,
50739,
73133,
81906,
100856,
52758,
142303,
107605,
77797,
124355]

def calculateFuel(mass) -> int:
	return math.floor(mass / 3.0) - 2

def calculateTotalFuel(mass) -> int:
	total = 0
	fuel = mass
	while True:
		fuel = calculateFuel(fuel)
		if fuel < 0:
			break
		total += fuel
	return total

fuel = reduce((lambda x, y: x + y), list(map(calculateTotalFuel, modules)))
print(fuel)
