
A = {1,3,5, 7}
B = {1,2,3,4,5}
 

s = {'g', 'e', 'k', 's'}
s.discard("e") # Remove specific value from sets

B.pop() # remove first value of set
# A.clear()

# print(A)


# print(A&B) # Common
# print(A|B) #  A U B -> All values

## Difference
set_A = {10, 20, 30, 40, 80}
set_B = {100, 30, 80, 40, 60}

# A - B = 10, 20
# B - A = 100, 60
# print(set_A.difference(set_B))
# print(set_B.difference(set_A))

# Shortcut 
# print(set_A - set_B)
# print(set_B - set_A)


## Frozen set
animals = frozenset(["cat", "dog", "lion"])
print("cat" in animals) # True
print("apple" in animals) # False





 



