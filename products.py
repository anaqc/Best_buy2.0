class Product:
    def __init__(self, name: str, price: float, quantity:int):
        """ Validate inputs """
        try:
            if not name:
                raise ValueError("Name cannot be empty")
            if price < 0:
                raise ValueError("Price cannot be negative")
            if quantity < 0:
                raise ValueError("Quantity cannot be negative")
            if quantity == 0:
                self.active = False
            else:
                self.active = True
            # Initialize instance variables
            self._name = name
            self._price = price
            self._quantity = quantity
            self._promotion = None
        except ValueError as e:
            print(e)


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or new_name == "":
            raise ValueError("Error value of Name")
        self._name = new_name


    @property
    def price(self):
        return self._price


    @price.setter
    def price(self, new_price):
        try:
            if new_price < 0:
                raise ValueError("Price cannot be negative")
            self._price = new_price
        except ValueError as e:
            print(e)

    @property
    def quantity(self) -> float:
        """ This function get the quantity from a product"""
        return float(self._quantity)


    @quantity.setter
    def quantity(self, quantity):
        """ This function update the quantity from a product"""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self._quantity = quantity
        if self._quantity == 0:
            self.deactivate()


    @property
    def promotion(self):
        return self._promotion


    @promotion.setter
    def promotion(self, new_promotion):
        self._promotion = new_promotion


    def __lt__(self, other):
        """ This function compare if the first product price is >"""
        return self.price < other.price


    def __gt__(self, other):
        """ This function compare if the first product price is <"""
        return self.price > other.price


    def is_active(self) -> bool:
        """ This function returns True if a product is activ or False if not"""
        return self.active


    def activate(self):
        """ This function activate a product if is_activate = False"""
        self.active = True


    def deactivate(self):
        """ This function deactivate the product"""
        self.active = False


    def __str__(self) -> str:
        """ This function return a string with the product information"""
        type_promotion = ""
        if self.promotion is not None:
            type_promotion = f", Promotion: {self.promotion.name}"
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{type_promotion}"


    def buy(self, buy_quantity) -> float:
        """ This function buy a product"""
        if buy_quantity <= 0:
            raise ValueError("Buy Quantity cannot be negative")
        if buy_quantity > self.quantity:
            raise ValueError("Insufficient quantity")
        if not self.is_active():
            raise ValueError("Product is not active")
        self.quantity = self.quantity - buy_quantity
        if self.quantity == 0:
            self.deactivate()
        if self.promotion is not None:
            return self.promotion.apply_promotion(self, buy_quantity)
        return self.price * buy_quantity



class NonStockedProduct(Product):
    def __init__(self, name, price):
        quantity = 0
        super().__init__(name, price, quantity)
        self.active = True


    def buy(self, buy_quantity) -> float:
        """ This function buy a product"""
        if self.promotion is not None:
            return self.promotion.apply_promotion(self, buy_quantity)
        return self.price * buy_quantity


    def show(self) -> str:
        """ This function return a string with the product information"""
        type_promotion = ""
        if self.promotion is not None:
            type_promotion = f", Promotion: {self.promotion.name}"
        return f"{self.name}, Price: {self.price}{type_promotion}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum: int):
        super().__init__(name, price, quantity)
        if maximum < 0:
            raise ValueError("Maximum has to be a positive number")
        self._maximum = maximum


    @property
    def maximum(self):
        return self._maximum


    @maximum.setter
    def maximum(self, new_maximum):
        if isinstance(new_maximum, int)  and new_maximum > 0:
            self._maximum = new_maximum
        else:
            raise ValueError("Maximum has to be a positive number")


    def show(self) -> str:
        """ This function return a string with the product information"""
        type_promotion = ""
        if self.promotion is not None:
            type_promotion = f", Promotion: {self.promotion.name}"
        return (f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, "
                f"Maximum: {self.maximum}{type_promotion}")


    def buy(self, buy_quantity) -> float:
        """ This function buy a product"""
        if self.maximum == buy_quantity:
            return super().buy(buy_quantity)
        raise ValueError("Error Limited product")



