"""
--- Day 15: Science for Hungry People ---
Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right
balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could
use to finish the recipe (your puzzle input) and their properties per teaspoon:

capacity (how well it helps the cookie absorb milk)
durability (how well it keeps the cookie intact when full of milk)
flavor (how tasty it makes the cookie)
texture (how it improves the feel of the cookie)
calories (how many calories it adds to the cookie)
You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce
your results in the future. The total score of a cookie can be found by adding up each of the properties (negative
totals become 0) and then multiplying together everything except calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient
must add up to 100) would result in a cookie with the following properties:

A capacity of 44*-1 + 56*2 = 68
A durability of 44*-2 + 56*3 = 80
A flavor of 44*6 + 56*-2 = 152
A texture of 44*3 + 56*-1 = 76

Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which
happens to be the best score possible given these ingredients. If any properties had produced a negative total, it would
have instead become zero, causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you
can make?
"""

from itertools import combinations, permutations

ingredients = {}

class Cookie:
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int
    recipe: {}

    def __init__(self, recipe: {}):
        self.capacity = 0
        self.durability = 0
        self.flavor = 0
        self.texture = 0
        self.calories = 0
        self.recipe = recipe

        self.calc()

    def __repr__(self):
        return "<Cookie capacity: %s, durability: %s, flavor: %s, texture: %s, calories: %s>" % \
               (self.capacity, self.durability, self.flavor, self.texture, self.calories)

    def calc(self):
        for ingredient, amount in self.recipe.items():
            self.capacity += amount * ingredients[ingredient]["capacity"]
            self.durability += amount * ingredients[ingredient]["durability"]
            self.flavor += amount * ingredients[ingredient]["flavor"]
            self.texture += amount * ingredients[ingredient]["texture"]
            self.calories += amount * ingredients[ingredient]["calories"]

    @property
    def total_score(self) -> int:
        return max(0, self.capacity) * max(0, self.durability) * max(0, self.flavor) * max(0, self.texture)

#
#

def parse(data: str):
    for line in data.strip().splitlines():
        name, properties = line.split(": ")
        ingredient = { "name": name }
        for property in properties.split(", "):
            name, value = property.split(" ")
            ingredient[name] = int(value)

        ingredients[ingredient["name"]] = ingredient

inputdata = open("input.data").read()

TEASPOONS = 100
TARGET_CALORIES = 500

parse(inputdata)

scores = []
targets = []
parts = list(ingredients.keys())

for combo in filter(lambda combo: sum(combo) == TEASPOONS, combinations(range(TEASPOONS), len(parts))):
    for perm in permutations(combo):
        recipe = {}
        for i in range(len(parts)):
            recipe[parts[i]] = perm[i]

        cookie = Cookie(recipe)
        scores.append(cookie)

        if cookie.calories == TARGET_CALORIES:
            targets.append(cookie)

cookie = max(scores, key=lambda cookie: cookie.total_score)
print("Part 1:", cookie.total_score)

cookie = max(targets, key=lambda cookie: cookie.total_score)
print("Part 2:", cookie.total_score)
