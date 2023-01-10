string_1 = input()
string_2 = input()
if len(string_1) > 1 and len(string_2) > 1:
    print(string_1) if string_1 > string_2 else print(string_2)
else:
    print('ERROR')