n = int(input("Введите целое число: "))
print(*[num for num in range(1, n + 1, 2)])  # odd
# print(*(num for num in range(0, n + 1, 2)))  # even
