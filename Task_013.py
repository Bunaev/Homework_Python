# Напишите программу, которая на вход принимает два числа A и B, и возводит 
# число А в целую степень B с помощью рекурсии.
# Пример:
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def degree_of_number(a, b):
    if b > 0:
        return a*degree_of_number(a, b-1)
    return 1


a = int(input('Введите число А: '))
b = int(input('Введите число В: '))
print(f'Степень {b} числа {a} = {degree_of_number(a,b)}')

