lines = open("input.data").read().strip().split("\n")

types = dict(A="Rock", B="Paper", C="Scissors", X="Rock", Y="Paper", Z="Scissors")

points = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

score = 0


def play(mine: str, opponents: str) -> int:
    if mine == "Rock" and opponents == "Scissors":
        return 6
    if mine == "Paper" and opponents == "Rock":
        return 6
    if mine == "Scissors" and opponents == "Paper":
        return 6
    if opponents == mine:
        return 3

    return 0


for line in lines:
    opponent, me = line.split(" ")
    opponent_hand = types[opponent]
    my_hand = types[me]

    score += points[my_hand] + play(my_hand, opponent_hand)

print("Part 1:", score)

score = 0
for line in lines:
    opponent, me = line.split(" ")
    opponent_hand = types[opponent]
    my_hand = opponent_hand

    if me == "X":
        if opponent_hand == "Rock":
            my_hand = "Scissors"
        if opponent_hand == "Paper":
            my_hand = "Rock"
        if opponent_hand == "Scissors":
            my_hand = "Paper"
    if me == "Z":
        if opponent_hand == "Rock":
            my_hand = "Paper"
        if opponent_hand == "Paper":
            my_hand = "Scissors"
        if opponent_hand == "Scissors":
            my_hand = "Rock"

    score += points[my_hand] + play(my_hand, opponent_hand)

print("Part 2:", score)
