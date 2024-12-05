"""
For example, if the spinlock were to step 3 times per insert, the circular buffer would begin to evolve
like this (using parentheses to mark the current position after each iteration of the algorithm):

(0), the initial state before any insertions.
0 (1): the spinlock steps forward three times (0, 0, 0), and then inserts the first value, 1, after it. 1 becomes the current position.
0 (2) 1: the spinlock steps forward three times (0, 1, 0), and then inserts the second value, 2, after it. 2 becomes the current position.
0  2 (3) 1: the spinlock steps forward three times (1, 0, 2), and then inserts the third value, 3, after it. 3 becomes the current position.

And so on:

    0  2 (4) 3  1
    0 (5) 2  4  3  1
    0  5  2  4  3 (6) 1
    0  5 (7) 2  4  3  6  1
    0  5  7  2  4  3 (8) 6  1
    0 (9) 5  7  2  4  3  8  6  1

The good news is that you have improved calculations for how to stop the spinlock.
They indicate that you actually need to identify the value after 0 in the current state of the circular buffer.

The bad news is that while you were determining this, the spinlock has just finished inserting its fifty millionth value (50000000).

What is the value after 0 the moment 50000000 is inserted?
"""
data = 363
target = 50000000

if False:
    data = 3
    target = 2017

buffer = [0, 0, 0]
buffer_len = 1

current_pos = 0
value = 1

while value <= target:
    current_pos = (current_pos + data) % buffer_len
    next_pos = current_pos + 1
    if next_pos == 1:
        buffer[1] = value

    value += 1
    buffer_len += 1
    current_pos = next_pos

"""
while value <= target:
    #print("PREV POS", current_pos)
    current_pos = (current_pos + data) % buffer_len
    #print("STEPPED", data, current_pos)

    next_pos = current_pos + 1
    if next_pos >= buffer_len:
        #print("APPEND", value, "AT END")
        buffer.append(value)
    else:
        #print("INSERT", value, "AT", current_pos)
        buffer.insert(next_pos, value)
    value += 1
    buffer_len += 1

    #print("NEXT POS", next_pos)
    current_pos = next_pos
    if value % 10000 == 0:
        print("V+", value)
"""

#print("Part 1:", buffer[current_pos+1])
print("Part 2:", buffer[1])