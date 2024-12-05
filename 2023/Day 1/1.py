import re

data = open("input.data").read().strip().split("\n")

test_data = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".strip().split("\n")

#data = test_data

def text_to_number(s):
    s = s.replace('zero', '0')
    s = s.replace('one', '1')
    s = s.replace('two', '2')
    s = s.replace('three', '3')
    s = s.replace('four', '4')
    s = s.replace('five', '5')
    s = s.replace('six', '6')
    s = s.replace('seven', '7')
    s = s.replace('eight', '8')
    s = s.replace('nine', '9')
    s = s.replace('sixteen', '16')
    return s

def convert(s):
    i = 0
    word = ''
    result = ''
    for j in range(len(s)):
        word += s[j]
        num = text_to_number(word)
        if num != word:
            result += num
            word = s[j]

    result += word
    #print(s, '<', result)
    return result

##

result_1 = 0
result_2 = 0
for line in data:
    nums = ''.join(filter(str.isdigit, line))
    if nums:
        result_1 += int(nums[0] + nums[-1])

    line2 = convert(line)

    nums = ''.join(filter(str.isdigit, line2))
    print(line, line2, ">", nums[0] + nums[-1])
    result_2 += int(nums[0] + nums[-1])

print("Part 1:", result_1)
print("Part 2:", result_2)
