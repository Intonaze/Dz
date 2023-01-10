email = input()

if '@' not in email:
    print("Введите адрес со знаком '@'")
elif len(email.split('@')[0]) < 2:
    print('Слишком короткое имя')
elif '.' not in (domen := email.split('@')[1]):
    print('Неверное доменное имя')
elif domen.split('.')[0] == '' or domen.split('.')[1] == '':
    print('Неверное доменное имя')
else:
    print('Адрес верный')
