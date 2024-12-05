data = open("input.data").read().strip().split("\n")

test_data = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".strip().split("\n")

xdata = test_data

result_1 = 0

for line in data:
    card = line.split(" | ")
    mine = set(card[1].replace("  ", " ").split(" "))
    numbers = set(card[0].replace("  ", " ").split(": ")[1].split(" "))
    matched = mine.intersection(numbers)

    if len(matched) > 0:
        score = 1
        for match in matched:
            score += score

        result_1 += int(score / 2)

print("Part 1:", result_1)

xdata = test_data
cards = {}
copies = {}

def add_card(id):
    print("Add card", id)
    if not id in cards:
        cards[id] = 0
    cards[id] += 1

pile = []
index = 0

def scratch_card(card):
    #print(10 * "----")
    #print("****", card)
    pile.append(card)
    card = card.replace("  ", " ").replace("  ", " ").split(" | ")
    id = int(card[0].split(": ")[0].split(" ")[1])
    #print("Scratch Card", id)
    mine = set(card[1].split(" "))
    numbers = set(card[0].split(": ")[1].split(" "))
    matched = mine.intersection(numbers)
    copies = []

    if len(matched) > 0:
        #print("WIN! COPY next", matched)
        copy_index = id
        for match in matched:
            card = data[copy_index]
            copy_index += 1
            copies.append(card)
            #print("Copy", card)
        #input()

        #print(copies)
        for card in copies:
            #print(">", card)
            scratch_card(card)

        #input()

while True:
    if index >= len(data):
        print("Part 2", len(pile))
        break

    card = data[index]
    scratch_card(card)

    #print("Card", id, "->", cards)
    #input()
    index += 1