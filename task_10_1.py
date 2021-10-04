
print("=" * 30, 'Задача_1', "=" * 30)

a = [[0, 7, 7, 0], [5, 7, 3, 1], [8, 8, 8, 8]]
d = [[4, 7, 0, 5], [1, 1, 5, 5], [4, 3, 2, 1]]


class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str, c))


matrix_1 = Matrix(a)
matrix_2 = Matrix(d)
print(f"Matrix 1\n{matrix_1}\n{'-' * 20}")
print(f"Matrix 2\n{matrix_2}\n{'-' * 20}")
print(f"matrix 1 + matrix 2\n{matrix_1 + matrix_2}")

print("=" * 30, 'Вариант решения', "=" * 30)
# import matrix as matrix


class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join('\t'.join([f"{itm:02}" for itm in line]) for line in self.data)

    def __add__(self, other):
        try:
            m = [[int(self.data[line][itm]) + int(other.data[line][itm]) for itm in range(len(self.data[line]))]
                 for line in range(len(self.data))]
            return Matrix(m)
        except IndexError:
            return f'Ошибка размерностей матриц'


m_1 = [[33, 7, -7], [5, 17, 1], [8, -8, 88]]
m_2 = [['4', 7, 5], [1, 5, 5], [4, 3, 2]]

mtrx_1 = Matrix(m_1)
mtrx_2 = Matrix(m_2)
new_m = mtrx_1 + mtrx_2

print(new_m)
# или с вводом значения(вариант ниже)

# string = int(input("Введите количество строк и столбцов матрицы: "))
# columns = string
#
# mtrx_1 = Matrix([[i * j for j in range(string)] for i in range(columns)])
# mtrx_2 = Matrix([[i * j for j in range(string)] for i in range(columns)])
#
# print('First matrix:\n', mtrx_1, end='\n\n')
# print('Second matrix:\n', mtrx_2, end='\n\n')
# print('Total of first and second matrix:\n', mtrx_1 + mtrx_2)

print("=" * 30, 'Вариант решения', "=" * 30)
# zip_longest - решает проблему разноразмерности
# fillvalue=10(0 или 99) - дозаполняет пустой список (10)

from itertools import zip_longest

class Matrix(object):

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n '.join(['\t'.join([str(i) for i in j]) for j in self.matrix]))

    def __add__(self, other):
        return Matrix([map(sum, zip_longest(*t, fillvalue=99))
                       for t in zip_longest(self.matrix, other.matrix, fillvalue=[])])


# m = [[4, 3, 5], [3, 4, 5], [1, 2, -9, 0]]
m = [[4, 3, 5], [3, 4, 5], [1, 2]]
n = [[7, 9, 1], [5, 8, 3], []]

matr_1 = Matrix(m)
matr_2 = Matrix(n)

print(matr_1)
print(matr_1 + matr_2)

print("=" * 30, 'Вариант решения', "=" * 30)

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return'\n'.join(map(lambda  r: '   '.join(map(str, r)), self.matrix)) + '\n'
    def __add__(self, other):
        return  Matrix(map(lambda r_1, r_2: map(lambda x, y: x + y, r_1, r_2), self.matrix, other.matrix))


my_m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
my_m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_m1)
print(my_m2)
s = my_m1 + my_m2
print(s)


