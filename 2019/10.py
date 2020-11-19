"""
--- Day 10: Monitoring Station ---
You fly into the asteroid belt and reach the Ceres monitoring station. 
The Elves here have an emergency: they're having trouble tracking all of the asteroids and can't be sure they're safe.

The Elves would like to build a new monitoring station in a nearby area of space; they hand you a map of all of the asteroids in that region (your puzzle input).

The map indicates whether each position is empty (.) or contains an asteroid (#). 
The asteroids are much smaller than they appear on the map, and every asteroid is exactly in the center of its marked position. 
The asteroids can be described with X,Y coordinates where X is the distance from the left edge and Y is the distance from the top edge
(so the top-left corner is 0,0 and the position immediately to its right is 1,0).

Your job is to figure out which asteroid would be the best place to build a new monitoring station. 
A monitoring station can detect any asteroid to which it has direct line of sight - that is, there cannot be another asteroid exactly between them. 
This line of sight can be at any angle, not just lines aligned to the grid or diagonally. 
The best location is the asteroid that can detect the largest number of other asteroids.

For example, consider the following map:

.#..#
.....
#####
....#
...##
The best location for a new monitoring station on this map is the highlighted asteroid at 3,4 because it can detect 8 asteroids, more than any other location. 
(The only asteroid it cannot detect is the one at 1,0; its view of this asteroid is blocked by the asteroid at 2,2.) All other asteroids are worse locations; 
they can detect 7 or fewer other asteroids. Here is the number of other asteroids a monitoring station on each asteroid could detect:

.7..7
.....
67775
....7
...87
Here is an asteroid (#) and some examples of the ways its line of sight might be blocked. If there were another asteroid at the location of a capital letter, 
the locations marked with the corresponding lowercase letter would be blocked and could not be detected:

#.........
...A......
...B..a...
.EDCG....a
..F.c.b...
.....c....
..efd.c.gb
.......c..
....f...c.
...e..d..c
Here are some larger examples:

Best is 5,8 with 33 other asteroids detected:
......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####

Best is 1,2 with 35 other asteroids detected:
#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.

Best is 6,3 with 41 other asteroids detected:
.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..

Best is 11,13 with 210 other asteroids detected:
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##

Find the best location for a new monitoring station. How many other asteroids can be detected from that location?
ANSWER: 288

--- Part Two ---
Once you give them the coordinates, the Elves quickly deploy an Instant Monitoring Station to the location and discover the worst: 
there are simply too many asteroids.

The only solution is complete vaporization by giant laser.

Fortunately, in addition to an asteroid scanner, the new monitoring station also comes equipped with a giant rotating laser perfect for vaporizing asteroids. 
The laser starts by pointing up and always rotates clockwise, vaporizing any asteroid it hits.

If multiple asteroids are exactly in line with the station, the laser only has enough power to vaporize one of them before continuing its rotation. 
In other words, the same asteroids that can be detected can be vaporized, but if vaporizing one asteroid makes another one detectable, the newly-detected 
asteroid won't be vaporized until the laser has returned to the same position by rotating a full 360 degrees.

For example, consider the following map, where the asteroid with the new monitoring station (and laser) is marked X:

.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....X...###..
..#.#.....#....##
The first nine asteroids to get vaporized, in order, would be:

.#....###24...#..
##...##.13#67..9#
##...#...5.8####.
..#.....X...###..
..#.#.....#....##
Note that some asteroids (the ones behind the asteroids marked 1, 5, and 7) won't have a chance to be vaporized until the next full rotation. The laser continues rotating; the next nine to be vaporized are:

.#....###.....#..
##...##...#.....#
##...#......1234.
..#.....X...5##..
..#.9.....8....76
The next nine to be vaporized are then:

.8....###.....#..
56...9#...#.....#
34...7...........
..2.....X....##..
..1..............
Finally, the laser completes its first full rotation (1 through 3), a second rotation (4 through 8), and vaporizes the last asteroid (9) partway through its third rotation:

......234.....6..
......1...5.....7
.................
........X....89..
.................
In the large example above (the one with the best monitoring station location at 11,13):

The 1st asteroid to be vaporized is at 11,12.
The 2nd asteroid to be vaporized is at 12,1.
The 3rd asteroid to be vaporized is at 12,2.
The 10th asteroid to be vaporized is at 12,8.
The 20th asteroid to be vaporized is at 16,0.
The 50th asteroid to be vaporized is at 16,9.
The 100th asteroid to be vaporized is at 10,16.
The 199th asteroid to be vaporized is at 9,6.
The 200th asteroid to be vaporized is at 8,2.
The 201st asteroid to be vaporized is at 10,9.
The 299th and final asteroid to be vaporized is at 11,1.
The Elves are placing bets on which will be the 200th asteroid to be vaporized. Win the bet by determining which asteroid that will be; what do you get if you multiply its X coordinate by 100 and then add its Y coordinate? (For example, 8,2 becomes 802.)

ANSWER: 616
"""

