print("=" * 30, 'Рассчёт суммарного расхода ткани', "=" * 30)

from abc import ABC, abstractmethod


class Clothes(ABC):
    result = 0

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        Clothes.result += self.consumption + other.consumption
        return Costume(0)

    def __str__(self):
        res = Clothes.result
        Clothes.result = 0
        return f"{res}"


class Coat(Clothes):
    @property
    def consumption(self):
        return round(self.param / 6.5) + 0.5


class Costume(Clothes):
    @property
    def consumption(self):
        return round((2 * self.param + 0.3) / 100)


coat = Coat(42)
costume = Costume(170)
print(coat + costume + coat)

print("=" * 30, 'Общий подсчёт расхода ткани', "=" * 30)

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def payment(self):
        pass

    def __add__(self, other):
        return self.payment + other.payment


class Coat(Clothes):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            print('На детей не шьём. Начнём с сорокового.')
            self.__size = 40
        elif size > 58:
            print('Не многовато ли? 58 - МАКСИМУМб для него и посчитаем')
            self.__size = 58
        else:
            self.__size = size

    @property
    def payment(self):
        return self.__size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 100:
            print('На детей не шьём.')
            self.__height = 150
        elif height > 240:
            print('Не многовато ли? 240 - МАКСИМУМ, для него и посчитаем')
            self.__height = 240
        else:
            self.__height = height

    @property
    def payment(self):
        return 2 * (self.__height / 100) + 0.3


coat_1 = Coat(int(input('Введите размер пальто для рассчёта:')))
print(f'Вам потребуется {coat_1.payment:.2f} метров ткани на пальто {coat_1.size} размера')
costume_1 = Costume(int(input('Введите рост для костюма для рассчёта (как обычно, в сантиметрах:')))
print(f'Вам потребуется {costume_1.payment:2f} метров ткани на костюм {costume_1.height} роста')
print(f'Всего вам потребуется {coat_1 + costume_1:.2f} метров ткани')
