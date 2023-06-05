# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств

import random
n = int(input('Введите количество чисел в первом наборе: '))
m = int(input('Введите количество чисел во втором наборе: '))
list_1 = [0]*n
list_2 = [0]*m
for i in range(len(list_1)):
    list_1[i] = int(random.randint(1, 10))
for k in range(len(list_2)):
    list_2[k] = int(random.randint(1, 10))
print(list_1)
print(list_2)
list_1 = set(list_1)
list_2 = set(list_2)
result = list(list_1.intersection(list_2))
for j in range(len(result)):
    print(result[j], end = ',')