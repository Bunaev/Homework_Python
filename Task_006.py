# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

s = int(input('Ввежите сумму искомых чисел: '))
p = int(input('Ввежите произведение искомых чисел: '))
num1 = 0
num2 = 0
for i in range(s):
    for k in range(p):
        if s == i + k and p == i * k:
            num1 = i
            num2 = k
if num1 > 0 and num2 > 0:
    print(f'Числа, которые Вы ищете - {num1} и {num2}')
else:
    print('Числа не найдены. Проверьте введенные значения.')