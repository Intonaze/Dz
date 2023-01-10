layers = int(input())
pyramid = []
start_layer_height = 3
layer_width = 0

# создаем правило увеличения ширины слоя по мере продвижения вниз
width_rule = []
for i in range(2, layers // 2 + 3) :
    width_rule.append(i)
    width_rule.append(i)
if len(width_rule) < layers:
    width_rule.append(i + 1)
width_rule = width_rule[::-1]

# строим пирамиду
layers_pyramid = layers
while layers_pyramid > 0:
    for i in range(start_layer_height):
        pyramid.append('/'+'*' * (layer_width * 2 + 1) + "\\")
        layer_width += 1
    layers_pyramid -= 1
    layer_width += width_rule.pop()
    start_layer_height += 1

# определяем ширину пирамиды
width_global = 0
for i in pyramid:
    if len(i) > width_global:
        width_global = len(i)

# выравнивание пирамиды по ширине
for i in range(len(pyramid)):
    pyramid[i] = pyramid[i].center(width_global)

# вставляем дверь
door_width = (layers // 2) * 2 + 1
door_start = (width_global - door_width) // 2 
for i in range(door_width):
    pyramid[-1 - i] = pyramid[-1 - i][0:door_start] + '|' * door_width + pyramid[-1 - i][door_start + door_width:]

# вставляем ручку
if layers > 3:
    pyramid[-door_width // 2] = pyramid[-door_width // 2][:door_start + door_width - 2] + "$" + pyramid[-door_width // 2][door_start + door_width - 1:]

# печатаем пирамиду
for i in range(len(pyramid)):
    print(pyramid[i])