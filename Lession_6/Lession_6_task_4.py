import random

lst = [random.randint(1, 50) for i in range(random.randint(1, 50))]
n = int(input('Введите число: '))
print('Число есть в списке') if n in lst else print('Числа нет в списке')