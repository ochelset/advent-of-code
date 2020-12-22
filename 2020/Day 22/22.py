class Player():

    name: str
    deck: list

    def __init__(self, name: str):
        self.name = name.replace("Player", "").replace(":", "").strip()
        self.deck = []

    def __repr__(self):
        return "<Player %s>" % self.name

    def deal(self) -> int:
        return self.deck.pop(0)

#
#

game = 1
class Combat():

    players: list
    rounds: int
    recursive: bool
    deck_history: list

    def __init__(self):
        global game
        self.game = game
        self.players = []
        self.rounds = 1
        self.recursive = False
        self.deck_history = []
        game += 1

    @property
    def score(self):
        if self.players[0].deck:
            return self.get_score(self.players[0])

        return self.get_score(self.players[1])

    def add_player(self, name: str, cards: list):
        player = Player(name)
        player.deck = [int(n) for n in cards]
        self.players.append(player)

    def play(self, recursive: bool = False):
        self.recursive = recursive

        #print()
        #print("==== Game %s ====" % self.game)
        #print()

        while True:
            #print("-- Round %s (Game %s) --" % (self.rounds, self.game))

            if self.recursive:
                decks = (self.players[0].deck, self.players[1].deck)
                if decks in self.deck_history:
                    self.players[1].deck = []
                    break

                self.deck_history.append((self.players[0].deck[:], self.players[1].deck[:]))

            #print("Player", self.players[0].name + "'s deck:", self.players[0].name, self.players[0].deck)
            #print("Player", self.players[1].name + "'s deck:", self.players[1].name, self.players[1].deck)
            player_one_card = self.players[0].deal()
            player_two_card = self.players[1].deal()
            #print("Player", self.players[0].name, "played:", player_one_card)
            #print("Player", self.players[1].name, "played:", player_two_card)

            player_one_wins = player_one_card > player_two_card

            if recursive:
                if len(self.players[0].deck) >= player_one_card and len(self.players[1].deck) >= player_two_card:
                    #print("Playing a sub-game to determine the winner...")
                    #input()
                    game = Combat()
                    game.add_player(self.players[0].name, self.players[0].deck[:player_one_card])
                    game.add_player(self.players[1].name, self.players[1].deck[:player_two_card])
                    game.play(recursive=True)

                    if game.players[0].deck:
                        player_one_wins = True
                    else:
                        player_one_wins = False

            if player_one_wins:
                #print("Player 1 wins round %s of game %s" % (self.rounds, self.game))
                self.players[0].deck.extend([player_one_card, player_two_card])
            else:
                #print("Player 2 wins round %s of game %s" % (self.rounds, self.game))
                self.players[1].deck.extend([player_two_card, player_one_card])

            #input()

            if not self.players[0].deck or not self.players[1].deck:
                break

            self.rounds += 1

    def get_score(self, player: Player) -> int:
        score = 0
        for i, card in enumerate(player.deck[::-1]):
            score += (i+1) * card
        return score

#
#

testdata = """
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
""".strip().split("\n\n")

data = testdata
data = open("input.data").read().strip().split("\n\n")

def part1():
    game = Combat()
    game.add_player(data[0].split("\n")[0], data[0].split("\n")[1:])
    game.add_player(data[1].split("\n")[0], data[1].split("\n")[1:])
    game.play()
    print("Part 1:", game.score)

def part2():
    game = Combat()
    game.add_player(data[0].split("\n")[0], data[0].split("\n")[1:])
    game.add_player(data[1].split("\n")[0], data[1].split("\n")[1:])
    game.play(recursive=True)
    print("Part 2:", game.score)

part1()
part2()

