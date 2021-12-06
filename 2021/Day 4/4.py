"""

"""

inputdata = open("input.data").read().splitlines()

numbers = inputdata.pop(0).split(",")
boards = []

# find boards
inputdata.pop(0)
board = []
for line in inputdata:
    line = line.strip().replace("  ", " ")
    if line == "":
        boards.append(board)
        board = []
        continue

    board.append(list(map(lambda x: [int(x), " "], line.split(" "))))
boards.append(board)

#

def render(board: []):
    for row in board:
        print(row)
    print()

def check_boards(number: int) -> []:
    winners = set()
    for j in range(len(boards)):
        board = boards[j]
        if not board:
            continue
        for i in range(len(board)):
            row = list(map(lambda x: [x[0], "*" if x[0] == number else x[1]], board[i]))
            board[i] = row

            if len(list(filter(lambda x: x[1] == "*", row))) == 5:
                winners.add(j)
                break

            for k in range(5):
                col = []
                for row in board:
                    col.append(row[k])

                if len(list(filter(lambda x: x[1] == "*", col))) == 5:
                    winners.add(j)
                    break

    return list(winners)

def sum_unmarked(board: []) -> int:
    result = 0
    for row in board:
        result += sum(list(map(lambda x: x[0] if x[1] == " " else 0, row)))
    return result

for number in numbers:
    winners = check_boards(int(number))
    for winner in winners:
        #print("Winner:", number)
        board = boards[winner]
        #render(board)

        unmarked_sum = sum_unmarked(board)
        print("Winner on", number, "- Sum unmarked:", unmarked_sum, unmarked_sum * int(number))

    for winner in winners:
        boards[winner] = None
