# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка содержит число X

import random

n = int(input("Введите количество чисел: "))
x = int(input("Введите число Х: "))
while x <= 0:
    print('Ошибка! Введите число > 0')
    x = int(input("Введите число Х: "))
min_x = 0
tmp = [0] * n
array = [0] * n
for i in range(len(array)):
    array[i] = random.randint(1, 99)
print(array)
for k in range(len(array)):
    if array[k] > x:
        tmp[k] = float(array[k] / x)
    elif array[k] < x:
        tmp[k] = float(x / array[k])
min_x = min(tmp)
for j in range(len(tmp)):
    if tmp[j] == min_x:
        print()
        print(f"Самый близкий по значению элемент к числу {x} находится на позиции № {j+1}, это число - {array[j]}!")
