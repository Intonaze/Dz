class Pivo():
    def __init__(self, name: str, volume: float, IBU: float):
        self.name = name
        self.volume = volume
        self.IBU = IBU
    
    def Сгонять(self):
        if self.IBU < 10:
            return 'Слабое пиво'
        elif self.IBU < 30:
            return 'Среднее пиво'
        else:
            return 'Крепкое пиво'
    
    def Представление(self):
        return f'{self.name} ({self.volume})'
    
    def Оценка(self):
        if self.IBU < 10:
            return 'Очень слабое пиво'
        elif self.IBU < 30:
            return 'Отличное пиво'
        else:
            return 'Очень горькое пиво'

b = Pivo('Жигули', 10, 50)
print(b.volume)
print(b.Оценка())
print(b.Представление())
print(b.Сгонять())