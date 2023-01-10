class Barbie():
    def __init__(self, appearance, mentality, character) -> None:
        self.appearance = appearance
        self.mentality = mentality
        self.character = character
    

    def GetAttributes(self):
        print(
f'''Аттрибуты барби:
    Внешний вид: {self.appearance}
    Ментальность: {self.mentality}
    Характер: {self.character}''')

class BarbieDoll(Barbie):
    def __init__(self, appearance, mentality, character, material, production, color, details) -> None:
        super().__init__(appearance, mentality, character)
        self.material = material
        self.production = production
        self.color = color
        self.details = details

    def GetAttributes(self):
        print(
f'''Аттрибуты куклы барби:
    Внешний вид: {self.appearance}
    Ментальность: {self.mentality}
    Характер: {self.character}
    Материал: {self.material}
    Тип производства: {self.production}
    Цвет: {self.color}
    Детали: {self.details}''')

b = BarbieDoll('Кукла', 'Очень хороший и веселый человек', 'Характер общительный', 'Пластик', 'Китай', 'Телесный', 'Родинка на шее')
print(b.mentality)
b.GetAttributes()