
numbers = [45, 87, 96, 65, 43, 85, 14,26,61, 70]
odds = []
evens = []

for num in numbers:
    if num % 2 == 1 & num % 5 == 0:
        odds.append(num)
    elif num % 2 == 0:
        evens.append(num)


# print(odds)
# print(evens)

## Comprehension
# -----------------

# odd_numbers = [num for num in numbers if num % 2 == 1]
odd_numbers = [num for num in numbers if num % 2 == 1 & num % 5 == 0]



players = ['sakib', 'musfik', 'liton']
ages = [38, 28,34]
age_com = []

for player in players:
    # print('Player : ', player)
    for age in ages:
        # print(player, age)
        age_com.append([player, age])

print(age_com)

age_comb2 = [[player,age] for player in players for age in ages]
print(age_comb2)




