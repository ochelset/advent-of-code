"""
--- Day 6: Probably a Fire Hazard ---
Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

After following the instructions, how many lights are lit?

Your puzzle answer was 400410.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

turn on 0,0 through 0,0 would increase the total brightness by 1.
toggle 0,0 through 999,999 would increase the total brightness by 2000000.

"""

from PIL import Image

testdata = """
turn on 0,0 through 999,999
toggle 0,0 through 999,0
turn off 100,100 through 200,200
""".strip().split("\n")

WIDTH = 1000
lights = WIDTH*WIDTH*[0]
brightness = WIDTH*WIDTH*[0]

#instructions = testdata
instructions = open("input.data").read().strip().split("\n")

def pixel(n: int) -> str:
    return '.' if n else ' '

def render():
    img = Image.new('RGB', (WIDTH, WIDTH), color=(0, 0, 0))
    pixels = img.load()

    y = 0
    while y < WIDTH:
        start = y * WIDTH
        for x in range(WIDTH):
            #pixels[x, y] = (255, 255, 0) if lights[start+x] == 1 else (0, 0, 0)
            pixels[x, y] = (brightness[start + x], brightness[start + x], 0)
        y += 1

    img.save("result.png")

def pos(p: str) -> tuple:
    x, y = [int(n) for n in p.split(",")]
    return (x, y)

def interpret(command: str) -> tuple:
    action = command.split(' ', 1)[0]
    parts = command.split(' ')
    state = ''

    if action == 'turn':
        state = parts[1]
    start = pos(parts[-3])
    end = pos(parts[-1])
    return (action, state, start, end)

def turn(state: str, start: tuple, end: tuple):
    for y in range(start[1], end[1]+1):
        for x in range(start[0], end[0]+1):
            pos = (y * WIDTH) + x
            lights[pos] = 1 if state == 'on' else 0
            brightness[pos] = brightness[pos] + (1 if state == 'on' else -1)
            if brightness[pos] < 0:
                brightness[pos] = 0

def toggle(start: int, end: int):
    for y in range(start[1], end[1]+1):
        for x in range(start[0], end[0]+1):
            pos = (y * WIDTH) + x
            lights[pos] = 0 if lights[pos] else 1
            brightness[pos] += 2

for instruction in instructions:
    action, state, start, end = interpret(instruction)
    if action == "turn":
        turn(state, start, end)
    if action == "toggle":
        toggle(start, end)

render()

print(lights[:2000])
print(brightness[:2000])
print(len(list(filter(lambda x: x == 1, lights))))
print(sum(brightness))
