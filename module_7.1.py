from pprint import pprint
class Product():
    # Метод __str__, который возвращает  строку в формате
    # '<название>, <вес>, <категория>'.Все данные в строке
    # разделены запятой с пробелами.
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'{self.name}, {self.weight}, {self.category}')

class Shop():
    def __init__(self):
        self.__file_name = 'product.txt'

    def  get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products


    def add(self, *products: Product):
        for i in products:
            if i.name not in self.get_products():
                file = open(self.__file_name, 'a')
                file.write(i.__str__() + '\n')

            else:
                print(f'Продукт {i.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())