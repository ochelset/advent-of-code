import time
from itertools import permutations

"""
--- Day 9: All in a Single Night ---
Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982
The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?
"""

testdata = """
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"""

t1 = time.perf_counter()
inputdata = open("input.data").read()
#inputdata = testdata

routes = {}
cities = set()
distances = set()

def add_city(city: str, destination: str, distance: int):
  cities.add(city)
  cities.add(destination)

  routes[(city, destination)] = distance
  routes[(destination, city)] = distance

def get_distance(city: str, destination: str) -> int:
  return routes[(city, destination)]


for line in inputdata.strip().splitlines():
  a, _, b, _, distance = line.split(" ")
  add_city(a, b, int(distance))

for route in permutations(cities):
  route_distance = 0
  start = route[0]
  for stop in route[1:]:
    route_distance += get_distance(start, stop)
    start = stop

  distances.add(route_distance)

print()
print("SHORTEST:", min(distances))
print("LONGEST:", max(distances))

t2 = time.perf_counter()
print(f"Execution time: {t2 - t1:0.4f} seconds")
