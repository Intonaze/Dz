string = input()
new_string = ''
cnt = 0
i = 0
while i < len(string):
    if cnt == 0:
        new_string += string[i]
        cnt +=1
    elif string[i] == new_string[-1]:
        cnt += 1
    else:
        new_string += str(cnt)
        new_string += string[i]
        cnt = 1
    i += 1
new_string += str(cnt)
print(new_string)
