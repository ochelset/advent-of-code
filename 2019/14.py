"""
--- Day 14: Space Stoichiometry ---
As you approach the rings of Saturn, your ship's low fuel indicator turns on.
There isn't any fuel here, but the rings have plenty of raw material.
Perhaps your ship's Inter-Stellar Refinery Union brand nanofactory can turn these raw materials into fuel.

You ask the nanofactory to produce a list of the reactions it can perform that are relevant to this process (your puzzle input).
Every reaction turns some quantities of specific input chemicals into some quantity of an output chemical.
Almost every chemical is produced by exactly one reaction; the only exception, ORE,
is the raw material input to the entire process and is not produced by a reaction.

You just need to know how much ORE you'll need to collect before you can produce one unit of FUEL.

Each reaction gives specific quantities for its inputs and output; reactions cannot be partially run,
so only whole integer multiples of these quantities can be used.
(It's okay to have leftover chemicals when you're done, though.) For example,
the reaction 1 A, 2 B, 3 C => 2 D means that exactly 2 units of chemical D can be produced by
consuming exactly 1 A, 2 B and 3 C. You can run the full reaction as many times as necessary;
for example, you could produce 10 D by consuming 5 A, 10 B, and 15 C.

Suppose your nanofactory produces the following list of reactions:

10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL
The first two reactions use only ORE as inputs; they indicate that you can produce as much of chemical A as you want (in increments of 10 units,
each 10 costing 10 ORE) and as much of chemical B as you want (each costing 1 ORE). To produce 1 FUEL, a total of 31 ORE is required: 1 ORE to produce 1 B,
then 30 more ORE to produce the 7 + 7 + 7 + 7 = 28 A (with 2 extra A wasted) required in the reactions to convert the B into C, C into D, D into E,
and finally E into FUEL. (30 A is produced because its reaction requires that it is created in increments of 10.)

Or, suppose you have the following list of reactions:

9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL
The above list of reactions requires 165 ORE to produce 1 FUEL:

Consume 45 ORE to produce 10 A.
Consume 64 ORE to produce 24 B.
Consume 56 ORE to produce 40 C.
Consume 6 A, 8 B to produce 2 AB.
Consume 15 B, 21 C to produce 3 BC.
Consume 16 C, 4 A to produce 4 CA.
Consume 2 AB, 3 BC, 4 CA to produce 1 FUEL.
Here are some larger examples:

13312 ORE for 1 FUEL:
157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT

180697 ORE for 1 FUEL:
2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF

2210736 ORE for 1 FUEL:
171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX

Given the list of reactions in your puzzle input, what is the minimum amount of ORE required to produce exactly 1 FUEL?
ANSWER: 278404

After collecting ORE for a while, you check your cargo hold: 1 trillion (1000000000000) units of ORE.

With that much ore, given the examples above:

The 13312 ORE-per-FUEL example could produce 82892753 FUEL.
The 180697 ORE-per-FUEL example could produce 5586022 FUEL.
The 2210736 ORE-per-FUEL example could produce 460664 FUEL.
Given 1 trillion ORE, what is the maximum amount of FUEL you can produce?
"""

