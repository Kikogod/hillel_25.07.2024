my_list = [2, 3]

if my_list:
    my_list.insert(0, my_list[-1])
    x = my_list.pop(-1)

print(my_list)

