
## Set data structure 
# Sets create using {}
# Set stored - Unique items 
# Unordered collection of  
# Mutable - add, remove but we can't modify a specific index value
# Unindexed 

## When set uses :
# 1. It is primarily used when you need to store non-duplicate elements and perform operations like unions, intersections, and differences efficiently.



#  list - []
#  tuple - ()
#  set  - {}


numbers = [12, 56, 98, 56, 12, 6, 98]
# print(numbers)

# using set we can create set 
numbers_set = set(numbers)
# print(numbers_set)
numbers_set.add(55) 
# print(numbers_set)
numbers_set.remove(6)
print(numbers_set)


for item in numbers_set:
    print(item)
    
if 98 in numbers_set:
    print("YES")
else:
    print("NO")
    
    









