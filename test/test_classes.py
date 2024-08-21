from Src import classes


def test_category(category_example, category_example_2, product_example_3,
                  product_example_4, product_example, product_example_2, goods_list_example):
    assert category_example.name == "Товары для дома"
    assert category_example.description == "Бытовая электроника, мебель"
    assert category_example.goods == []
    category_example.goods = product_example
    category_example.goods = product_example_2
    category_example.goods = product_example_3
    category_example.goods = product_example_4
    assert category_example.goods == [product_example, product_example_2,
                                      product_example_3, product_example_4]
    assert category_example.goods_list == goods_list_example
    assert classes.Category.total_of_category == 2




def test_product(product_example, product_example_2, product_example_3, product_example_4):
    assert product_example.name == "Холодильник"
    assert product_example.description == "Аппарат для охлаждения продуктов"
    assert product_example.price == 49999.99
    assert product_example.quantity_in_stock == 4
    product = classes.Product.create_product("камень", "я не дам", 0, 3)
    assert product.name == "камень"
    assert product.description == "я не дам"
    assert product.is_low_price == True
    product_new = classes.Product.create_product("камень", "я не дам", 30, 2)
    assert product_new.quantity_in_stock == 5
    assert product_new.price == 30
    assert classes.Category.total_of_products == 1