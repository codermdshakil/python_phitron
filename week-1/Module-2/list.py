
# list, array, collection is same (simple turms)

# index    0   1   2   3    4  5   6   7    8  9
numbers = [45, 56, 12, 89, 87, 32, 84, 59, 46, 93]
# index    -10  -9 -8 -7  -6   -5  -4  -3  -2  -1


## list (start : end)
# print(numbers[2:6]) # print value from index to before 6 index not including  index 6
# print(numbers[1:7])


## list(start, end, steps)

# print(numbers[1:7:1])
# print(numbers[1:7:2]) # 1 3 5 7 it work like this

print(numbers[7:2:-1]) # one step
print(numbers[7:2:-2]) # two step


# start with 4 index to end
print(numbers[4:])

# start with 0 index to index 7
print(numbers[:7])

# print all values and copy list
print(numbers[:]) # shortcut to copy a list

# reverse list
print(numbers[::-1]) ## shortcut to reverse





