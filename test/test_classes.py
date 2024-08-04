from Src import classes


def test_category(category_example, category_example_2):
    assert category_example.name == "Товары для дома"
    assert category_example.description == "Бытовая электроника, мебель"
    assert category_example.goods == [
        "Стиральная машина",
        "Холодильник",
        "Микроволновая печь",
        "Столешница",
        "Стул",
        "Стол",
    ]
    category_example.goods = "Электрический чайник"
    assert category_example.goods == [
        "Стиральная машина",
        "Холодильник",
        "Микроволновая печь",
        "Столешница",
        "Стул",
        "Стол",
        "Электрический чайник"
    ]
    assert classes.Category.total_of_category == 2



def test_product(product_example, product_example_2, product_example_3, product_example_4):
    assert product_example.name == "Холодильник"
    assert product_example.description == "Аппарат для охлаждения продуктов"
    assert product_example.price == 49999.99
    assert product_example.quantity_in_stock == 4
    assert classes.Category.total_of_products == 4


