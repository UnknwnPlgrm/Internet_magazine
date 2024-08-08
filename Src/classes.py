class Category:
    name: str
    description: str
    __goods: list
    goods: list
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

    @property
    def goods_list(self):
        return [f'{good.name}, {good.price} руб., Остаток: {good.quantity_in_stock} шт.' for good in self.__goods]

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

    @classmethod
    def create_product(cls, name, description, price, quantity_of_stock):
        created_product = cls(name, description, price, quantity_of_stock)
        return created_product

    @property
    def is_low_price(self):
        if self.price <= 0:
            print("Некорректная цена товара")
            return True
