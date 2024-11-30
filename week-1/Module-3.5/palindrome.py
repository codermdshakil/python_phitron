# Input the number of elements
n = int(input())

# Input the list of numbers
my_list = list(map(int, input().split()))

# Check if the list is equal to its reversed version
if my_list == my_list[::-1]:
    print("YES")
else:
    print("NO")
