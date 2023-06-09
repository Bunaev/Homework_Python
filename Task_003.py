# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме 
# последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

ticket = int(input('Введите шестизначный номер Вашего билета: '))
while ticket < 100000 or ticket > 999999:
    print('Введено неверное число')
    ticket = int(input('Введите шестизначный номер Вашего билета: '))
side_a = int(ticket/1000)
side_b = int(ticket%1000)
sum_a = int(side_a%10) + int((side_a/10)%10) + int((side_a/100)%10)
sum_b = int(side_b%10) + int((side_b/10)%10) + int((side_b/100)%10)
if int(sum_a) == int(sum_b):
    print('Поздравляем!Ваш билет - СЧАСТЛИВЫЙ!')
else:
    print('Увы. Повезёт в другой раз')
