
## Dictionary (python) Or Object(Js)
# key value pair
# object
# hastable
# mutable

person = {
    
    # 'key' = 'value'
    'name' : 'Shakil Ahmed',
    'age':19,
    'Job':"Finance Manager",
    'Job1':"Tuitor",
    'salary': 15000
}

# print(person['name']) # name
# print(person.keys()) # keys
# print(person.values()) # all values
# del person['age'] # delete age
# Modify
# person['name'] = "Jani na"

# print dictionary keys and values  [special]
for key, value in person.items():
    print(key, " " ,value)
    