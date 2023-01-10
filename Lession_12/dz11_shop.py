from pprint import pprint

class Shop():
    def __init__(self) -> None:
        self.storage = {}
        self.prices = {}

    def add_product_on_storage(self, product: str, amount: int):
        self.storage[product] = self.storage.get(product, 0) + amount
    
    def add_product_price(self, product: str, price: float):
        self.prices.update({product: price})

    def get_prices(self):
        for i in self.prices.keys():
            print(f'{i}: {self.prices[i]}')
    
    def get_storage(self):
        for i in self.storage.keys():
            print(f'{i}: {self.storage[i]}')

    def get_information(self):  
        for i in self.prices.keys():
            print(f"{i}:    {self.prices[i]}    {self.storage.get(i, 'Нет на складе')}")

    def selling(self, product, amount):
        if self.storage[product] > amount:
            self.storage[product] -=amount
        else:
            return 'Недостаточно товара на складе'


s = Shop()
s.add_product_price('hleb', 15)
s.add_product_price('moloko', 8)
s.add_product_on_storage('moloko', 7)
s.get_information()

    
