data = open("input.data").read().strip().split("\n")

test_data = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".strip().split("\n")

def get_map(keyword):
    result = []
    found = False
    for line in data:
        if found and line == '':
            return result

        if not found:
            if line.startswith(keyword):
                found = True
            continue

        ranges = [int(x) for x in line.split(" ")]
        result.append((ranges[1], ranges[1]+ranges[2]-1, ranges[0], ranges[0]+ranges[2]-1, ranges[2]))
    return result

def seed_in_range(seed, seed_range) -> bool:
    return seed >= seed_range[0] and seed <= seed_range[1]

def map_seeds(keys, source, target, value_from=None):
    for key in keys:
        if not key in seed_map:
            seed_map[key] = {}

        value = key
        if value_from and value_from in seed_map[key]:
            value = seed_map[key][value_from]

        mapped = False
        for range_map in source:
            if seed_in_range(value, range_map):
                seed_map[key][target] = abs(range_map[0] - value) + range_map[2]
                mapped = True
                break

        if not mapped:
            seed_map[key][target] = value

def get_keys_for(target):
    return [x[target] for x in seed_map.values()]

xdata = test_data

result_1 = 0
result_2 = None
seed_map = {}
seeds = [int(x) for x in data[0][7:].split(" ")]
seed_to_foil_map = get_map('seed-to-soil')
soil_to_fertilizer = get_map('soil-to-fertilizer')
fertilizer_to_water = get_map('fertilizer-to-water')
water_to_light = get_map('water-to-light')
light_to_temperature = get_map('light-to-temperature')
temperature_to_humidity = get_map('temperature-to-humidity')
humidity_to_location = get_map('humidity-to-location')

map_seeds(seeds, seed_to_foil_map, 'soil')
map_seeds(seeds, soil_to_fertilizer, 'fertilizer', 'soil')
map_seeds(seeds, fertilizer_to_water, 'water', 'fertilizer')
map_seeds(seeds, water_to_light, 'light', 'water')
map_seeds(seeds, light_to_temperature, 'temperature', 'light')
map_seeds(seeds, temperature_to_humidity, 'humidity', 'temperature')
map_seeds(seeds, humidity_to_location, 'location', 'humidity')

print("Part 1:", min(get_keys_for('location')))

xl = """
3880387060 2052152805 97611299
2442736538 3295723734 10591308
3014234548 3058886861 44150293
2722522139 3413370195 153277538
2877652345 3226748198 68975536
678696757 79205913 5515453
3758528684 3103037154 121858376
3648288667 2533118408 110240017
3457871155 4266074310 28892986
2176930761 3905620500 135283057
2312213818 2369019482 56130623
2875799677 3224895530 1852668
2052152805 3780842544 124777956
2598433171 3306315042 56382802
1279041455 278559111 48074772
2964261570 2302916483 49972978
344154771 1539624544 79809331
1030322972 1619433875 248718483
1905012367 1868152358 115533200
105230362 326633883 51970437
4085966662 2880778716 178108145
684212210 1466450827 73173717
919250672 396737705 108684083
868993622 1215278638 50257050
2962757902 2879275048 1503668
1847630888 378604320 18133385
3232700402 4040903557 225170753
2575587736 3390524760 22845435
3977998359 2425150105 107968303
3058384841 3362697844 27826916
789787709 0 79205913
4264074807 2272023994 30892489
3114006964 3594442940 118693438
460824111 202771015 75788096
423964102 1983685558 36860009
2946627881 2352889461 16130021
157200799 505421788 186953972
3486764141 2717750522 161524526
1027934755 692375760 2388217
2453327846 2149764104 122259890
2368344441 2643358425 74392097
0 1407620238 58830589
2654815973 3713136378 67706166
1865764273 117123148 39248094
3086211757 3566647733 27795207
58830589 156371242 46399773
536612207 1265535688 142084550
757385927 84721366 32401782
1327116227 694763977 520514661
""".strip().split("\n")
Mi = None
Ma = None
for line in xl:
    line = [int(x) for x in line.split(" ")]
    mi, ma = (min(line), max(line))
    if Mi == None or mi < Mi:
        Mi = mi
    if Ma == None or ma > Ma:
        Ma = ma

for i in range(Mi, Ma):
    x = i
print("Done")


for i in range(0, len(seeds), 2):
    print("New range", seeds[i], seeds[i]+seeds[i+1])
    seed_map = {}
    seed_range = range(seeds[i], seeds[i]+seeds[i+1])
    print(len(seed_range))
    for sr in seed_range:
        if sr % 10000 == 0:
            print(sr)
        map_seeds([sr], seed_to_foil_map, 'soil')
        map_seeds([sr], soil_to_fertilizer, 'fertilizer', 'soil')
        map_seeds([sr], fertilizer_to_water, 'water', 'fertilizer')
        map_seeds([sr], water_to_light, 'light', 'water')
        map_seeds([sr], light_to_temperature, 'temperature', 'light')
        map_seeds([sr], temperature_to_humidity, 'humidity', 'temperature')
        map_seeds([sr], humidity_to_location, 'location', 'humidity')

        location = min(get_keys_for('location'))
        if result_2 == None or location < result_2:
            result_2 = location
            print("New low:", location)

print("Part 2:", result_2)