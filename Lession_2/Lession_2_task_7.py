a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
if a == b:
    print('a делится на b и b делится на a')
elif a % b == 0:
    print('a делится на b')
elif b % a == 0:
    print('b делится на a')
else:
    print('Числа не делятся друг на друга нацело')