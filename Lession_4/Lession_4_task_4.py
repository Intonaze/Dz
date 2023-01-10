string = input()
digit = True
i = 0
while digit and i < len(string):
    if string[i] not in '0123456789':
        digit = False
    i += 1
print(digit)