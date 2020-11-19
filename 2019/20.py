"""
--- Day 20: Donut Maze ---
You notice a strange pattern on the surface of Pluto and land nearby to get a closer look. Upon closer inspection,
you realize you've come across one of the famous space-warping mazes of the long-lost Pluto civilization!

Because there isn't much space on Pluto, the civilization that used to live here thrived by inventing a method for folding spacetime.
Although the technology is no longer understood, mazes like this one provide a small glimpse into the daily life of an ancient Pluto citizen.

This maze is shaped like a donut. Portals along the inner and outer edge of the donut can instantly teleport you from one side to the other. For example:

         A
         A
  #######.#########
  #######.........#
  #######.#######.#
  #######.#######.#
  #######.#######.#
  #####  B    ###.#
BC...##  C    ###.#
  ##.##       ###.#
  ##...DE  F  ###.#
  #####    G  ###.#
  #########.#####.#
DE..#######...###.#
  #.#########.###.#
FG..#########.....#
  ###########.#####
             Z
             Z
This map of the maze shows solid walls (#) and open passages (.).
Every maze on Pluto has a start (the open tile next to AA) and an end (the open tile next to ZZ).
Mazes on Pluto also have portals; this maze has three pairs of portals: BC, DE, and FG. When on an open tile next to one of these labels,
a single step can take you to the other tile with the same label. (You can only walk on . tiles; labels and empty space are not traversable.)

One path through the maze doesn't require any portals.
Starting at AA, you could go down 1, right 8, down 12, left 4, and down 1 to reach ZZ, a total of 26 steps.

However, there is a shorter path:
You could walk from AA to the inner BC portal (4 steps),
warp to the outer BC portal (1 step), walk to the inner DE (6 steps), warp to the outer DE (1 step),
walk to the outer FG (4 steps), warp to the inner FG (1 step), and finally walk to ZZ (6 steps). In total, this is only 23 steps.

Here is a larger example:

                   A
                   A
  #################.#############
  #.#...#...................#.#.#
  #.#.#.###.###.###.#########.#.#
  #.#.#.......#...#.....#.#.#...#
  #.#########.###.#####.#.#.###.#
  #.............#.#.....#.......#
  ###.###########.###.#####.#.#.#
  #.....#        A   C    #.#.#.#
  #######        S   P    #####.#
  #.#...#                 #......VT
  #.#.#.#                 #.#####
  #...#.#               YN....#.#
  #.###.#                 #####.#
DI....#.#                 #.....#
  #####.#                 #.###.#
ZZ......#               QG....#..AS
  ###.###                 #######
JO..#.#.#                 #.....#
  #.#.#.#                 ###.#.#
  #...#..DI             BU....#..LF
  #####.#                 #.#####
YN......#               VT..#....QG
  #.###.#                 #.###.#
  #.#...#                 #.....#
  ###.###    J L     J    #.#.###
  #.....#    O F     P    #.#...#
  #.###.#####.#.#####.#####.###.#
  #...#.#.#...#.....#.....#.#...#
  #.#####.###.###.#.#.#########.#
  #...#.#.....#...#.#.#.#.....#.#
  #.###.#####.###.###.#.#.#######
  #.#.........#...#.............#
  #########.###.###.#############
           B   J   C
           U   P   P
Here, AA has no direct path to ZZ, but it does connect to AS and CP. By passing through AS, QG, BU, and JO, you can reach ZZ in 58 steps.

In your maze, how many steps does it take to get from the open tile marked AA to the open tile marked ZZ?
ANSWER: 604

--- Part Two ---
Strangely, the exit isn't open when you reach it. Then, you remember: the ancient Plutonians were famous for building recursive spaces.

The marked connections in the maze aren't portals: they physically connect to a larger or smaller copy of the maze. Specifically,
the labeled tiles around the inside edge actually connect to a smaller copy of the same maze,
and the smaller copy's inner labeled tiles connect to yet a smaller copy, and so on.

When you enter the maze, you are at the outermost level; when at the outermost level,
only the outer labels AA and ZZ function (as the start and end, respectively); all other outer labeled tiles are effectively walls.
At any other level, AA and ZZ count as walls, but the other outer labeled tiles bring you one level outward.

Your goal is to find a path through the maze that brings you back to ZZ at the outermost level of the maze.

In the first example above, the shortest path is now the loop around the right side. If the starting level is 0,
then taking the previously-shortest path would pass through BC (to level 1), DE (to level 2), and FG (back to level 1).
Because this is not the outermost level, ZZ is a wall, and the only option is to go back around to BC,
which would only send you even deeper into the recursive maze.

In the second example above, there is no path that brings you to ZZ at the outermost level.

Here is a more interesting example:

             Z L X W       C
             Z P Q B       K
  ###########.#.#.#.#######.###############
  #...#.......#.#.......#.#.......#.#.#...#
  ###.#.#.#.#.#.#.#.###.#.#.#######.#.#.###
  #.#...#.#.#...#.#.#...#...#...#.#.......#
  #.###.#######.###.###.#.###.###.#.#######
  #...#.......#.#...#...#.............#...#
  #.#########.#######.#.#######.#######.###
  #...#.#    F       R I       Z    #.#.#.#
  #.###.#    D       E C       H    #.#.#.#
  #.#...#                           #...#.#
  #.###.#                           #.###.#
  #.#....OA                       WB..#.#..ZH
  #.###.#                           #.#.#.#
CJ......#                           #.....#
  #######                           #######
  #.#....CK                         #......IC
  #.###.#                           #.###.#
  #.....#                           #...#.#
  ###.###                           #.#.#.#
XF....#.#                         RF..#.#.#
  #####.#                           #######
  #......CJ                       NM..#...#
  ###.#.#                           #.###.#
RE....#.#                           #......RF
  ###.###        X   X       L      #.#.#.#
  #.....#        F   Q       P      #.#.#.#
  ###.###########.###.#######.#########.###
  #.....#...#.....#.......#...#.....#.#...#
  #####.#.###.#######.#######.###.###.#.#.#
  #.......#.......#.#.#.#.#...#...#...#.#.#
  #####.###.#####.#.#.#.#.###.###.#.###.###
  #.......#.....#.#...#...............#...#
  #############.#.#.###.###################
               A O F   N
               A A D   M
One shortest path through the maze is the following:

Walk from AA to XF (16 steps)
Recurse into level 1 through XF (1 step)
Walk from XF to CK (10 steps)
Recurse into level 2 through CK (1 step)
Walk from CK to ZH (14 steps)
Recurse into level 3 through ZH (1 step)
Walk from ZH to WB (10 steps)
Recurse into level 4 through WB (1 step)
Walk from WB to IC (10 steps)
Recurse into level 5 through IC (1 step)
Walk from IC to RF (10 steps)
Recurse into level 6 through RF (1 step)
Walk from RF to NM (8 steps)
Recurse into level 7 through NM (1 step)
Walk from NM to LP (12 steps)
Recurse into level 8 through LP (1 step)
Walk from LP to FD (24 steps)
Recurse into level 9 through FD (1 step)
Walk from FD to XQ (8 steps)
Recurse into level 10 through XQ (1 step)
Walk from XQ to WB (4 steps)
Return to level 9 through WB (1 step)
Walk from WB to ZH (10 steps)
Return to level 8 through ZH (1 step)
Walk from ZH to CK (14 steps)
Return to level 7 through CK (1 step)
Walk from CK to XF (10 steps)
Return to level 6 through XF (1 step)
Walk from XF to OA (14 steps)
Return to level 5 through OA (1 step)
Walk from OA to CJ (8 steps)
Return to level 4 through CJ (1 step)
Walk from CJ to RE (8 steps)
Return to level 3 through RE (1 step)
Walk from RE to IC (4 steps)
Recurse into level 4 through IC (1 step)
Walk from IC to RF (10 steps)
Recurse into level 5 through RF (1 step)
Walk from RF to NM (8 steps)
Recurse into level 6 through NM (1 step)
Walk from NM to LP (12 steps)
Recurse into level 7 through LP (1 step)
Walk from LP to FD (24 steps)
Recurse into level 8 through FD (1 step)
Walk from FD to XQ (8 steps)
Recurse into level 9 through XQ (1 step)
Walk from XQ to WB (4 steps)
Return to level 8 through WB (1 step)
Walk from WB to ZH (10 steps)
Return to level 7 through ZH (1 step)
Walk from ZH to CK (14 steps)
Return to level 6 through CK (1 step)
Walk from CK to XF (10 steps)
Return to level 5 through XF (1 step)
Walk from XF to OA (14 steps)
Return to level 4 through OA (1 step)
Walk from OA to CJ (8 steps)
Return to level 3 through CJ (1 step)
Walk from CJ to RE (8 steps)
Return to level 2 through RE (1 step)
Walk from RE to XQ (14 steps)
Return to level 1 through XQ (1 step)
Walk from XQ to FD (8 steps)
Return to level 0 through FD (1 step)
Walk from FD to ZZ (18 steps)
This path takes a total of 396 steps to move from AA at the outermost layer to ZZ at the outermost layer.

In your maze, when accounting for recursion, how many steps does it take to get from the open tile marked AA to the open tile marked ZZ,
both at the outermost layer?
ANSWER
"""

