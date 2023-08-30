"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(-1) is False
        assert product.check_quantity(-10) is False
        assert product.check_quantity(1) is True
        assert product.check_quantity(10) is True
        assert product.check_quantity(999) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False
        assert product.check_quantity(10001) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(1)
        assert product.quantity == 999
        product.buy(99)
        assert product.quantity == 900
        product.buy(900)
        assert product.quantity == 0

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            assert product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_cart_add_product(self, cart, product):
        assert len(cart.products) == 0
        cart.add_product(product, 1)
        assert cart.products[product] == 1
        cart.add_product(product, 10)
        assert cart.products[product] == 11

    def test_cart_remove_product(self, cart, product):
        # remove_count передан
        cart.add_product(product, 10)
        cart.remove_product(product, 1)
        assert cart.products[product] == 9
        # remove_count = buy_count
        cart.remove_product(product, 9)
        assert len(cart.products) == 0
        # remove_count не передан
        cart.add_product(product, 10)
        cart.remove_product(product)
        assert len(cart.products) == 0
        # remove_count > buy_count
        cart.add_product(product, 10)
        cart.remove_product(product, 100)
        assert len(cart.products) == 0

    def test_cart_clear(self, cart, product):
        cart.add_product(product, 10)
        cart.clear()
        assert len(cart.products) == 0

    def test_cart_get_total_price(self, cart, product):
        cart.add_product(product, 10)
        assert cart.get_total_price() == 1000

    def test_cart_buy(self, cart, product):
        cart.add_product(product, 10)
        cart.buy()
        assert len(cart.products) == 0
        assert product.quantity == 990

    def test_cart_buy_value_error(self, cart, product):
        cart.add_product(product, 9999)
        with pytest.raises(ValueError):
            assert cart.buy()
