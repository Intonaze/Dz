string = input()
print(string[0:len(string) // 2:2] + string[len(string) // 2:len(string):2])