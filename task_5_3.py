from itertools import islice, zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Федора']
# tutors = ['Иван', 'Анастасия', 'Петр',]  # Покажет пустую структуру, т.к.
# условие "len(tutors) > len(klasses)" не соблюдается.
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б']

rezult = (i for i in zip_longest(tutors, klasses) if len(tutors) > len(klasses))

print(type(rezult))
print(*islice(rezult, 9))  # Сделали слайс
print(list(islice(rezult, 3)))  # Ещё слайс, но у нас уже пустой список (выдаст: [])
print("*" * 20, "Вариант 2", "*" * 20)
from itertools import islice, zip_longest

# tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Федора']
# klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б']
#
# together = ((tutors[n], klasses[n]) if len(klasses) > n else (tutors[n], None) for n in range(len(tutors)))
#
# print(type(together), *together, sep='\n')
# print(next(together)) # С помощью "next" добились подтверждение исчерпываемости генератора
