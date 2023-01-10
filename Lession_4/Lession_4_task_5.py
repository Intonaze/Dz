products = {'хлеб': 100, 
            'молоко':120, 
            'огурцы': 60, 
            'апельсины': 450}
thing = input()
total = 0
while thing != 'EXIT':
    total += products[thing]
    thing = input()
print(total)