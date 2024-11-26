

## multiple paramter, set default value in function parameter


# set default parameter value in function like num3=0
def sum(num1, num2, num3=0, num4 = 0, num5 = 0):
    result = num1 + num2 + num3
    return result

total = sum(99,11, 44)
# print('Total : ',total)



# multiple numbers of parameter
#  set default parameter value in function using args
def all_sum(num1, num2, *numbers): # * makes tuple
    print(numbers)
    sum = 0
    for num in numbers:
        print(num)
        num = sum + num
    
total = all_sum(45, 46, 54,1,3,44)
print("All total value : ", total)


def do_a_lot(*args):
    print(args)
    
