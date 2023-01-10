import string

def k_isalpha(s: str) -> bool:
    alpha = True
    for i in s:
        if i not in string.ascii_letters:
            alpha = False
    return alpha


def k_islower(s: str) -> bool:
    lower = True
    for i in s:
        if i in string.ascii_uppercase:
            lower = False
    letter = False
    for i in s:
        if i in string.ascii_letters:
            letter = True
    return lower and letter


def k_istitle(s: str) -> bool:
    title = True
    for i in s.split():
        if i[0] not in string.ascii_uppercase:
            title = False
        for j in range(1, len(i)):
            if i[j] not in string.ascii_lowercase:
                title = False
    return title


def k_upper(s: str) -> str:
    new_s = ''
    for i in s:
        if 97 <= ord(i) <= 122:
            new_s += chr(ord(i) - 32)
        else:
            new_s += i
    return new_s


def k_endswith(s: str, substring: str) -> bool:
    if s[len(s) - len(substring):] == substring:
        return True
    else:
        return False


def k_count(s: str, substring: str) -> int:
    cnt = 0
    for i in range(len(s) - len(substring) + 1):
        if s[i: i + len(substring)] == substring:
            cnt += 1
    return cnt

def k_strip(s: str) -> str:
    i = 0
    while s[i] == ' ' or s[i] == '\n' or s[i] == '\t':
        i += 1
    else:
        s = s[i:]
    print(s)
    i = -1
    while s[i] == ' ' or s[i] == '\n' or s[i] == '\t':
        i -= 1
    else:
        s = s[:len(s) + i + 1]
    return s


def k_replace(s: str, oldvalue: str, newvalue: str, count: int) -> str:
    for j in range(count):
        for i in range(len(s) - len(oldvalue) + 1):
            if s[i: i + len(oldvalue)] == oldvalue:
                s = s[:i] + newvalue + s[i + len(oldvalue):]
                break
    return s
 
 

print(0,k_strip('SsS'), 0, sep='')
print(0,'SsS'.strip(), 0, sep='')