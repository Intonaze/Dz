import os

def cleardir(dir: str)-> None:
    for i in os.listdir(path=dir):
        if os.path.isfile(dir + '\\' + i):
            os.remove(dir + '\\' + i)
        elif os.path.isdir(dir + '\\' + i):
            cleardir(dir + '\\' + i)
            os.rmdir(dir + '\\' + i)

while True:
    command = input().split()
    if command[0] == 'ls' and len(command) == 1:
        print(*os.listdir(path="."), sep='\n')
    elif command[0] == 'ls' and len(command) == 2:
        print(*os.listdir(path='.\\' + command[1]), sep='\n')
    elif command[0] == 'cd' and len(command) == 2:
        os.chdir(command[1])
    elif command[0] == 'pwd' and len(command) == 1:
        print(os.getcwd())
    elif command[0] == 'mkdir' and len(command) == 2:
        os.mkdir(command[1])
    elif command[0] == 'touch' and len(command) == 2:
        my_file = open(command[1], "w")
        my_file.write("")
        my_file.close()
    elif command[0] == 'rm' and len(command) == 2:
        if os.path.isfile(command[1]):
            os.remove(command[1])
        elif command[0] == 'rm' and command[1] == '-rf' and len(command) == 2:
            cleardir('.')
            d = os.path.abspath('.')
            os.chdir('..')
            os.rmdir(d)
    else: print('Неизвестная команда')