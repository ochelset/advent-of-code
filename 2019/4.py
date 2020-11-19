"""
--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

--- Part Two ---
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?

Your puzzle input is 359282-820401.
"""

low = 359282
high = 820401

def split(password) -> [int]:
	result = [password % 10]
	f = 10
	for n in range(5):
		password = int(password / 10)
		result.append(password % 10)

	return result

def qualified(original) -> bool:
	password = split(original)
	p = set(password)
	#if len(p) == 6:
	#	return False

	adjacent = False
	groups = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0 }
	for n in range(1, 6):
		x = password[n-1]
		y = password[n]

		# never decreases
		if y > x:
			return False

		# find adjacent equal digits
		if x == y:
			if groups[x] == 0:
				groups[x] += 2
			else:
				groups[x] += 1

	adjacent = filter(lambda x: x[1] > 1, groups.items())

	# at least two adjacent digits are the same, but not in a larger group
	adjacent = filter(lambda y: y[1] == 2, adjacent)

	return len(list(adjacent)) > 0

def generatePasswords():
	valid = 0
	for n in range(low, high):
		if qualified(n):
			valid += 1
			#print("V", n)

	print("Valid combinations:", valid)

generatePasswords()

