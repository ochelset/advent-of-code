testdata = """
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
""".strip().split("\n")

def assess_allergens(data: list):
    wordmap = {}
    wordset = set()

    for line in data:
        words, allergens = line[:-1].split(" (contains ")
        words = words.split(" ")
        allergens = allergens.split(", ")
        wordset.update(words)

        for allergen in allergens:
            if not allergen in wordmap:
                wordmap[allergen] = set(words)
            else:
                wordmap[allergen] = set(wordmap[allergen]).intersection(words)

    allergen_words = set()
    for key in wordmap.keys():
        allergen_words.update(wordmap[key])

    wordset = wordset.difference(allergen_words)
    counter = 0
    for line in data:
        words = line[:-1].split(" (contains ")[0].split(" ")
        counter += len(wordset.intersection(words))

    print("Part 1:", counter)

    canonical = [(n, wordmap[n]) for n in wordmap.keys()]
    for index in range(len(canonical)):
        allergen = canonical[index]
        for i, compare_to_allergen in enumerate(canonical):
            if set(allergen[1]).difference(compare_to_allergen[1]):
                allergen = (allergen[0], set(allergen[1]).difference(compare_to_allergen[1]))
                canonical[index] = allergen
                allergen = canonical[index]

    canonical = sorted(canonical)
    output = []
    for allergen in canonical:
        output.append(allergen[1].pop())

    print("Part 2:", ",".join(output))

data = open("input.data").read().strip().split("\n")

#assess_allergens(testdata)
assess_allergens(data)