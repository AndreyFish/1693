def odd_nums(num):
    # for num in range(1, num + 1, 2): # Список не чётных чисел,
    # каждому последующему числу прибавляется 1 с шагом 2.
    for num in range(0, num + 1, 2): # Список чётных чисел, если с нуля
        yield num


for i in odd_nums(15): # От 1 до 15
    print(i)