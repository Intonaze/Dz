# myfile = open('hello.py', mode='w')
# myfile.write("print('Hello world!')")
# myfile.close

# 2
# for n in range(1,6):
#     file = open(f'test/test{n}', mode='w')
#     file.write('')
#     file.close()

my_file = open('ex3.txt', mode='w')
for i in range(1, 123456 + 1):
    my_file.write('qwerty, ' * (sum(map(int, str(i))) - 1))
    my_file.write('qwerty\n')
my_file.close