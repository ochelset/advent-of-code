inputdata = open("input.data").read().strip().splitlines()
inputdatax = """
aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
""".strip().splitlines()

def analyze(room):
    key, checksum = room[:-1].split("[")
    sector_id = int(key.split("-")[-1])
    analysis = { "sector_id":sector_id, "key": key.replace("-", " "), "checksum": checksum, "histogram": {}, "valid": True }

    for char in key:
        if char == "-":
            continue
        if char not in analysis["histogram"]:
            analysis["histogram"][char] = 0
        analysis["histogram"][char] += 1

    s = float('inf')
    prev_letter = None
    for letter in analysis["checksum"]:
        if letter not in key:
            analysis["valid"] = False
            break

        if analysis["histogram"][letter] < s:
            #print(">", letter, "<", analysis["histogram"][letter], s)
            s = analysis["histogram"][letter]
        elif analysis["histogram"][letter] == s and ord(letter) > ord(prev_letter):
            #print(">", letter, "=", analysis["histogram"][letter], s)
            s = analysis["histogram"][letter]
            #print("XXX", letter, ord(letter), analysis["histogram"][letter], s)
            #input()
        else:
            analysis["valid"] = False
            break
        prev_letter = letter
    return analysis

def decipher(key, shift=0):
    output = ""
    for letter in key:
        if letter in ("-", " "):
            output += " "
            continue

        deciphered = ord(letter)
        deciphered += shift % 26
        if deciphered > 122:
            deciphered -= 26

        output += chr(deciphered)
    return output

sector_id_sum = 0
valid_rooms = []
for line in inputdata:
    room = analyze(line)
    if room["valid"]:
        sector_id_sum += room["sector_id"]
        valid_rooms.append(room)

print("Part 1:", sector_id_sum)

for room in valid_rooms:
    key = room["key"]
    decrypted = decipher(key, room["sector_id"])

    if "north" in decrypted:
        print(decrypted, room)
