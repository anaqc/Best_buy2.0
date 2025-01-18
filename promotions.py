from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name


    def apply_promotion(self, product, quantity):
        """ This method gets 2 parameters - a product instance and a quantity,
        and returns the discounted price after promotion was applied."""
        pass


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        """ Second item at half price """
        quantity_promotion = int(quantity / 2)
        rest_quantity = quantity - quantity_promotion
        return (quantity_promotion * product.price / 2) + (rest_quantity * product.price)


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        """ Buy 2, get 1 free"""
        quantity_free = quantity // 3
        return product.price * (quantity - quantity_free)


class PercentDiscount(Promotion):
    def __init__(self,name, percent):
        super().__init__(name)
        self.percent = percent


    def apply_promotion(self, product, quantity):
        """ Percentage discount"""
        total = product.price * quantity
        total_with_discount = (1 - self.percent / 100) * total
        return total_with_discount