testdata1 = """
         A
         A
  #######.#########
  #######.........#
  #######.#######.#
  #######.#######.#
  #######.#######.#
  #####  B    ###.#
BC...##  C    ###.#
  ##.##       ###.#
  ##...DE  F  ###.#
  #####    G  ###.#
  #########.#####.#
DE..#######...###.#
  #.#########.###.#
FG..#########.....#
  ###########.#####
             Z
             Z
"""

testdata2 = """
                   A
                   A
  #################.#############
  #.#...#...................#.#.#
  #.#.#.###.###.###.#########.#.#
  #.#.#.......#...#.....#.#.#...#
  #.#########.###.#####.#.#.###.#
  #.............#.#.....#.......#
  ###.###########.###.#####.#.#.#
  #.....#        A   C    #.#.#.#
  #######        S   P    #####.#
  #.#...#                 #......VT
  #.#.#.#                 #.#####
  #...#.#               YN....#.#
  #.###.#                 #####.#
DI....#.#                 #.....#
  #####.#                 #.###.#
ZZ......#               QG....#..AS
  ###.###                 #######
JO..#.#.#                 #.....#
  #.#.#.#                 ###.#.#
  #...#..DI             BU....#..LF
  #####.#                 #.#####
YN......#               VT..#....QG
  #.###.#                 #.###.#
  #.#...#                 #.....#
  ###.###    J L     J    #.#.###
  #.....#    O F     P    #.#...#
  #.###.#####.#.#####.#####.###.#
  #...#.#.#...#.....#.....#.#...#
  #.#####.###.###.#.#.#########.#
  #...#.#.....#...#.#.#.#.....#.#
  #.###.#####.###.###.#.#.#######
  #.#.........#...#.............#
  #########.###.###.#############
           B   J   C
           U   P   P
"""

