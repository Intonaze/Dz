import random
#1
# n = int(input())
# ch = input()
# for i in range(n):
#     print(ch * n)

#2
# chislo = [random.randint(1, 100) for i in range(5)]
# more50 = True
# for i in chislo:
#     if i <= 50:
#         more50 = False
# print(more50)
# print(chislo)

#3
# lst = []
# lst += ['молоко', 'огурцы', 'пиво', 'рыбка']
# lst += ['чай','сахар','сухарики']
# lst.remove('пиво')
# lst.remove('рыбка')
# print(*lst)

#4
# l = [40, 51, 62, 8, 86, 3 , 7, 9, 67, 3, 58]
# n = int(input())
# print('Число есть в списке') if n in l else print('Числа нет в списке')


#5
l = [40, 51, 62, 8, 86, 3 , 7, 9, 67, 3, 58]
print(f'Это число встречается {l.count(int(input()))} раз')