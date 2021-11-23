"""
--- Day 10: Elves Look, Elves Say ---
Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud the previous sequence and using that reading as the next sequence. For example, 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step, take the previous value, and replace each run of digits (like 111) with the number of digits (3) followed by the digit itself (1).

For example:

1 becomes 11 (1 copy of digit 1).
11 becomes 21 (2 copies of digit 1).
21 becomes 1211 (one 2 followed by one 1).
1211 becomes 111221 (one 1, one 2, and two 1s).
111221 becomes 312211 (three 1s, two 2s, and one 1).
Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?

Your puzzle input is 1321131112.
"""

def look_and_say(input: str) -> str:
  output = ""
  counter = 0
  letter = None

  for next_letter in input:
    if letter and next_letter != letter:
      output += str(counter) + letter
      counter = 0

    counter += 1
    letter = next_letter

  return output + str(counter) + letter

x = "1321131112"
for i in range(40):
  x = look_and_say(x)

print("Part 1:", len(x))

for i in range(10):
  x = look_and_say(x)

print("Part 2:", len(x))


