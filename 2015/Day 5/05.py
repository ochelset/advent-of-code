"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?

Your puzzle answer was 238.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping,
like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them,
like xyx, abcdefeghi (efe), or even aaa.

For example:
qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

How many strings are nice under these new rules?
"""

import itertools

testdata = """
ugknbfddgicrmopn
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb
"""

testdata2 = """
abcdefeghi
aaa
qjhvhtzxzqqjkmpb
xxyxx
uurcxstgmygtbstg
ieodomkazucvgmuy
eitavndozoezojsi
"""

testdata3 = """
xdwduffwgcptfwad
zbgtglaqqolttgng
ttgrkjjrxnxherxd
qaqlyoyouotsmamm
tadsdceadifqthag
aohjxahenxaermrq
ydpgwxxoxlywxcgi
nscghlafavnsycjh
aoojqakosnaxosom
urybkdyvsrosrfro
boaaruhalgaamqmh
ephlkipjfnjfjrns
ywfmuogvicpywpwm
pkpkrqjvgocvaxjs
usquiquspcdppqeq
tornfzkzhjyofzqa
ldymyvumyhyamopg
azxynqididtrwokb
uetoytptktkmewre
afaefrwhcosurprw
opmopgyabjjjoygt
klvhlhuqhosvjuqk
juududyojcazzgvr
dxsvscqukljxcqyi
rumwchfihhihpqui
zrhemeqegmzrpufd
pjtuxskkowutltlq
yafopikiqswafsit
sknufchjdvccccta
oljkoldhfggkfnfc
dijdacfteteypkoq
xojwroydfeoqupup
uoghiuosiiwiwdws
twsgsfzyszsfinlc
bsnansnfxduritrr
eitavndozoezojsi
qifbtzszfyzsjzyx
kgjruggcikrfrkrw
kbgufbosjghahacw
cyypypveppxxxfuq
lqbjwjqxqbfgdckc
usfenmavvuevevgr
evdqxevdacsbfbjb
vrseaozoheawffoq
ermaenjunjtbekeo
komgvqejojpnykol
gnnalgfvefdfdwwg
nofhmbxififwroeg
oibkuxhjmhxhhzby
badkdgqrpjzbabet
uuxufbwfegysabww
wbqgqkwbibiilhzc
bqzctiuaxpriuiga
aetgqmiqzxbvbviz
joakcwpfggtitizs
wkkypomlvyglpfpf
jcaqyaqvsefwtaya
cmjpjjgndozcmefj
zynfntqwblbnfqik
obkbmflhyanxilnx
iylmzraibygmgmqj
mvhyerxfiljlotjl
mtsynnfxunuohbnf
imylyalawbqwkrwb
mkzvquzvqvwsejqs
kadkaftffaziqdze
fpsrobmbqbmigmwk
xbhjakklmbhsdmdt
fkgrqbyqpqcworqc
"""

#words = testdata2.strip().split("\n")
words = open("input.data").read().strip().split("\n")

def isNice(word: str) -> bool:
    vowels = 0
    consecutive = False
    forbidden = ["ab", "cd", "pq", "xy"]

    for illegal in forbidden:
        if illegal in word:
            return False

    prev_char = ""
    for char in word:
        if not consecutive and char == prev_char:
            consecutive = True

        if char in "aeiou":
            vowels += 1

        prev_char = char

    if vowels < 3:
        return False

    return consecutive

def isNiceWithNewRules(word: str) -> bool:
    letter_map = {}
    for index, letter in enumerate(word):
        if not letter in letter_map:
            letter_map[letter] = []
        letter_map[letter].append((letter, index))

    pairs = findPairsOf([n for n in letter_map.keys() if len(letter_map[n]) > 1], word)
    splits = findSplitsOf([letter_map[n] for n in letter_map.keys() if len(letter_map[n]) > 1], word)

    if pairs > 1 and splits:
        return True

    return False

def findPairsOf(letters: [str], word: str) -> int:
    combinations = []

    for letter in letters:
        combinations.append((letter, letter))
    for combination in itertools.combinations(letters, 2):
        combinations.append(combination)
        combinations.append((combination[1], combination[0]))

    for combination in combinations:
        pair = "".join(combination)

        index = word.find(pair)
        if index == -1:
            continue

        index2 = word.find(pair, index + 2)
        if index2 == -1:
            continue

        return 2

    return 0

def findSplitsOf(letters: list, word: str) -> bool:
    for letter_set in letters:
        prev = letter_set[0]
        for index, letter in enumerate(letter_set):
            if index == 0:
                continue

            if letter[1] - letter_set[index-1][1] == 2:
                return True
            if letter[1] - prev[1] == 2:
                return True

            prev = letter_set[index-1]

    return False

def part1():
    niceWords = 0
    for word in words:
        niceWords += 1 if isNice(word) else 0

    print("Part 1:", niceWords)

def part2():
    niceWords = 0
    for word in words:
        niceWords += 1 if isNiceWithNewRules(word) else 0

    print("Part 2:", niceWords)

part1()
part2()
