string = input()
new_string = ''
i = 0
not_in_brackets = True
while i < len(string):
    if not_in_brackets and string[i] not in '\'\"':
        new_string += string[i]
    elif string[i] in '\'\"':
        not_in_brackets = not not_in_brackets
    i += 1
print(new_string)