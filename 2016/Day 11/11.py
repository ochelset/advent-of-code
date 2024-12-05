"""
The first floor contains a polonium generator, a thulium generator, a thulium-compatible microchip, a promethium generator, a ruthenium generator,
    a ruthenium-compatible microchip, a cobalt generator, and a cobalt-compatible microchip.
The second floor contains a polonium-compatible microchip and a promethium-compatible microchip.
The third floor contains nothing relevant.
The fourth floor contains nothing relevant.
"""

floors = [
    [" E ", "POG", None, "THG", "THM", "PRG", None, "RUG", "RUM", "COG", "COM"],
    [None, None, "POM", None, None, None, "PRM", None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None],
]
silos = {
    "POG": 1,
    "POM": 2,
    "THG": 3,
    "THM": 4,
    "PRG": 5,
    "PRM": 6,
    "RUG": 7,
    "RUM": 8,
    "COG": 9,
    "COM": 10
}

"""
The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.
"""

if True:
    floors = [
        [" E ", None, "HYM", None, "LYM"],
        [None, "HYG", None, None, None],
        [None, None, None, "LYG", None],
        [None, None, None, None, None]
    ]
    silos = {
        "HYG": 1,
        "HYM": 2,
        "LYG": 3,
        "LYM": 4
    }

elevator = {
    "floor": 0,
    "content": [],
    "dir": 1
}

def render(floors):
    print()
    index = 4
    for floor in floors[::-1]:
        row = list(map(lambda room: " . " if not room else room, floor))
        generators = list(filter(lambda room: room != None and room.endswith("G"), floor))
        for room in floor:
            if not room:
                continue
            generator = room[:2] + "G"
            if room.endswith("M") and generator not in floor and generator in generators:
                row.append("X")
        print("F%s" % index, " ".join(row))
        index -= 1

def scan(floor):
    if floor < 0 or floor >= 4:
        return []
    return [x for x in floors[floor] if x != None]

def move():
    if len(elevator["content"]) == 0:
        return

    print("Move:", elevator)
    new_current = list(map(lambda x: None if x == " E " or x in elevator["content"] else x, floors[elevator["floor"]]))
    floors[elevator["floor"]] = new_current

    elevator["floor"] += elevator["dir"]
    floors[elevator["floor"]][0] = " E "
    while elevator["content"]:
        item = elevator["content"].pop()
        floors[elevator["floor"]][silos[item]] = item

    #print(new_current)
#

render(floors)

while None in floors[-1]:
    above = scan(elevator["floor"] + 1)
    current = scan(elevator["floor"])
    below = scan(elevator["floor"] - 1)

    print("Above:", above)
    print("Currt:", current)
    print("Below:", below)

    if len(elevator["content"]) < 2:
        print("PICK UP")
        for item in above:
            prefix = item[:2]
            match = list(filter(lambda x: x[:2] == prefix, current))
            #print("FOUND", prefix, match)
            if len(match):
                #elevator["content"].append(item)
                elevator["content"].append(match[0])
                #break

    move()
    render(floors)
    input()