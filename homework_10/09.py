nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
new_list = []
[[[new_list.append(j) for j in k] for k in i] for i in nice_list]
print(new_list)
