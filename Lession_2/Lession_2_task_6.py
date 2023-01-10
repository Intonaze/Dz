a = int(input())
b = int(input())
c = input()
if c in ['/', 'div', 'mod'] and b == 0:
    print('Нельзя делить на ноль')
elif c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    print(a / b)
elif c == 'pow':
    print(a ** b)
elif c == 'mod':
    print(a % b)
elif c == 'div':
    print(a // b)
else:
    print('Неизвестно')