"""
--- Day 6: Universal Orbit Map ---
You've landed at the Universal Orbit Map facility on Mercury. Because navigation in space often involves transferring between orbits, 
the orbit maps here are useful for finding efficient routes between, for example, you and Santa. You download a map of the local orbits (your puzzle input).

Except for the universal Center of Mass (COM), every object in space is in orbit around exactly one other object. An orbit looks roughly like this:

                  \
                   \
                    |
                    |
AAA--> o            o <--BBB
                    |
                    |
                   /
                  /
In this diagram, the object BBB is in orbit around AAA. The path that BBB takes around AAA (drawn with lines) is only partly shown. 
In the map data, this orbital relationship is written AAA)BBB, which means "BBB is in orbit around AAA".

Before you use your map data to plot a course, you need to make sure it wasn't corrupted during the download. To verify maps, 
the Universal Orbit Map facility uses orbit count checksums - the total number of direct orbits (like the one shown above) and indirect orbits.

Whenever A orbits B and B orbits C, then A indirectly orbits C. 
This chain can be any number of objects long: if A orbits B, B orbits C, and C orbits D, then A indirectly orbits D.

For example, suppose you have the following map:

COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
Visually, the above map of orbits looks like this:

        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I
In this visual representation, when two objects are connected by a line, the one on the right directly orbits the one on the left.

Here, we can count the total number of orbits as follows:

D directly orbits C and indirectly orbits B and COM, a total of 3 orbits.
L directly orbits K and indirectly orbits J, E, D, C, B, and COM, a total of 7 orbits.
COM orbits nothing.
The total number of direct and indirect orbits in this example is 42.

What is the total number of direct and indirect orbits in your map data? 
Answer: 344238

--- Part Two ---

Now, you just need to figure out how many orbital transfers you (YOU) need to take to get to Santa (SAN).

You start at the object YOU are orbiting; your destination is the object SAN is orbiting. An orbital transfer lets you move from any object 
to an object orbiting or orbited by that object.

For example, suppose you have the following map:

COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
Visually, the above map of orbits looks like this:

                          YOU
                         /
        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN
In this example, YOU are in orbit around K, and SAN is in orbit around I. To move from K to I, a minimum of 4 orbital transfers are required:

K to J
J to E
E to D
D to I
Afterward, the map of orbits looks like this:

        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN
                 \
                  YOU
What is the minimum number of orbital transfers required to move from the object YOU are orbiting to the object SAN is orbiting? (Between the objects 
they are orbiting - not between YOU and SAN.)

Answer: 436
"""

testdata = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
"""

testdata2 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
"""

file = open("data/6.data", "r")
inputs = file.read()
file.close()

#inputs = testdata2

class Object:

	name = ''
	orbits = None 		# The one this object is orbiting
	orbiters = []		# The ones orbiting this object
	count = 0

	def __init__(self, name):
		self.name = name
		self.orbiters = []
		self.count = 0

	def __repr__(self) -> str:
		return "Object <%s ( %s>" % (self.name, self.orbits.name if self.orbits else '')

	def addOrbiter(self, orbiter):
		self.orbiters.append(orbiter)

	def isOrbiting(self, around):
		self.orbits = around
		around.addOrbiter(self)

	def pathToCenter(self):
		paths = []
		orbiter = self
		while orbiter.orbits:
			paths.append(orbiter)
			orbiter = orbiter.orbits

		return paths[1:]

#
#

objects = {}
for relationship in inputs.strip().split('\n'):
	names = relationship.split(')')
	a = Object(names[0])
	b = Object(names[1])

	if names[0] in objects:
		a = objects[names[0]]
	if names[1] in objects:
		b = objects[names[1]]

	b.isOrbiting(a)

	objects[a.name] = a
	objects[b.name] = b

count = 0
for name in objects.keys():
	orbiter = objects[name]
	if orbiter.name == "COM":
		continue

	while orbiter.orbits:
		count += 1
		orbiter = orbiter.orbits

print("Total orbits:", count)

you = objects["YOU"]
santa = objects["SAN"]
myPath = you.pathToCenter()
santasPath = santa.pathToCenter()

while myPath[-1] == santasPath[-1]:
	myPath.pop()
	santasPath.pop()

print("Orbital transfers:", len(myPath) + len(santasPath))
