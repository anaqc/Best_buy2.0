import pytest
import products
import store


product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                ]
test_store = store.Store(product_list)


def test_creating_product():
    assert products.Product("MacBook Air M2", 1450, 100)


def test_creating_product_with_invalid_name():
    assert products.Product("", 1450, 100)


def test_creating_product_with_negative_price():
    assert products.Product("MacBook Air M2", -10, 100)


def test_creating_product_with_negative_quantity():
    assert products.Product("MacBook Air M2", 10, -100)


def test_set_quantity_negative():
    product = test_store.get_product_by_index(0)
    with pytest.raises(ValueError, match="Quantity cannot be negative"):
        product.quantity =-10


def test_product_quantity_is_0_and_inactive():
    new_product = products.Product("MacBook Air M2", 1450, 0)
    assert new_product.is_active() == False


def test_product_purchase_modifies_the_quantity():
    # new_store.get_total_quantity() = 850
    list_order = [(test_store.get_product_by_index(0), 10)]
    test_store.order(list_order)
    assert test_store.get_total_quantity() == 840


def test_buying_larger_quantity():
    buying_product = test_store.get_product_by_index(0)
    with pytest.raises(ValueError, match="Insufficient quantity"):
        buying_product.buy(110)

