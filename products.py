class Product:
    def __init__(self, name: str, price: float, quantity: int):
        """ Validate inputs """
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
        self.active = True


    def get_quantity(self) -> float:
        """ This function get the quantity from a product"""
        return float(self.quantity)


    def set_quantity(self, quantity):
        """ This function update the quantity from a product"""
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
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity) -> float:
        """ This function buy a product"""
        try:
            if self.quantity > quantity and self.active:
                self.quantity -= quantity
                return self.price * quantity
            if self.quantity == quantity:
                self.quantity = 0
                self.deactivate()
                return self.price * quantity
            raise ValueError("Insufficient quantity")
        except ValueError as e:
            print(e)
            return 0
