class Category:
    name: str
    description: str
    __goods: list
    total_of_category = 0
    total_of_products = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.__goods = goods
        Category.total_of_category += 1

    @property
    def goods(self):
        return self.__goods

    @goods.setter
    def goods(self, good):
        self.__goods.append(good)


class Product:
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        Category.total_of_products += 1
