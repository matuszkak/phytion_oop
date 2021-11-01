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
            print(f'New product recorded in Warehouse: {product_name}')

    def remove_product(self, product_name):
        for product in self.products:
            if product[1] == product_name:
                self.products.remove(product)
                print(f'\nProduct removed from Warehouse: {product_name}')

    def display_products(self):
        print(f'\nWarehouse product list:')
        for product in self.products:

            print(product)

    def sort_by_price(self, ascending):
        if ascending:
            return self.products.sort(key=lambda x: x[2])
            # print(f'\nWarehouse product list by price - ascending order:')
            # for product in self.products:
            #     print(f'product_name: {product[1]}, price: {product[2]}')
        else:
            return self.products.sort(key=lambda x: x[2], reverse=True)
            # print(f'\nWarehouse product list by price - descending order:')
            # for product in self.products:
            #     print(product)


warehouse = Warehouse()
warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)
warehouse.add_product('Camera', 2900.0)
warehouse.add_product('USB Cable', 24.9)
warehouse.add_product('Mouse', 49.0)
warehouse.add_product('Monitor', 949.0)

warehouse.display_products()
warehouse.remove_product('Monitor')

warehouse.display_products()
warehouse.sort_by_price(True)

print(f'\nWarehouse product list by price - ascending order:')
for product in warehouse.products:
    print(product)