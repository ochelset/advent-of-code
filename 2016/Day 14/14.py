import hashlib

def stretch(key: str, repeats: int) -> str:
    for i in range(repeats):
        key = hashlib.md5(key.encode("utf-8")).hexdigest()
    return key

def find_sequence(hash: str, length: int):
    for i in range(length-1, len(hash)):
        letter = hash[i]
        match = True
        for j in range(1, length):
            if hash[i-j] != letter:
                match = False
                break

        if match:
            return [letter]

    return []

def is_valid(matched: {}, index: int, stretched=False) -> bool:
    if len(matched) == 0:
        return False

    for letter in matched:
        pattern = letter * 5
        for j in range(1, 1001):
            next_hash = inputdata + str(index + j)
            if not stretched:
                md5_next = hashlib.md5(next_hash.encode("utf-8"))
                if pattern in md5_next.hexdigest():
                    return True
            else:
                md5 = hashlib.md5(next_hash.encode("utf-8"))
                md5_next = stretch(md5.hexdigest(), 2016)
                if pattern in md5_next:
                    return True

    return False

#

inputdata = "ngcjuoqr"
keys = []

index = 0
while True:
    hash = inputdata + str(index)
    md5 = hashlib.md5(hash.encode("utf-8"))
    key = md5.hexdigest()
    stretched_key = stretch(key, 2016)
    print(hash, key, stretched_key)
    input()

    matched = find_sequence(key, 3)

    if is_valid(matched, index):
        keys.append(key)

        if len(keys) == 64:
            print("Part 1:", index)
            break

    index += 1

keys = []
index = 0
while True:
    hash = inputdata + str(index)
    md5 = hashlib.md5(hash.encode("utf-8"))
    key = stretch(md5.hexdigest(), 2016)
    print(index, hash, key)

    matched = find_sequence(key, 3)
    #print("M", matched)
    #input()

    if is_valid(matched, index, stretched=True):
        keys.append(key)
        print(len(keys), index, matched, "VALID", key)

        #input()

        if len(keys) == 64:
            print("Part 2:", index)
            break

    index += 1