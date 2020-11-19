"""
--- Day 18: Many-Worlds Interpretation ---
As you approach Neptune, a planetary security system detects you and activates a giant tractor beam on Triton! You have no choice but to land.

A scan of the local area reveals only one interesting feature: a massive underground vault. You generate a map of the tunnels (your puzzle input).
The tunnels are too narrow to move diagonally.

Only one entrance (marked @) is present among the open passages (marked .) and stone walls (#),
but you also detect an assortment of keys (shown as lowercase letters) and doors (shown as uppercase letters).
Keys of a given letter open the door of the same letter: a opens A, b opens B, and so on.
You aren't sure which key you need to disable the tractor beam, so you'll need to collect all of them.

For example, suppose you have the following map:

#########
#b.A.@.a#
#########
Starting from the entrance (@), you can only access a large door (A) and a key (a). Moving toward the door doesn't help you,
but you can move 2 steps to collect the key, unlocking A in the process:

#########
#b.....@#
#########
Then, you can move 6 steps to collect the only other key, b:

#########
#@......#
#########
So, collecting every key took a total of 8 steps.

Here is a larger example:

########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################
The only reasonable move is to take key a and unlock door A:

########################
#f.D.E.e.C.b.....@.B.c.#
######################.#
#d.....................#
########################
Then, do the same with key b:

########################
#f.D.E.e.C.@.........c.#
######################.#
#d.....................#
########################
...and the same with key c:

########################
#f.D.E.e.............@.#
######################.#
#d.....................#
########################
Now, you have a choice between keys d and e. While key e is closer, collecting it now would be slower in the long run than collecting key d first,
so that's the best choice:

########################
#f...E.e...............#
######################.#
#@.....................#
########################
Finally, collect key e to unlock door E, then collect key f, taking a grand total of 86 steps.

Here are a few more examples:

########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################
Shortest path is 132 steps: b, a, c, d, f, e, g

#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################
Shortest paths are 136 steps;
one is: a, f, b, j, g, n, h, d, l, o, e, p, c, i, k, m

########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################
Shortest paths are 81 steps; one is: a, c, f, i, d, g, b, e, h

How many steps is the shortest path that collects all of the keys?
ANSWER:
"""

data = """
#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################
"""

class Entity:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '<Entity (%s,%s)>' % (self.x, self.y)

    def __str__(self):
        return '.'

    @property
    def position(self):
        return (self.x, self.y)

    def stepsBetween(self, entity):
        # Should apply route to, containing steps necessary to get there
        # Must also consider if an option will be slower in the long run, even if it is closer
        return abs(self.x - entity.x) + abs(self.y - entity.y)

class Wall(Entity):
    def __repr__(self):
        return '<Wall (%s,%s)>' % (self.x, self.y)

    def __str__(self):
        return '#'

class Key(Entity):
    def __init__(self, x, y, name):
        super().__init__(x, y)
        self.name = name

    def __repr__(self):
        return '<Key %s (%s,%s)>' % (self.name, self.x, self.y)

    def __str__(self):
        return self.name

class Door(Entity):
    def __init__(self, x, y, door):
        super().__init__(x, y)
        self.door = door

    def __repr__(self):
        return '<Door %s (%s,%s)>' % (self.door, self.x, self.y)

    def __str__(self):
        return self.door


class Robot(Entity):

    steps = 0
    def __init__(self, x, y):
        super().__init__(x, y)
        self.steps = 0

    def __repr__(self):
        return '<Robot (%s,%s) -> Steps %s>' % (self.x, self.y, self.steps)

    def __str__(self):
        return '@'

    def moveTo(self, position: Entity):
        # MUST APPLY LOGIC HERE TO SEE IF THERE ARE DOORS/WALLS preventing us from going there
        self.steps += self.stepsBetween(position)
        self.x = position.x
        self.y = position.y

class TunnelAnalyzer():
    map = []
    keys = []
    doors = []
    startingPosition = (0,0)
    width = 0
    height = 0

    def scan(self, data):
        y = 0
        for line in data.strip().split('\n'):
            row = []
            x = 0
            for cell in line:
                if cell == '#':
                    row.append(Wall(x, y))
                elif cell == '@':
                    row.append(Entity(x, y))
                    self.startingPosition = (x, y)
                elif cell.isupper():
                    row.append(Door(x, y, cell))
                    self.doors.append((x, y, cell))
                elif cell.islower():
                    key = Key(x, y, cell)
                    row.append(key)
                    self.keys.append(key)
                else:
                    row.append(Entity(x, y))

                x = x + 1
            self.map.append(row)
            y = y + 1

        self.width = len(self.map[0])
        self.height = len(self.map)

        print('Start at', self.startingPosition, self.width, self.height)

    def findClosestKey(self, fromPosition: Entity) -> Key:
        # need logic here too, to calculate route and check for doors
        closestDistance = 10000
        closestKey = None
        for key in self.keys:
            distance = fromPosition.stepsBetween(key)
            if distance < closestDistance:
                closestDistance = distance
                closestKey = key
        return closestKey

    def pickUp(self, key: Key):
        print('Picking up', key, 'at', key.x, key.y)
        self.map[key.y][key.x] = Entity(key.x, key.y)
        self.keys = list(filter(lambda a: a.name != key.name, self.keys))

    def getAt(self, position):
        if position[0] < 0 or position[0] >= self.width or position[1] < 0 or position[1] >= self.height:
            return None
        return self.map[position[1]][position[0]]

    def getAdjacentTo(self, position):
        x, y = position
        return [self.getAt((x, y-1)), self.getAt((x+1, y)), self.getAt((x, y+1)), self.getAt((x-1, y))]

    def render(self, robot: Robot):
        for y in range(len(self.map)):
            row = []
            for x in range(len(self.map[0])):
                if robot.x == x and robot.y == y:
                    row.append(robot)
                    continue
                row.append(self.map[y][x])

            print(''.join(map(str, row)))


analyzer = TunnelAnalyzer()
analyzer.scan(data)

robot = Robot(analyzer.startingPosition[0], analyzer.startingPosition[1])
closestKey = analyzer.findClosestKey(robot)
robot.moveTo(closestKey)
analyzer.pickUp(closestKey)
analyzer.render(robot)
print(analyzer.getAt(robot.position))
print(analyzer.getAdjacentTo(robot.position))
input()

closestKey = analyzer.findClosestKey(robot)
robot.moveTo(closestKey)
analyzer.pickUp(closestKey)
analyzer.render(robot)