class NanoFactory:

    ore = 0
    reactions = []

    def __init__(self, data):
        self.data = data.strip().split('\n')
        self.reactions = []
        self.generators = {}
        self.stock = {}
        self.fuel = 0
        self.ores = ORES
        self.needed = 0
        self.best = None
        self.analyze()

    def analyze(self):
        for line in self.data:
            requirements, result = line.split(' => ')

            reaction = Reaction()
            for part in requirements.split(','):
                amount, name = part.strip().split(' ')
                reaction.input(amount, Chemical(name))

            amount, name = result.split(' ')
            reaction.outputs(amount, Chemical(name))
            self.reactions.append(reaction)
            self.generators[name] = reaction

    def run(self):
        for reaction in self.reactions:
            print("RUN", reaction)
            if "FUEL" in self.stock and self.stock["FUEL"] > 0:
                #print("GOT FUEL! ORES NEEDED", self.needed)
                self.fuel += 1
                self.stock["FUEL"] = 0
                if self.best == None or self.needed < self.best:
                    self.best = self.needed
                #self.needed = 0
                #break
                #input()

            if False and reaction.output[1].name == "FUEL":
                print(80*"-")
                for inp in reaction.inputs:
                    print(inp[1].name, self.stock[inp[1].name] if inp[1].name in self.stock else 0)
                #input()

            if self.ores <= 0:
                break

            if not reaction.output[1].name in self.stock:
                self.stock[reaction.output[1].name] = 0

            #print(reaction, "HAVE", self.stock[reaction.output[1].name], reaction.output[1].name)

            for consumes in reaction.inputs[::-1]:
                #print("CONSUME", consumes)
                if not consumes[1].name in self.stock:
                    self.stock[consumes[1].name] = 0

                if consumes[1].name == "ORE":
                    self.stock["ORE"] += consumes[0]
                    self.needed += consumes[0]
                    self.ores -= consumes[0]
                    #print("+ORE", consumes[0], self.needed, self.ores)
                    #input()

                while self.stock[consumes[1].name] < consumes[0]:
                    if self.ores <= 0:
                        break
                    #print("==>")
                    self.generate(consumes[1].name)

                #print("CONSUME", consumes[0], consumes[1].name, "(have %d)" % self.stock[consumes[1].name])
                self.stock[consumes[1].name] -= consumes[0]

            self.stock[reaction.output[1].name] += reaction.output[0]

    def generate(self, name):
        if self.ores <= 0:
            print("X")
            return

        reaction = self.generators[name]
        #print("GENERATE", name, reaction)
        for consumes in reaction.inputs[::-1]:
            #print("KONSUMES", consumes)
            if self.ores < 0:
                break

            if not consumes[1].name in self.stock:
                self.stock[consumes[1].name] = 0

            while self.stock[consumes[1].name] < consumes[0]:
                if consumes[1].name == "ORE":
                    self.stock["ORE"] += consumes[0]
                    self.needed += consumes[0]
                    self.ores -= consumes[0]
                    #print("++ORE", consumes[0], self.needed, self.ores)
                    break
                else:
                    #print("-->")
                    self.generate(consumes[1].name)

            #print("CONSUME", consumes[0], consumes[1].name, "(have %d)" % self.stock[consumes[1].name])
            self.stock[consumes[1].name] -= consumes[0]
            #input()
        #print(">>", name, reaction.output[0])
        self.stock[name] += reaction.output[0]
        #print("<<")

        #print("<", self.stock)


class Reaction:

    def __init__(self):
        self.inputs = []
        self.output = (0, '')
        self.consumed = 0

    def __repr__(self):
        a = []
        for i in self.inputs:
            a.append("%d %s" % (i[0], i[1].name))
        return "<Reaction %s => %d %s>" % (', '.join(a), self.output[0], self.output[1].name)

    def input(self, amount, chemical):
        self.inputs.append((int(amount), chemical))

    def outputs(self, amount, chemical):
        self.output = (int(amount), chemical)


class Chemical:

    def __init__(self, name):
        self.name = name
        self.chain = None

    def __repr__(self):
        return "<Chemical %s>" % self.name

    def attach(self, chemical):
        self.chain = chemical

data = open("data/14.data").read()

datax = """
157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT
"""
datax = """
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX
"""

ORES = 1000000000000

prevOres = ORES
consumedSincePrev = 0

factory = NanoFactory(data)
factory.run()

""" 75120192
The 13312 ORE-per-FUEL example could produce 82892753 FUEL.
The 180697 ORE-per-FUEL example could produce 5586022 FUEL.
The 2210736 ORE-per-FUEL example could produce 460664 FUEL.
    278404                                    3591902
Given 1 trillion ORE, what is the maximum amount of FUEL you can produce?
"""

print("Part 1:", factory.best, "remaining:", factory.ores)

delta = 0
while factory.ores > 0:
    factory.run()

    #for item in factory.stock.items():
    #    print(item)

    for reaction in factory.reactions:
        if reaction.inputs[0][1].name == "ORE":
            print(reaction.inputs[0][0], reaction.inputs[0][1].name, ">", reaction.output[0], reaction.output[1].name, "(", factory.stock[reaction.output[1].name], ")")
    print(factory.fuel, "<", factory.needed, factory.ores)
    input()

    if factory.fuel % 1000 == 0 and False:
        if consumedSincePrev == 0:
            delta = prevOres - factory.ores
        else:
            delta = consumedSincePrev
        consumedSincePrev = prevOres - factory.ores
        prevOres = factory.ores
        delta = abs(delta - consumedSincePrev)
        print("remaining:", factory.ores, factory.fuel, "consumed", consumedSincePrev, delta)
        #input(":")

print("Part 2:", factory.best, "remaining:", factory.ores, factory.fuel)
# > 244418