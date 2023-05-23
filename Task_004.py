# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку 
# на два прямоугольника).

n = int(input('Введите количество долек по одной стороне: '))
m = int(input('Введите количество долек по второй стороне: '))
k = int(input('Введите количество долек, которые Вы хотите отломить: '))
while k > n * m:
    print('В шоколадке нет столько долек!')
    k = int(input('Введите количество долек, которые Вы хотите отломить: '))
if k == n * m:
    print('Это все дольки в шоколадке.')
elif k % n == 0 or k % m == 0:
    print('Указанное кол-во долек можно отломить с одной из сторон!')
else:
    print('Указанное количество долек нельзя отломить ни с одной из сторон!')