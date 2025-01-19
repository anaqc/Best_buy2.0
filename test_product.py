import pytest
import products
import promotions
import store

# test product_list
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("MacBook Air", price=1000, quantity=10),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                products.LimitedProduct("Google Pixel 7", price=500, quantity=250, maximum=1)
                ]
# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].promotion = second_half_price
product_list[1].promotion = third_one_free
product_list[2].promotion = thirty_percent


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
    # new_store.get_total_quantity() = 1110
    list_order = [(test_store.get_product_by_index(0), 10)]
    test_store.order(list_order)
    assert test_store.get_total_quantity() == 1100


def test_buying_larger_quantity():
    buying_product = test_store.get_product_by_index(0)
    with pytest.raises(ValueError, match="Insufficient quantity"):
        buying_product.buy(110)


def test_ordering_limited_product_over_the_limit_quantity():
    # product = "Google Pixel 7", price=500, quantity=250, maximum=1
    product = test_store.get_product_by_index(4)
    with pytest.raises(ValueError, match="Error Limited product"):
        product.buy(3)


def test_promotion_second_half_price():
    # total without discount is 2900
    product = test_store.get_product_by_index(0)
    assert product.buy(2) == 2175


def test_third_one_free():
    # total without discount is 4000
    product = test_store.get_product_by_index(1)
    assert product.buy(4) == 3000


def test_thirty_percent():
    # total without discount is 1000
    product = test_store.get_product_by_index(2)
    assert product.buy(4) == 700
