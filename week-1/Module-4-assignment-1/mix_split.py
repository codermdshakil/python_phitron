
# Problem Link : https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/S?fbclid=IwAR1qi6o8WBDOrdzcZ--U5YO_40SSQmmLbZ8jggB6CFIRqog1ukVL_Z2wK2s

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


    
     





