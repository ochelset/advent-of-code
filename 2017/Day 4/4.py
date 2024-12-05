from itertools import permutations

passphrases = open("input.data").read().strip().split("\n")


def validate(passphrase: str, secure=False) -> bool:
    buffer = {}
    words = passphrase.split(" ")
    for word in words:
        if word in buffer:
            return False

        buffer[word] = 1
        if secure:
            anagrams = set(permutations(word))
            for anagram in anagrams:
                if anagram == word:
                    continue
                if anagram in buffer:
                    return False
                buffer[anagram] = 1

    return True


for i in (0, 1):
    valid_counter = 0
    for line in passphrases:
        if validate(line, secure=[False, True][i != 0]):
            valid_counter += 1
    print("Part %s:" % (i + 1), valid_counter)
