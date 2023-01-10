import random

chislo = [random.randint(1, 100) for i in range(5)]
more50 = True
for i in chislo:
    if i <= 50:
        more50 = False
print(more50)