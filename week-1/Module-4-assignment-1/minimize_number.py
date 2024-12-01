

# Problem link : https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/P

# take n input
n = int(input())

# take list elements input
my_list = list(map(int, input().split())) 

# counter how many time do operation
count = 0

while all(num % 2 == 0 for num in my_list):
    
    # all my_list elements divided by 2 
    my_list = [num // 2 for num in my_list]
    
    # increment operation 
    count += 1
    
print(count)







 

