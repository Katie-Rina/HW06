'''Задача 30:  Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.'''

# a = []
# ai, d, n = int(input('a1 = ')), int(input('d = ')), int(input('n = '))
# a.append(ai)
# for i in range(2, n + 1):
#     ai += d;
#     a.append(ai)
# print(a)

'''Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)'''

import random
some_list = [random.randint(-10, 11) for _ in range(int(input('Размер списка: ')))]
print(some_list)
minn, maxx = int(input('min = ')), int(input('max = '))
for i in range(len(some_list)):
    if minn < some_list[i] < maxx:
        print(i, end=' ')

'''Для введенных строк определите, в какой из них встречается больше всего различных символов, 
отличающихся от контрольного. Выведите эти символы из строки без повторений, 
каждый с новой строки. Если таких строк несколько, выведите символы из любой.

Формат ввода
Вводится контрольный символ, затем количество строк, затем сами строки.
Формат вывода
Выведите подряд без повторений символы из строки, в которой их оказалось больше всего, 
не считая контрольный. Если ни одной не оказалось, выведите -1. Порядок вывода произвольный.

Пример 1
Ввод

E
5
EVERY
MAN
TO
HIS
TASTE

Вывод
RVY

Пример 2
Ввод

A
4
AA
AAA
AAAA
AAAAAA

Вывод
-1   '''



