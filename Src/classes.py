class Category:
    """Экземпляр класса категорий продуктов"""

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
        """Геттер списка товаров в объекте класса Category"""

        return self.__goods

    @property
    def goods_list(self):
        """Геттер списка товаров в объекте класса Category с указанием цены и остатка"""

        return [f"{good.name}, {good.price} руб., Остаток: {good.quantity_in_stock} шт." for good in self.__goods]

    @goods.setter
    def goods(self, good):
        """Сеттер добавления товара в список товаров объекта класса Category"""

        self.__goods.append(good)


class Product:
    """Экземпляр класса продуктов"""

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
        """Метод создания нового продукта с учетом фильтрации дубликатов. При обнаржуении дубликата,
        складывается остаток и принимается наиболее высокая цена в сравнении между дубликатами"""

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
        """Геттер получения информации о некорректном значении цены товара"""

        if self.price <= 0:
            print("Некорректная цена товара")
            return True

    @is_low_price.setter
    def set_low_price(self, new_price):
        answer = input("Понизить цену товара? Y/N: ")
        if answer.lower() == "y":
            self.price = new_price