testdata3 = """

             Z L X W       C                 
             Z P Q B       K                 
  ###########.#.#.#.#######.###############  
  #...#.......#.#.......#.#.......#.#.#...#  
  ###.#.#.#.#.#.#.#.###.#.#.#######.#.#.###  
  #.#...#.#.#...#.#.#...#...#...#.#.......#  
  #.###.#######.###.###.#.###.###.#.#######  
  #...#.......#.#...#...#.............#...#  
  #.#########.#######.#.#######.#######.###  
  #...#.#    F       R I       Z    #.#.#.#  
  #.###.#    D       E C       H    #.#.#.#  
  #.#...#                           #...#.#  
  #.###.#                           #.###.#  
  #.#....OA                       WB..#.#..ZH
  #.###.#                           #.#.#.#  
CJ......#                           #.....#  
  #######                           #######  
  #.#....CK                         #......IC
  #.###.#                           #.###.#  
  #.....#                           #...#.#  
  ###.###                           #.#.#.#  
XF....#.#                         RF..#.#.#  
  #####.#                           #######  
  #......CJ                       NM..#...#  
  ###.#.#                           #.###.#  
RE....#.#                           #......RF
  ###.###        X   X       L      #.#.#.#  
  #.....#        F   Q       P      #.#.#.#  
  ###.###########.###.#######.#########.###  
  #.....#...#.....#.......#...#.....#.#...#  
  #####.#.###.#######.#######.###.###.#.#.#  
  #.......#.......#.#.#.#.#...#...#...#.#.#  
  #####.###.#####.#.#.#.#.###.###.#.###.###  
  #.......#.....#.#...#...............#...#  
  #############.#.#.###.###################  
               A O F   N                     
               A A D   M                   
"""

