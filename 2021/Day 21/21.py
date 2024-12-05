# Player 1 starting position: 6
# Player 2 starting position: 8

player1 = [6, 0]
player2 = [8, 0]

index = 1
def roll_dice() -> int:
    global index
    index += 3
    dice = 0
    for i in range(index-3, index):
        dice += i % 100
    return dice

def move(player):
    player[0] = (player[0] + roll_dice()) % 10
    player[1] += player[0]

while True:
    move(player1)
    if player1[1] >= 1000:
        break

    move(player2)
    if player2[1] >= 1000:
        break

print("Part 1:", min(player1[1], player2[1]) * (index-1))
