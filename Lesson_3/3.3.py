my_list = [1, 2, 4, 5, 1]

ltr = (len(my_list) + 1) // 2


ltr1 = my_list[:ltr]
ltr2 = my_list[ltr:]

result = [ltr1, ltr2]

print(result)


