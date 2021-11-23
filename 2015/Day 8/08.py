'''
--- Day 8: Matchsticks ---
Space on the sleigh is limited this year, and so Santa will be bringing his list as a digital copy. He needs to know how
much space it will take up when stored.

It is common in many programming languages to provide a way to escape special characters in strings. For example, C,
JavaScript, Perl, Python, and even PHP handle special characters in very similar ways.

However, it is important to realize the difference between the number of characters in the code representation of the
string literal and the number of characters in the in-memory string itself.

For example, given the four strings above, the total number of characters of string code (2 + 5 + 10 + 6 = 23)
minus the total number of characters in memory for string values (0 + 3 + 7 + 1 = 11) is 23 - 11 = 12.
'''

import re

input_file = "input.data"

with open(input_file) as f:
  data = f.read().strip().splitlines()

raw_length = 0
memory_length = 0
encoded_length = 0

for line in data:
  raw_length += len(line)
  memory_length += len(eval(line))

  encoded = r'"' + re.sub(r'(["\\])', r'\\\1', line) + r'"'
  encoded_length += len(encoded)

print()
print("Raw:", raw_length)
print("Memory:", memory_length)
print("Difference:", raw_length - memory_length)

print()
print("Encoded:", encoded_length)
print("Difference:", encoded_length - raw_length)
