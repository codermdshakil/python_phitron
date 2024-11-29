
#  Lambda
# def doubled(x):
#     return x*2

# using lambda small function
doubled = lambda num : num * 2
squared = lambda num : num * num
r = doubled(44)
r1 = squared(9)

# print(r)
# print(r1)

# function_name = lambda parameters : operation 

sum = lambda x, y : x+y
print(sum(10, 30))

numbers = [1,3,4,22,45,67,88,23,65,76,98]

# doubled_nums = map(doubled, numbers)
doubled_nums = map(lambda x:x*2, numbers)

# print(numbers)
# print(list(doubled_nums))


squared_nums = map(lambda x : x*x, numbers)
print(list(squared_nums))


actors = [
    {'name':'sabana', 'age':65},
    {'name':'sabnoor', 'age':35},
    {'name':'srabonti', 'age':55},
    {'name':'sabila norr', 'age':38},
    {'name':'shaon', 'age':47},
]

# Lambda is function in one line
juniors = filter(lambda actor : actor['age'] < 40, actors)
print(list(juniors))

