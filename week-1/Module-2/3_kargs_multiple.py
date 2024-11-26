

def full_name(first, last):
    name = f"Full name is : {first} {last}"
    return name

## sent arguments order wise
# name = full_name('Shakil', 'Ahmed')

## sent arguments as what is wish
name = full_name(last="Ahmed", first= 'Shakil')
print(name)

# args  save without parameter value in a tuple
def sum(num1, num2, *numbers):
    result = num1 + num2
    print(numbers) # *numbers =  (30, 20) [take it like args] 
    return result

# r = sum(10, 20, 30, 20, 50, 80, 90, 120)
# print(r)



# arges example with string
def full_name2(first, last, *names):
    name = f"{first} {last}"
    print("Agrs string values : ", names)
    return name

# name1 = full_name2('Shakil', 'Ahmed', 'Noyon', 'Nadim')
# print(name1)







