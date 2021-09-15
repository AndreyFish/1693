my_list = [1, 2, 3, 4, 5, 6]
# new_1 = {n:n ** 3 for n in range(1, 11)}
# print(new_1)
new_1 = {k: n ** 3 for n, k in zip(range(1, 11), "sdfghjk")}
print(new_1)