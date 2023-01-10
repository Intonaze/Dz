line = input().split()
words = {i: line.count(i) for i in line}
for key in words:
    print(key, words[key])