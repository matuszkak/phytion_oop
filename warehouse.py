import uuid


class Product:
    def __init__(self, product_name, price):
        self.name = product_name
        self.price = price
        self.id = self.get_id()
        print('\nProduct created!')

    def __repr__(self):
        return f"A termék neve: {self.name}, ára: {self.price}"

    @staticmethod
    def get_id():
        id = str(uuid.uuid4())
        id_parts = id.split('-')
        return id_parts[4]


class Warehouse:
    def __init__(self):
        self.products = []
        # print('Warehouse created!')

    def add_product(self, product_name, price):
        if product_name in self.products:
            print(f'Product already in Warehouse!')
        else:
            newProduct = Product(product_name, price)
            print(newProduct.id, newProduct.name, newProduct.price)
            self.products.append(
                [newProduct.id, newProduct.name, newProduct.price])
            print(f'\nNew product recorded: {product_name}')

    def remove_product(self, product_name):
        for product in self.products:
            if product[1] == product_name:
                self.products.remove(product)
                print(f'\nProduct removed: {product_name}')

    def display_products(self):
        print(f'\nWarehouse product list:')
        for product in self.products:

            print(product)

    def sort_by_price(self, ascending):
        if ascending:
            self.products.sort('price')
            for product in self.products:
                print(product)
        else:
            for product in self.sort(key='price', reverse=True):
                print(product)


myProduct = Product('alma', 20)
print(myProduct)

print(myProduct.id, myProduct.name, myProduct.price)

myWarehouse = Warehouse()
myWarehouse.add_product('Laptop', 3900.0)
myWarehouse.add_product('Monitor', 5800.0)
myWarehouse.add_product('Mouse', 1100.0)
myWarehouse.display_products()
myWarehouse.remove_product('Monitor')
myWarehouse.display_products()
myWarehouse.sort_by_price(True)