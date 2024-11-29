
# String methods
# NOTE:  Every string method in Python does not change the original string instead return a new string with the changed attributes

name = "shakAil AhmedA"
name2 = """

My name is Shakil. Shakil wanted to be a Programmer. Shakil is Logical thinker. Shakil like to mentoring people and Shakil is a problem solver

"""

r1 = name.upper() # SHAKIL AHMED
r2 = name.lower() # shakil ahmed
r3 = name.title() # Shakil Ahmed
r4 = name.swapcase() # smaller -> Capital , Capital -> Smaller
r5 = name.capitalize() # Capitalise
r6 = name.casefold()
r7 = name.count('A') # In a string count a how manay time have a specific letter or word
r8 = name2.count("Shakil") # In a string count a how manay time have a specific letter or word
r9 = name.find("k") # give index of specific character


## Format 
# Example:

nam = "Ram"
age = 22
point = 3.89
message = "My name is {0}. My age is {1}. My point is {2} My favorate number is {1} here is {2}".format(nam, age,point,)
# print(message)

str = "This article is written in {}"
print(str.format("Python"))

print("Hello, I am {} years old !".format(18))

print("This is {} {} {} {} {}".format("One", "Two", "Three", "Four", "Five"))