import math

data = open("data/10.data").read()


class MonitoringStation:

	def __init__(self, asteroid):
		self.hitMap = {}
		self.location = asteroid
		self.laser = GiantLaserVaporizer()
		asteroid.place(self)

	def __repr__(self):
		return "<MonitoringStation on Asteroid %d,%d>" % (self.location.pos)

	@property
	def x(self):
		return self.location.x

	@property
	def y(self):
		return self.location.y

	@property
	def hits(self):
		return len(self.hitMap)
	
	def distance(self, asteroid):
		a = self.x - asteroid.x
		b = self.y - asteroid.y
		return math.sqrt((a*a) + (b*b))

	def angle(self, asteroid):
		a = self.x - asteroid.x
		b = self.y - asteroid.y
		angle = math.atan2(a, b) * -180/math.pi
		return (angle + 720) % 360

	def scan(self, map):
		self.hitMap = {}
		for asteroid in map.asteroids:
			if asteroid == self.location:
				continue

			if asteroid.mass == 0:
				continue

			distance = self.distance(asteroid)
			angle = self.angle(asteroid)

			if angle in self.hitMap and distance >= self.hitMap[angle][1]:
				continue

			self.hitMap[angle] = (asteroid, distance)

		#self.render()

	def render(self):
		output = []
		for y in range(asteroidMap.height):
			row = []
			for x in range(asteroidMap.width):
				row.append('.')
			output.append(row)

		output[self.y][self.x] = '%d' % self.hits

		for hit in self.hitMap.items():
			asteroid = hit[1][0]
			output[asteroid.y][asteroid.x] = '*'

		for row in output:
			print(''.join(row))


class GiantLaserVaporizer:

	def __init__(self):
		self.reset()

	def fire(self, asteroid):
		asteroid.demolish()
		#print("> Fire! Angle: %.6f deg." % self.angle)

	def reset(self):
		self.angle = 0.0  # straight up (figure out...)
		self.energy = 9

	def step(self):
		self.angle += 0.000001
		print("%.6f" % self.angle)


class Map:

	width = 0
	height = 0
	asteroids = []
	data = []
	best = None

	def __init__(self, data):
		self.analyze(data)

	def analyze(self, data):
		self.data = data.strip().split('\n')
		self.width = len(self.data[0])
		self.height = len(self.data)
		self.asteroids = []

		for y, row in enumerate(self.data):
			for x, column in enumerate(row):
				if column != '.':
					self.asteroids.append(Asteroid((x, y))) 

	def render(self, hits=True):
		output = []
		for y in range(self.height):
			row = []
			for x in range(self.width):
				row.append('.')
			output.append(row)

		for asteroid in self.asteroids:
			representation = '*' if asteroid.mass > 0 else '-'
			if asteroid.best:
				representation = 'X'
			output[asteroid.y][asteroid.x] = str(asteroid.station.hits) if hits else representation

		for row in output:
			print(''.join(row))

		print()


class Asteroid:

	def __init__(self, pos):
		self.pos = pos
		self.station = None
		self.mass = 1000.0
		self.best = False

	def __repr__(self):
		return "<Asteroid @ %d,%d | %dT>" % (self.pos[0], self.pos[1], self.mass)

	@property
	def x(self):
		return self.pos[0]

	@property
	def y(self):
		return self.pos[1]

	def place(self, station):
		self.station = station

	def demolish(self):
		self.mass = 0

#
#

testdata = """
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
"""
#print(data)

asteroidMap = Map(data)
for asteroid in asteroidMap.asteroids:
	station = MonitoringStation(asteroid)
	station.scan(asteroidMap)

#asteroidMap.render()

best = None
for asteroid in asteroidMap.asteroids:
	if best == None or asteroid.station.hits > best.station.hits:
		best = asteroid

if best:
	best.best = True

print("Part 1:", best.station.hits)

#
#

station = best.station
rotations = 0
n = 1
while True:
	station.scan(asteroidMap)
	ordered = sorted(list(map(lambda k: (k[0], k[1][0]), station.hitMap.items())))
	if len(ordered) == 0:
		break

	rotations += 1
	station.laser.reset()
	for asteroid in ordered:
		station.laser.fire(asteroid[1])
		if n == 200:
			#print(n, asteroid)
			print("Part 2:", (asteroid[1].x * 100) + asteroid[1].y)
		n += 1

	if False:
		asteroidMap.render(False)

print("Rotations:", rotations)