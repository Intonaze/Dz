def read_last(lines: int, file: str):
    with open(file) as f:
        d = f.readlines()
    return(d[len(d) - lines:])


def longest_words(file: str):
    with open(file, encoding='UTF-8') as f:
        words = f.read().split()
        lenght = list(map(len, words))
    return [i for i in words if len(i) == max(lenght)]


def get_basket_amount(file: str) -> int:
    with open(file, encoding='UTF-8') as f:
        goods = f.read().split('\n')
        summ = 0
        for i in range(len(goods)):
            goods[i] = list(goods[i].split())
            if len(goods[i]) == 3:
                summ += int(goods[i][1]) * int(goods[i][2])
    return summ