DIRECTIONS = {
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, -1),
    "D": (0, 1)
}

class Maze:

    maze = []
    entrance = None
    exit = None
    level = 0

    def __init__(self, data, recursive=False, hideWalls=True, level=0):
        self.data = data
        self.level = level
        self.hideWalls = hideWalls
        self.recursive = recursive
        self.analyze()

    def open(self, position):
        print("OPEN NEW MAZE", position)
        return Maze(self.data, recursive=self.recursive, hideWalls=self.hideWalls, level=self.level+1)

    def analyze(self):
        self.lines = []
        self.maze = {}
        self.portals = {}
        self.width = 0

        portalBuffer = {}
        for line in self.data.split('\n'):
            if line.strip() == '':
                continue
            if len(line) > self.width:
                self.width = len(line)
            self.lines.append(line)
        self.height = len(self.lines)
        z = self.level

        for y in range(self.height):
            line = self.lines[y]
            for x in range(self.width):
                if x < len(line):
                    if (x, y) in self.maze:
                        continue

                    char = line[x]
                    if char == '#':
                        self.maze[(x, y, z)] = Wall(x, y, z)
                    elif char == '.':
                        self.maze[(x, y, z)] = Path(x, y, z)
                    elif char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        code = self.getCodeAt(x, y)
                        self.maze[(x, y, z)] = Letter(char, x, y)
                        if code:
                            if code[1] == 'AA':
                                if self.level == 0:
                                    self.entrance = Entrance(code[0][0], code[0][1])
                                    self.maze[code[0]] = self.entrance
                                else:
                                    self.maze[(x, y, z)] = Wall(x, y, z)
                            elif code[1] == 'ZZ':
                                if self.level == 0:
                                    self.exit = Exit(code[0][0], code[0][1])
                                    self.maze[code[0]] = self.exit
                                else:
                                    self.maze[(x, y, z)] = Wall(x, y, z)
                            else:
                                portal = Portal(code[0][0], code[0][1], code[1], code[2])
                                if portal.code in portalBuffer:
                                    portalBuffer[portal.code].connect(portal)
                                    portal.connect(portalBuffer[portal.code])
                                else:
                                    portalBuffer[portal.code] = portal
                                self.portals[code[0]] = portal
                                self.maze[code[0]] = portal

    def getCodeAt(self, x, y):
        char = self.lines[y][x]
        left = (-1, 0)
        above = (0, -1)
        right = (1, 0)
        below = (0, 1)
        position = (x, y)

        result = [char]
        for adjacent in [left, above, right, below]:
            x1 = x + adjacent[0]
            y1 = y + adjacent[1]
            if y1 < 0 or y1 >= self.height:
                continue

            line = self.lines[y1]

            if x1 < 0 or x1 >= len(line):
                continue

            code = self.lines[y1][x1]
            if code == ' ':
                continue

            if code == '.':
                position = (x1, y1)

            if adjacent == left or adjacent == above:
                result.insert(0, code)
            else:
                result.append(code)

        if not '.' in result:
            return None

        inner = True
        if position[0] == 2 or position[1] == 2 or position[0] == self.width-3 or position[1] == self.height-3:
            inner = False

        #print(self.width, self.height, position, ''.join(result), inner)
        return (position, ''.join(list(filter(lambda char: char != '.', result))), inner)

    def getBlockAt(self, x, y, z):
        return self.maze[(x, y, z)] if (x, y, z) in self.maze else None

    def getPortalAt(self, x, y, z):
        return self.portals[(x, y, z)] if (x, y, z) in self.portals else None

    def getAdjacentTo(self, x, y, z):
        west = self.getBlockAt(x - 1, y, z)
        east = self.getBlockAt(x + 1, y, z)
        north = self.getBlockAt(x, y - 1, z)
        south = self.getBlockAt(x, y + 1, z)
        return (west, north, east, south)


