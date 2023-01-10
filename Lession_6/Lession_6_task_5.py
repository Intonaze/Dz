import random

lst = [random.randint(1, 50) for i in range(random.randint(1, 50))]
print(f'Это число встречается {lst.count(int(input()))} раз')