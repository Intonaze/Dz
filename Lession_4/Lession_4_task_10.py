height = int(input())
width = height * 2 + 1
layer = 0
while layer < height:
    i = '*' * (layer * 2 + 1)
    print(i.center(width))
    layer += 1