class Block:

    def __init__(self, x, y, z=0):
        self.position = (x, y, z)

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

    @property
    def z(self):
        return self.position[2]

class Letter(Block):

    def __init__(self, char, x, y):
        self.char = char
        super().__init__(x, y, 0)


class Entrance(Block):

    def __repr__(self):
        return "<Entrance %d,%d,%d>" % self.position


class Exit(Block):

    def __repr__(self):
        return "<Exit %d,%d,%d>" % self.position


class Wall(Block):

    def __repr__(self):
        return "<Wall %d,%d,%d>" % self.position


class Path(Block):

    def __repr__(self):
        return "<Path %d,%d,%d>" % self.position


class Portal(Block):

    def __init__(self, x, y, z, code, inner=False):
        super().__init__(x, y, z)
        self.exit = self.position
        self.code = code
        self.inner = inner

    def __repr__(self):
        return "<Portal %s %d,%d,%d <=> %d,%d,%d) %s>" % (self.code, self.position[0], self.position[1], self.position[2], self.exit[0], self.exit[1], self.exit[2], 'Inner' if self.inner else 'Outer')

    def connect(self, portal):
        self.exit = portal.position


class Intersection:

    def __init__(self, a, b, exits=[]):
        self.routes = [b] + exits
        self.taken = {}
        self.take(a, b)

    def __repr__(self):
        return "<Intersection %s>" % self.routes

    def take(self, a, b):
        self.taken[(a, b)] = 1
        self.taken[(b, a)] = 1

    def isTaken(self, a, b):
        return True if (a, b) in self.taken else False

    def isDone(self, a):
        for route in self.routes:
            if a == route.position:
                continue
            if not self.isTaken(a, route.position):
                return False
        return True

    def next(self, a):
        print("NXY", a, self.routes)
        for route in self.routes:
            if a == route.position:
                continue
            if not self.isTaken(a, route.position):
                self.take(a, route.position)
                return route.position
        return None

class Level:

    def __init__(self, maze):
        self.maze = maze

