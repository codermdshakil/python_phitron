
# Problem Link: https://atcoder.jp/contests/arc087/tasks/arc087_a 

from collections import Counter

def min_item_remove_to_good_sequence(n, my_list):
    
    # Count frequencies of each element in the array
    frequency = Counter(my_list)
    
    # store min items to remove
    remove = 0
    
    for x, count in frequency.items():
        
        if count > x:
            
            remove += count - x
            
        elif count < x:
            remove += count
    
    return remove


# take number input
n = int(input())

# get my_list elements   
my_list = list(map(int, input().split()))   

# print output
print(min_item_remove_to_good_sequence(n, my_list))

    
    
    
