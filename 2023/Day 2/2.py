import re

data = open("input.data").read().strip().split("\n")

test_data = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".strip().split("\n")

xdata = test_data

result_1 = 0

def sum_up(play):
    valid = True
    round = play.strip().split(";")
    for cubes in round:
        game = { 'red': 12, 'green': 13, 'blue': 14 }
        for cube in cubes.split(","):
            amount, color = cube.strip().split(" ")
            #print(amount, color)
            game[color] -= int(amount)
        #print([x for x in game.values()])
        #print("--------")

        for x in game.values():
            if x < 0:
                #print("X", [x for x in game.values()])
                return False

        #print("+", [x for x in game.values()])
    return True

for game in data:
    game = game[4:]
    id, game = game.split(':')
    if sum_up(game):
        result_1 += int(id)
print("Part 1:", result_1)

test_data = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".strip().split("\n")

xdata = test_data
result_2 = 0

for game in data:
    #print("New round")
    game = game[4:]
    id, play = game.split(':')

    round = play.strip().split(";")
    game = { 'red': 0, 'green': 0, 'blue': 0 }
    for cubes in round:
        #print(cubes)
        for cube in cubes.split(","):
            amount, color = cube.strip().split(" ")
            game[color] = max(int(amount), game[color])


    power = 1
    for x in game.values():
        power *= x

    result_2 += power

print("Part 2:", result_2)
