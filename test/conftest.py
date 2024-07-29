import pytest

from Src import classes


@pytest.fixture
def category_example():
    return classes.Category(
        "Товары для дома",
        "Бытовая электроника, мебель",
        ["Стиральная машина", "Холодильник", "Микроволновая печь", "Столешница", "Стул", "Стол"],
    )


@pytest.fixture
def category_example_2():
    return classes.Category(
        "Товары для дачи",
        "Бытовая электроника, мебель, садовые инструменты",
        [
            "Стиральная машина",
            "Холодильник",
            "Микроволновая печь",
            "Газонокосилка",
            "Грабли",
            "Столешница",
            "Стул",
            "Стол",
        ],
    )


@pytest.fixture
def product_example():
    return classes.Product("Холодильник", "Аппарат для охлаждения продуктов", 49999.99, 4)


@pytest.fixture
def product_example_2():
    return classes.Product("Микроволновая печь", "Аппарат для разогрева продуктов", 13400, 5)


@pytest.fixture
def product_example_3():
    return classes.Product("Газонокосилка", "Аппарат для облагораживания территории, путем скоса травы", 23000.50, 2)


@pytest.fixture
def product_example_4():
    return classes.Product("Стол", "Объект мебели для помещений различного назначения", 3000, 1)
