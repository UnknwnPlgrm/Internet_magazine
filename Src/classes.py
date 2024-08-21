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
    products_list = []

    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock


    @classmethod
    def create_product(cls, name, description, price, quantity_in_stock):
        for product in Product.products_list:
            if product.name.lower == name.lower:
                product.quantity_in_stock += quantity_in_stock
                if product.price < price:
                    product.price = price
                return product
        created_product = cls(name, description, price, quantity_in_stock)
        Product.products_list.append(created_product)
        Category.total_of_products += 1
        return created_product

    @property
    def is_low_price(self):
        if self.price <= 0:
            print("Некорректная цена товара")
            return True
