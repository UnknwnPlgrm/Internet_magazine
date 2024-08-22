import pytest

from Src import classes


@pytest.fixture
def category_example():
    return classes.Category("Товары для дома", "Бытовая электроника, мебель", [])


#        ["Стиральная машина", "Холодильник", "Микроволновая печь", "Столешница", "Стул", "Стол"],
#   )


@pytest.fixture
def category_example_2():
    return classes.Category("Товары для дачи", "Бытовая электроника, мебель, садовые инструменты", [])


#        [
#            "Стиральная машина",
#            "Холодильник",
#            "Микроволновая печь",
#            "Газонокосилка",
#            "Грабли",
#            "Столешница",
#            "Стул",
#            "Стол",
#        ],
#    )


@pytest.fixture
def product_example():
    return classes.Product("Холодильник", "Аппарат для охлаждения продуктов", 49999.99, 4)


@pytest.fixture
def product_example_2():
    return classes.Product("Микроволновая печь", "Аппарат для разогрева продуктов", 13400, 5)


@pytest.fixture
def product_example_3():
    return classes.Product("Газонокосилка", "Аппарат для облагораживания территории, путем скоса травы", 23000.5, 2)


@pytest.fixture
def product_example_4():
    return classes.Product("Стол", "Объект мебели для помещений различного назначения", 3000, 1)


@pytest.fixture
def goods_list_example():
    return [
        "Холодильник, 49999.99 руб., Остаток: 4 шт.",
        "Микроволновая печь, 13400 руб., Остаток: 5 шт.",
        "Газонокосилка, 23000.5 руб., Остаток: 2 шт.",
        "Стол, 3000 руб., Остаток: 1 шт.",
    ]
