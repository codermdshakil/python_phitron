
num_lists = [1,6,0]
copy_list = []


for n in num_lists:
    copy_list.append(n)

copy_list.reverse()


if num_lists == copy_list:
    print("YES")
else:
    print("NO")
    