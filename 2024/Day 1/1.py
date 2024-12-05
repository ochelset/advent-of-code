data = open("input.data").read().strip().splitlines()
datax = """
3   4
4   3
2   5
1   3
3   9
3   3
""".strip().splitlines()

left_nums = []
right_nums = []
for line in data:
    pair = list(map(int, line.split()))
    left_nums.append(pair[0])
    right_nums.append(pair[1])


def part1(left_nums, right_nums):
    left_nums = left_nums[:]
    right_nums = right_nums[:]
    left_nums.sort()
    right_nums.sort()
    distance = 0

    for i in range(len(left_nums)):
        a, b = left_nums[i], right_nums[i]
        distance += abs(a - b)

    print("Part 1:", distance)


def part2(left_nums, right_nums):
    similarity = 0
    for key in left_nums:
        similarity += right_nums.count(key) * key

    print("Part 2:", similarity)


part1(left_nums, right_nums)
part2(left_nums, right_nums)
