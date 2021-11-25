"""
--- Day 11: Corporate Policy ---

Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password
based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for
security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step;
if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz.
They cannot skip letters; abd doesn't count.
Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are
therefore confusing.
Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.

For example:
hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement
         (because it contains i and l).
abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
abbcegjk fails the third requirement, because it only has one double letter (bb).
The next password after abcdefgh is abcdffaa.
The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi...,
since i is not allowed.
Given Santa's current password (your puzzle input), what should his next password be?

Your puzzle input is vzbxkghb.
"""

MIN_LENGTH = 8
ILLEGAL_CHARS = [ord("i"), ord("o"), ord("l")]
LOW = ord("a")
HIGH = ord("z")

def valid(password: list) -> bool:
  if len(password) < MIN_LENGTH:
    return False

  if contains_illegal_chars(password):
    return False

  if not contains_increasing_straight(password):
    return False

  if not contains_overlapping_pairs(password):
    return False

  return True

def contains_illegal_chars(password: list) -> bool:
  return len(list(filter(lambda x: x in ILLEGAL_CHARS, password))) > 0

def contains_increasing_straight(password: list) -> bool:
  for i in range(len(password)-3):
    if list(map(lambda x: x-password[i], password[i:i+3])) == [0, 1, 2]:
      return True

  return False

def contains_overlapping_pairs(password: list) -> bool:
  pairs = set()
  letter = None
  for char in password:
    if char == letter:
      pairs.add(char)

    letter = char

  return len(pairs) >= 2

def increment(password: list) -> list:
  buffer = password[::-1]
  incrementor = 1
  zero = None
  for i in range(MIN_LENGTH):
    if buffer[i] in ILLEGAL_CHARS:
      zero = i
      buffer[i] += 1
      break

    buffer[i] += incrementor
    if buffer[i] > HIGH:
      buffer[i] = LOW
    else:
      incrementor = 0

  if zero != None:
    for i in range(zero):
      buffer[i] = LOW

  return buffer[::-1]

def convert(password: str) -> [int]:
  return list(map(lambda x: ord(x), list(password)))

def converted(password: list) -> str:
  return "".join(list(map(lambda x: chr(x), password)))

def get_next_password(password: str) -> str:
  password = increment(convert(password))
  while not valid(password):
    password = increment(password)

  return converted(password)

p1 = "vzbxkghb"
for i in range(2):
  p1 = get_next_password(p1)
  print("Part %s:" % (i + 1), p1)
