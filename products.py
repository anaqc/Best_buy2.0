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
            # Initialize instance variables
            self.name = name
            self.price = price
            self.quantity = quantity
            if quantity == 0:
                self.active = False
            else:
                self.active = True
            self.promotion = None
        except ValueError as e:
            print(e)

    def get_promotion(self):
        return self.promotion


    def set_promotion(self, new_promotion):
        self.promotion = new_promotion


    def get_quantity(self) -> float:
        """ This function get the quantity from a product"""
        return float(self.quantity)


    def set_quantity(self, quantity):
        """ This function update the quantity from a product"""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False


    def is_active(self) -> bool:
        """ This function returns True if a product is activ or False if not"""
        return self.active


    def activate(self):
        """ This function activate a product if is_activate = False"""
        self.active = True


    def deactivate(self):
        """ This function deactivate the product"""
        self.active = False


    def show(self) -> str:
        """ This function return a string with the product information"""
        type_promotion = ""
        if self.get_promotion() is not None:
            type_promotion = f", Promotion: {self.get_promotion().name}"
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{type_promotion}"


    def buy(self, buy_quantity) -> float:
        """ This function buy a product"""
        if self.get_promotion() is not None:
            self.quantity -= buy_quantity
            return self.promotion.apply_promotion(self, buy_quantity)
        if self.quantity > buy_quantity and self.active:
            self.quantity -= buy_quantity
            return self.price * buy_quantity
        if self.quantity == buy_quantity and self.active:
            self.quantity = 0
            self.deactivate()
            return self.price * buy_quantity
        raise ValueError("Insufficient quantity")


    def add_promotion(self):
        pass


class NonStockedProduct(Product):
    def __init__(self, name, price):
        quantity = 0
        super().__init__(name, price, quantity)
        self.active = True

    def buy(self, buy_quantity) -> float:
        """ This function buy a product"""
        if self.get_promotion() is not None:
            return self.promotion.apply_promotion(self, buy_quantity)
        return self.price * buy_quantity


    def show(self) -> str:
        """ This function return a string with the product information"""
        type_promotion = ""
        if self.get_promotion() is not None:
            type_promotion = f", Promotion: {self.get_promotion().name}"
        return f"{self.name}, Price: {self.price}{type_promotion}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum


    def show(self) -> str:
        """ This function return a string with the product information"""
        type_promotion = ""
        if self.get_promotion() is not None:
            type_promotion = f", Promotion: {self.get_promotion().name}"
        return (f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, "
                f"Maximum: {self.maximum}{type_promotion}")


    def buy(self, buy_quantity) -> float:
        """ This function buy a product"""
        if self.maximum == buy_quantity:
            return super().buy(buy_quantity)
        raise ValueError("Error Limited product")



