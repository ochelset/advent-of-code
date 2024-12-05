"""
--- Day 19: Medicine for Rudolph ---
Rudolph the Red-Nosed Reindeer is sick! His nose isn't shining very brightly, and he needs medicine.

Red-Nosed Reindeer biology isn't similar to regular reindeer biology; Rudolph is going to need custom-made medicine.
Unfortunately, Red-Nosed Reindeer chemistry isn't similar to regular reindeer chemistry, either.

The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission plant, capable of constructing any
Red-Nosed Reindeer molecule you need. It works by starting with some input molecule and then doing a series of
replacements, one per step, until it has the right molecule.

However, the machine has to be calibrated before it can be used. Calibration involves determining the number of
molecules that can be generated in one step from a given starting point.

For example, imagine a simpler machine that supports only the following replacements:

H => HO
H => OH
O => HH
Given the replacements above and starting with HOH, the following molecules could be generated:

HOOH (via H => HO on the first H).
HOHO (via H => HO on the second H).
OHOH (via H => OH on the first H).
HOOH (via H => OH on the second H).
HHHH (via O => HH).
So, in the example above, there are 4 distinct molecules (not five, because HOOH appears twice) after one replacement
from HOH. Santa's favorite molecule, HOHOHO, can become 7 distinct molecules (over nine replacements: six from H,
and three from O).

The machine replaces without regard for the surrounding characters. For example, given the string H2O, the
transition H => OO would result in OO2O.

Your puzzle input describes all of the possible replacements and, at the bottom, the medicine molecule for which you
need to calibrate the machine. How many distinct molecules can be created after all the different ways you can do one
replacement on the medicine molecule?

--- Part Two ---
Now that the machine is calibrated, you're ready to begin molecule fabrication.

Molecule fabrication always begins with just a single electron, e, and applying replacements one at a time, just like
the ones during calibration.

For example, suppose you have the following replacements:

e => H
e => O
H => HO
H => OH
O => HH
If you'd like to make HOH, you start with e, and then make the following replacements:

e => O to get O
O => HH to get HH
H => OH (on the second H) to get HOH
So, you could make HOH after 3 steps. Santa's favorite molecule, HOHOHO, can be made in 6 steps.

How long will it take to make the medicine? Given the available replacements and the medicine molecule in your puzzle
input, what is the fewest number of steps to go from e to the medicine molecule?
"""

data, molecule = open("input.data").read().strip().split("\n\n")

if False:
    data = """
    e => H
    e => O
    H => HO
    H => OH
    O => HH
    """.strip()
    molecule = "HOHOHO"

molecules = set()
for replacement in data.splitlines():
    source, target = replacement.split(" => ")
    indices = [i for i in range(len(molecule)) if molecule[i:i + len(source)] == source]
    for index in indices:
        new_molecule = molecule[:index] + target + molecule[index + len(source):]
        molecules.add(new_molecule)

print("Part 1:", len(molecules))

#
#

steps = 0
replacements = {}
for line in data.splitlines():
    source, target = line.split(" => ")
    replacements[target] = source.strip()

print(replacements)

i = 1
while True:
    steps += 1
    i = len(molecule) - 1
    replacement = None
    print()
    print("Step %s:" % steps)
    # print("> CURRENT", molecule)
    while True:
        new_replacement = molecule[i:]
        if new_replacement in replacements:
            replacement = new_replacement
            # print("new repl?", replacement)
            # input()

        i -= 1
        if i < 0:
            print("<<< X2", replacement)
            break
    print("*", replacement)
    input()

    print("@", molecule, "-", replacement)
    molecule = molecule[:-len(replacement)] + replacements[replacement]
    print("=", molecule)
    if len(molecule) > 1 and molecule.endswith("e"):
        molecule = molecule[:-1]
        continue

    if molecule == "e":
        print("Part 2:", steps)
        break
    # print(">", i + 1, replacement, "<=", replacements[replacement], ">>", molecule)
    # input()
