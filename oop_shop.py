from datetime import date

class Product:
    def __init__(self, name, price, stock, weight):
        self.name=name
        self.price=price
        self.stock=stock
        self.weight=weight

    def get_info(self):
        return f"Product Name: {self.name}, Price: ${self.price}, Stock: {self.stock}, Weight: {self.weight} kg"

    def apply_discount(self, discount_percentage):
        self.price-=(self.price*(discount_percentage/100))
        return self.price

    def check_stock(self,quantity):
        if self.stock >= quantity:
            self.stock-=quantity
            return f"Order {quantity} units of {self.name}: Successful, Stock Left: {self.stock}"
        else:
            return f"{self.name} is out of stock!"

    def calculate_shipping_cost(self):
        cost=self.weight*10
        return f"Shipping cost for {self.name}: ${cost:.2f}"



class ElectronicProduct(Product):
    def __init__(self, name, price, stock, weight, warranty_years, brand):
        super().__init__(name, price, stock, weight)
        self.warranty_years=warranty_years
        self.brand=brand

    def get_info(self):
        return f"Electronic Product: {self.name} (Brand: {self.brand}), Price: ${self.price:.2f}, Warranty: {self.warranty_years} years, Stock: {self.stock}, Weight: {self.weight} kg"

    def calculate_warranty_extension(self,extra_years):
        self.warranty_years+=extra_years
        return f"Extended warranty for {self.name}: {self.warranty_years} years"

class GroceryProduct(Product):
    def __init__(self, name, price, stock, weight, expiration_date, is_perishable):
        super().__init__(name, price, stock, weight)
        self.expiration_date=expiration_date
        self.is_perishable=is_perishable

    def get_info(self):
        return f"Grocery Product: {self.name}, Price: ${self.price:.2f}, Expiration Date: {self.expiration_date}, Stock: {self.stock}, Weight: {self.weight} kg, Perishable: {self.is_perishable}"

    def check_if_expired(self,current_date):
        if current_date >= self.expiration_date:
            self.is_perishable=True
        else:
            self.is_perishable=False
        return f"Is Milk expired? {self.is_perishable}"



Laptop_1=ElectronicProduct("Laptop", 1500,10, 2.5, 3, "Dell")
Milk_1=GroceryProduct("Milk", 4,50,1, date(2024,11, 15), True )

print(Laptop_1.get_info())
print(Milk_1.get_info())
(Laptop_1.apply_discount(15))
#15% discount on laptop
print(Laptop_1.get_info())
# Order 5 units each of milk & laptop
print(Laptop_1.check_stock(5))
print(Milk_1.check_stock(5))
print(Milk_1.get_info())
# Shipping cost for Laptop
print(Laptop_1.calculate_shipping_cost())
print(Milk_1.calculate_shipping_cost())
# For the laptop, extend the warranty by 2 more years.
print(Laptop_1.calculate_warranty_extension(2))
# Check if milk is expired given today's date (assume today's date is "2024-10-01")
print(Milk_1.check_if_expired(date(2024,10, 1)))
