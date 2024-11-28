# def solve(a, b):
#     return a**b
    
# result = solve(2, 4)
# print(result)

def display_person(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


display_person(Name="Amir Khan", Age="45")