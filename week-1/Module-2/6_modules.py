# Using module system we can use one file code everywhere I can use it
# module function we can just take from same folder file

from function import double_it
from sum_function import sum_two_variable

result = double_it(45)
# print(result)

result1 = sum_two_variable(10, 20)
print(result1)



