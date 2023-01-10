import string
password = input()
upper_in, lower_in, digit_in, symbol_in = False, False, False, False
for i in password:
    if i in string.ascii_lowercase:
        lower_in = True
    if i in string.ascii_uppercase:
        upper_in = True
    if i in string.digits:
        digit_in = True
    if i in string.punctuation:
        symbol_in = True
if upper_in and lower_in and digit_in and symbol_in and len(password) >= 12:
    print('Надежный пароль')  
else:
    print('Ненадежный пароль')