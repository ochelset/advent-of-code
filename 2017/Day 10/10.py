"""
Suppose we instead only had a circular list containing five elements, 0, 1, 2, 3, 4, and were given input lengths of 3, 4, 1, 5.

    The list begins as [0] 1 2 3 4 (where square brackets indicate the current position).
    The first length, 3, selects ([0] 1 2) 3 4 (where parentheses indicate the sublist to be reversed).
    After reversing that section (0 1 2 into 2 1 0), we get ([2] 1 0) 3 4.
    Then, the current position moves forward by the length, 3, plus the skip size, 0: 2 1 0 [3] 4. Finally, the skip size increases to 1.

    The second length, 4, selects a section which wraps: 2 1) 0 ([3] 4.
    The sublist 3 4 2 1 is reversed to form 1 2 4 3: 4 3) 0 ([1] 2.
    The current position moves forward by the length plus the skip size, a total of 5, causing it not to move because it wraps around: 4 3 0 [1] 2. The skip size increases to 2.

    The third length, 1, selects a sublist of a single element, and so reversing it has no effect.
    The current position moves forward by the length (1) plus the skip size (2): 4 [3] 0 1 2. The skip size increases to 3.

    The fourth length, 5, selects every element starting with the second: 4) ([3] 0 1 2. Reversing this sublist (3 0 1 2 4 into 4 2 1 0 3) produces: 3) ([4] 2 1 0.
    Finally, the current position moves forward by 8: 3 4 2 1 [0]. The skip size increases to 4.

In this example, the first two numbers in the list end up being 3 and 4; to check the process, you can multiply them together to produce 12.

******************************************************************************************

The logic you've constructed forms a single round of the Knot Hash algorithm; running the full thing requires many of these rounds.
Some input and output processing is also required.

First, from now on, your input should be taken not as a list of numbers, but as a string of bytes instead. Unless otherwise specified,
convert characters to bytes using their ASCII codes. This will allow you to handle arbitrary ASCII strings, and it also ensures that your
input lengths are never larger than 255. For example, if you are given 1,2,3, you should convert it to the ASCII codes for each
character: 49,44,50,44,51.

Once you have determined the sequence of lengths to use, add the following lengths to the end of the sequence: 17, 31, 73, 47, 23.
For example, if you are given 1,2,3, your final sequence of lengths should be 49,44,50,44,51,17,31,73,47,23 (the ASCII codes from the
input string combined with the standard length suffix values).

Second, instead of merely running one round like you did above, run a total of 64 rounds, using the same length sequence in each round.
The current position and skip size should be preserved between rounds. For example, if the previous example was your first round, you
would start your second round with the same length sequence (3, 4, 1, 5, 17, 31, 73, 47, 23, now assuming they came from ASCII codes
and include the suffix), but start with the previous round's current position (4) and skip size (4).

Once the rounds are complete, you will be left with the numbers from 0 to 255 in some order, called the sparse hash. Your next task is
to reduce these to a list of only 16 numbers called the dense hash. To do this, use numeric bitwise XOR to combine each consecutive block
of 16 numbers in the sparse hash (there are 16 such blocks in a list of 256 numbers). So, the first element in the dense hash is the first
sixteen elements of the sparse hash XOR'd together, the second element in the dense hash is the second sixteen elements of the sparse hash
XOR'd together, etc.

For example, if the first sixteen elements of your sparse hash are as shown below, and the XOR operator is ^, you would calculate the first
output number like this:

65 ^ 27 ^ 9 ^ 1 ^ 4 ^ 3 ^ 40 ^ 50 ^ 91 ^ 7 ^ 6 ^ 0 ^ 2 ^ 5 ^ 68 ^ 22 = 64

Perform this operation on each of the sixteen blocks of sixteen numbers in your sparse hash to determine the sixteen numbers in your dense hash.

Finally, the standard way to represent a Knot Hash is as a single hexadecimal string; the final output is the dense hash in hexadecimal notation.
Because each number in your dense hash will be between 0 and 255 (inclusive), always represent each number as two hexadecimal digits (including a
leading zero as necessary). So, if your first three numbers are 64, 7, 255, they correspond to the hexadecimal numbers 40, 07, ff, and so the
first six characters of the hash would be 4007ff. Because every Knot Hash is sixteen such numbers, the hexadecimal representation is always 32
hexadecimal digits (0-f) long.

Here are some example hashes:

    The empty string becomes a2582a3a0e66e6e86e3812dcb672a272.
    AoC 2017 becomes 33efeb34ea91902bb2f59c9920caa6cd.
    1,2,3 becomes 3efbe78a8d82f29979031a4aa0b16a9d.
    1,2,4 becomes 63960835bcdc130f0b66d7ff4f6a5a8e.

Treating your puzzle input as a string of ASCII characters, what is the Knot Hash of your puzzle input? Ignore any leading or trailing whitespace you might encounter.
"""
data = [x for x in range(256)]
data = [x for x in range(5)]
input_lengths = [206,63,255,131,65,80,238,157,254,24,133,2,16,0,1,3]
input_lengths = [3,4,1,5]

pos = 0
skip_size = 0

def pick(items, pos, length):
    result = items[:]
    item_length = len(items)

    picked = []
    for i in range(pos, pos+length):
        x = i % item_length
        picked.append(items[x])

    picked.reverse()

    for i in range(pos, pos+length):
        x = i % item_length
        result[x] = picked[i - pos]

    return result

#print(data)
#print()

while input_lengths:
    length = input_lengths.pop(0)
    #ranges = data[:pos] + data[pos:pos+length][::-1] + data[pos+length:] #pick/wrap and rebuild
    #print("> PICK", pos, length, data)
    data = pick(data, pos, length)

    pos += length + skip_size
    skip_size += 1

    #print(">", data)
    #print("pos:", pos, "skip size:", skip_size)
    #input()

print("Part 1:", data[0] * data[1])

data = [x for x in range(256)]
#data = [x for x in range(5)]

string = "206,63,255,131,65,80,238,157,254,24,133,2,16,0,1,3"
input_lengths = []
for s in string.strip():
    input_lengths.append(ord(s))
input_lengths += [17, 31, 73, 47, 23]
#data += [17, 31, 73, 47, 23]
#print(input_lengths)
#print(data)

pos = 0
skip_size = 0
for i in range(64):
    lengths = input_lengths[:]
    while lengths:
        length = lengths.pop(0)
        data = pick(data, pos, length)
        pos += length + skip_size
        skip_size += 1
    #print("Round", i+1, data)
    #input_lengths = [3,4,1,5]

dense_hash = []
for i in range(16):
    sparse_hash = data[i*16:i*16+16]

    #print(sparse_hash, len(sparse_hash))
    hash = 0
    for sparse in sparse_hash:
        hash ^= sparse

    char = hex(hash).replace('0x', '')
    if len(char) == 1:
        char = '0' + char
    dense_hash.append(char)

dense_hash = ''.join(dense_hash)
print("Part 2:", dense_hash)
