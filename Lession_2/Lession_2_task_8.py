a = int(input())
digit1 = a // 100 % 10
digit2 = a //10 % 10
digit3 = a % 10
if digit1 == digit2 == digit3:
    print('Все цифры одинаковые')
elif digit1 == digit2 or digit1 == digit3 or digit2 == digit3:
    print('Две цифры одинаковые')
else:
    print('Нет одинаковых цифр')