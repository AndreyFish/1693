class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):  # make_order - нарезает на ряды
        return '\n'.join(['♠︎' * rows for _ in range(self.nums // rows)]) + '\n' + '♠︎' * (self.nums % rows)

    def __str__(self):
        return f"{self.nums}"

    # сумма ячеек
    def __add__(self, other):
        print("Sum of cell is:")
        return Cell(self.nums + other.nums)

    # вычитание ячеек
    def __sub__(self, other):
        print("Substraction of cell is:")
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else "Ячеек в первой клетке меньше второй, вычитание невозможно!"

    # умножение ячеек
    def __mul__(self, other):
        print("Multiply of cell is:")
        return Cell(self.nums * other.nums)

    # целочисленное
    def __floordiv__(self, other):
        print("Truediv of cell is:")
        return Cell(self.nums // other.nums)


cell_1 = Cell(39)  # если cell_1 будет меньше cell_2 - сработает else
cell_2 = Cell(24)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(7))
