
fruits = ['apple', 'orange', 'banana', 'cherry', 'banana']

fruits.append('Pineapple')
fruits.insert(2, 'Ami ane bomu')
# fruits.pop() # pop element from list last element
# fruits.reverse() # reverse list
# fols = fruits.copy() # copy list

total_count = fruits.count('banana') # count how many times have banana
# print(total_count)
index_cherry = fruits.index('cherry') # return index o argument
# print(index_cherry)

fruits.sort() # sort list based on word first letter

# fruits.clear() # clear all elements

fruits.remove('banana') # last matched value remove
print(fruits)


## Extent - join two list 
foods = ['rice', 'joss', 'water']
extra_food = ['dal', 'chicken']
foods.extend(extra_food)
print(foods)




"""
Summary
----------

* append('value') - add value in last of list
* insert(x_index, value) - value to specific position
* count('banana') - count how many time have this value in list
* clear() - clear list
* copy() - shallow copy
* sort() - based on
* reverse() - reverse list
* remove('banana') - if in list banana has two time then last banana value remove 
* pop() - remove last element
* extent() - join two list


"""


 