class Person(Block):

    level = 0
    mazes = []

    @property
    def maze(self):
        return self.mazes[self.level]

    def __init__(self, maze):
        self.mazes = [maze]
        super().__init__(self.maze.entrance.position[0], self.maze.entrance.position[1])
        self.visited = {}

    def explore(self):
        self.steps = 0
        self.route = []
        self.visited = { self.position: 1 }
        self.best = []
        self.intersections = {}
        self.level = 0

        while True:
            best = len(self.best)
            nextPosition = None
            if self.position == None:
                self.visited = {}
                for position in self.best:
                    self.visited[position] = 1
                self.render()
                print()
                print("ROUTE", self.best)
                print("BEST ROUTE:", best)
                break

            #print("-"*80)
            #self.render()

            currentBlock = self.maze.getBlockAt(self.x, self.y, self.z)
            if isinstance(currentBlock, Exit):
                if best == 0 or best > len(self.route):
                    self.best = self.route[:]

                nextPosition = self.backtrack()
                if nextPosition:
                    self.position = nextPosition
                    continue

            #print("Best:", best, len(self.route))
            #if best > 0 and best < len(self.route):
            #    nextPosition = self.backtrack()
            #    if nextPosition:
            #        self.position = nextPosition

            #    print("BACKTRACKED", self.position, best)
            #    input()
            #    continue

            # Add current position to the route and set to visited
            self.route.append(self.position)
            self.visited[self.position] = 1

            prevPosition = self.route[-2] if len(self.route) > 1 else self.route[-1]
            prevBlock = self.maze.getBlockAt(prevPosition[0], prevPosition[1], prevPosition[2])
            print("PP", self.position, prevPosition, prevBlock)

            possibleMoves = self.getPossibleMoves()

            # Generate new intersection if not already done
            if len(possibleMoves) > 1:
                if not self.position in self.intersections:
                    self.intersections[self.position] = Intersection(currentBlock, prevBlock, possibleMoves)

            # If at an intersection, get next possible way out
            intersection = self.intersections[self.position] if self.position in self.intersections else None
            if intersection:
                nextPosition = intersection.next(prevPosition)
                #print("INTERSECT:", intersection, (prevPosition, self.position), "=>", nextPosition)
            else:
                for possible in possibleMoves:
                    if not possible.position in self.visited:
                        if isinstance(possible, Portal):
                            self.route.append(possible.position)
                            self.visited[possible.position] = 1

                            if self.maze.recursive:
                                if possible.inner:
                                    self.openDoor(possible)
                                else:
                                    print("Close door and return to previous level")
                                continue

                            nextPosition = possible.exit
                            self.visited[nextPosition] = 1
                            print("> WRP to", self.level, possible.code, possible.exit, possible, self.maze.recursive)

                            break

                        nextPosition = possible.position
                        break

            if not nextPosition and isinstance(currentBlock, Portal):
                #print("IS AT PORTAL", currentBlock, currentBlock.exit in self.visited)
                if currentBlock.exit in self.visited:
                    nextPosition = self.backtrack()
                else:
                    nextPosition = currentBlock.exit
                    self.visited[nextPosition] = 1
                    print("> WRPX to", currentBlock.code, currentBlock.exit, currentBlock)

            # Backtrack if dead end
            if not nextPosition:
                nextPosition = self.backtrack()

            #print("POSITION:", self.position, currentBlock)
            #print("POSSIBLES:", west, east, north, south, "=>", possibleMoves)
            #print("VISITADOS:", self.visited)
            #print("NEXT POS: ", nextPosition)
            #print("INTERSECT:", intersections)
            #print("ROUTE:    ", len(self.route), self.route)

            self.render()
            print("POS", self.position, "->", nextPosition)
            input(">")

            self.position = nextPosition

    def backtrack(self):
        while True:
            if not len(self.route):
                return None

            backtrackedTo = self.route.pop()
            if backtrackedTo in self.visited:
                del self.visited[backtrackedTo]

            intersection = self.intersections[backtrackedTo] if backtrackedTo in self.intersections else None
            if not intersection:
                continue

            if not len(self.route):
                return None

            prevPosition = self.route[-1]
            if intersection.isDone(prevPosition):
                del self.intersections[backtrackedTo]
                continue

            #print("BACKTRACKED TO", backtrackedTo)
            return backtrackedTo

    def openDoor(self, door):
        #self.render()

        self.mazes.append(self.maze.open(door.exit))
        print(self.mazes)
        self.level += 1
        #self.visited[self.level] = { door.exit: 1 }

        print("Open door %s and enter level" % door.code, self.level)
        self.render()
        input()

    def getPossibleMoves(self):
        possibles = list(filter(lambda x: (x != None and not isinstance(x, Wall)) and not isinstance(x, Letter) and x.position not in self.visited, self.maze.getAdjacentTo(self.x, self.y, self.z)))
        return list(filter(lambda x: (not isinstance(x, Portal)) or x.exit not in self.visited, possibles))

    def move(self, steps, direction):
        self.position = (self.x + (direction[0] * steps), self.y + (direction[1] * steps))
        self.steps += steps

    def render(self):
        wall = ' ' if self.maze.hideWalls else '#'

        print()
        print(80*'-')
        print("LEVEL", self.level, self.position)
        z = self.level
        for y in range(self.maze.height):
            output = []
            for x in range(self.maze.width):
                if (x, y, self.level) == self.position:
                    output.append('+')
                    continue

                block = self.maze.getBlockAt(x, y, z)
                char = ' '
                if isinstance(block, Wall):
                    char = wall
                elif isinstance(block, Path):
                    char = '\u00B7'
                elif isinstance(block, Entrance):
                    char = '\u2A00'
                elif isinstance(block, Exit):
                    char = 'X'
                elif isinstance(block, Portal):
                    char = ' ' #'\u2299'
                elif isinstance(block, Letter):
                    char = block.char

                #if self.level > 0:


                if block and block.position in self.visited:
                    char = '*'

                output.append(char)

            output.append(str(y))
            print(''.join(output))
        print(self.visited)

#
#

data = open("data/20.data").read()

#maze = Maze(data)
#robot = Person(maze)
#robot.explore()

maze = Maze(testdata2, recursive=True, hideWalls=True)
robot = Person(maze)
robot.explore()