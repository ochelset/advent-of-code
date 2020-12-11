from functools import lru_cache

testdata = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

class SeatMap:
    seat_map = {}
    width = 0
    height = 0

    def __init__(self, data: str):
        for y, line in enumerate(data.strip().split("\n")):
            for x, spot in enumerate(line):
                if spot != ".":
                    self.seat_map[(x, y)] = spot

        self.width = x + 1
        self.height = y + 1


    @property
    def occupied(self) -> int:
        counter = 0
        for seat in self.seat_map.keys():
            counter += 1 if self.seat_map[seat] == "#" else 0

        return counter


    def render(self):
        for y in range(self.height):
            line = []
            for x in range(self.width):
                seat = self.seat_map.get((x, y))
                if not seat:
                    line.append(".")
                else:
                    line.append(seat)

            print("".join(line))

        print()


    def occupied_seats_adjacent(self, x: int, y: int, distance: int) -> int:
        adjacent = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        occupied_adjacents = 0
        for coordinate in adjacent:
            for z in range(1, distance + 1):
                if (x < 0 or x >= self.width or y < 0 or y >= self.height):
                    break

                seat_pos = (x + (coordinate[0] * z), y + (coordinate[1] * z))
                if not seat_pos in self.seat_map:
                    continue
                occupied_adjacents += 1 if self.seat_map[seat_pos] == "#" else 0
                break

        return occupied_adjacents


    def occupy_seats(self, tolerance: int, distance: int = 1) -> bool:
        map_copy = self.seat_map.copy()
        modified = False
        for y in range(self.height):
            for x in range(self.width):
                seat = self.seat_map.get((x, y))
                if not seat:
                    continue

                occupied_adjacents = self.occupied_seats_adjacent(x, y, distance)
                if seat == "L" and occupied_adjacents == 0:
                    map_copy[(x, y)] = "#"
                    modified = True

                elif seat == "#" and occupied_adjacents >= tolerance:
                    map_copy[(x, y)] = "L"
                    modified = True

        if modified:
            self.seat_map = map_copy.copy()

        return modified

#
#

data = open("input.data").read()

def part1():
    seat_map = SeatMap(data)

    while seat_map.occupy_seats(tolerance=4):
        continue

    print("Part 1:", seat_map.occupied)


def part2():
    seat_map = SeatMap(data)

    while seat_map.occupy_seats(tolerance=5, distance=200):
        continue

    print("Part 2:", seat_map.occupied)

part1()
part2()