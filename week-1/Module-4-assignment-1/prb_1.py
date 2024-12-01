
# take input string
s = input()

# inisialise variable
balance = 0 
result = [] 
start = 0 

for i in range(len(s)):
    
    if s[i] == 'L':   
        balance += 1
    elif s[i] == 'R':   
        balance -= 1
        
    if balance == 0:  
        # append substring to result list
        result.append(s[start:i + 1])   
        start = i + 1   


# print output
# result length is substring 
print(len(result)) 

# print substrings
for substring in result: 
    print(substring)


    
     





