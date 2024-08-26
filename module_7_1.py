class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        self.products_file = None

    def get_products(self):
        products_file = open(self.__file_name, 'r')
        text = products_file.read()
        products_file.close()
        return text

    def add(self, *products: Product):
        for product in products:
            self.products_file = open(self.__file_name, 'a+')
            if product.__str__() not in self.get_products():
                self.products_file.write(str(product) + '\n')
                self.products_file.seek(0)
            else:
                print(f'Продукт {product.__str__()} уже есть в магазине')
            self.products_file.close()


if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())
