temp = 7
time = 0
while temp < 100:
    temp += 1
    time += 2
print(f'Вода закипит через {time // 60} минут, {time % 60} секунд')