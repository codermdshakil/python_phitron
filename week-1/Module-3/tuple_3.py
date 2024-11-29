
# Tuple
# tuple start with () this brackets
# in tuple we can use tuple methods 
# use can access tuple like list
# tuple is immutable

# Speciallity of tuple is
#

def multiple():
    return 3, 5
# print(multiple())

things = "Water Bottol", "Hand Wash", "Pen", "Paper", "Phone", "Book"

# print(things)
# print(things[0:4])
# print(things[3:])
# print(things[::-1])

if 'Paper' in things:
    print("YES")

for item in things:
    print(item)
    


numbers = ([3,4,5,6], [10, 30, 2,44,34])

# using common sense modify tuple
numbers[0][3] = 500
# print(numbers)



"""
### Speciality of tuples:
1. Immutable - that means we can't add, remove, modify, Fixed data
2. Faster performance
3. Memory efficiency
4. Tuple works in fixed data like months, weeks



When to Use a Tuple Over a List ?

When you want read-only data.
When you need a hashable object for sets or dictionary keys.
When performance or memory efficiency is critical.


"""



"""

Summary Table List VS Tuple

Feature 	    List    	                    Tuple
Mutability	    Mutable 	                    Immutable
Syntax	        []	                            ()
Performance	    Slower	                        Faster
Methods	        Many (e.g., append())	        Few (count(), index())
Use Case	    Dynamic data	                Fixed, constant data
Memory Usage	Higher	                        Lower
Hashable	    No	                            Yes (if items are hashable)


"""




