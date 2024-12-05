inputdata = open("input.data").read().strip().split("\n\n")
inputdata = open("example.data").read().strip().split("\n\n")

scanner_map = {}

# build a complete rotation map for each scanner
# check for overlapping points - can be any of x,y,z against z,x,y

class Scanner:
    def __init__(self, id):
        self.id = id
        self.x = 0
        self.y = 0
        self.z = 0
        self.rx = 0
        self.ry = 0
        self.rz = 0
        self.beacons: [Beacon] = []
        self.scans = []

    def set_pos(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def add(self, x: int, y: int, z: int):
        self.beacons.append(Beacon(x, y, z))

    def __repr__(self):
        return "<Scanner %s: %s,%s,%s>" % (self.id, self.x, self.y, self.z)
#

class Beacon:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "<Beacon @ %s>" % str(self.pos)

    @property
    def pos(self) -> (int, int, int):
        return (self.x, self.y, self.z)
#

for scanner in inputdata:
    data = scanner.splitlines()
    id = int(data.pop(0).replace("--- scanner ", "").replace(" ---", ""))
    scanner = Scanner(id)
    scanner_map[id] = scanner

    for line in data:
        x, y, z = line.split(",")
        scanner.add(int(x), int(y), int(z))

#

def check_overlapping(id1, id2):
    scanner1 = scanner_map[id1]
    scanner2 = scanner_map[id2]
    overlapping = []

    print("CHECKING", scanner1, scanner2)
    for beacon1 in scanner1.beacons:
        for beacon2 in scanner2.beacons:
            adjusted = beacon2.pos
            adjusted = (adjusted[0] + scanner2.x, adjusted[1] + scanner2.y, adjusted[2] + scanner2.z)
            print("CMP", beacon1.pos, beacon2.pos, adjusted)
        input()


scanner_map[1].set_pos(68, -1246, -43)
check_overlapping(0, 1)
#