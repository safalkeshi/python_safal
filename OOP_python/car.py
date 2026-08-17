class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale


        def get_brand(self):
            return self.__brand
        
    def full_name(self):
        return f"{self.model} {self.color}"


class ElectricCar(Car):
    def __init__(self, battery_size, year, model, color, for_sale):
        # Note: In your super(), make sure the order matches Car's __init__ (model, year, color, for_sale)
        super().__init__(model, year, color, for_sale)
        self.battery_size = battery_size


# 1. Pass 5 items in the exact order ElectricCar expects them:
# battery_size="85 kWh", year=2026, model="Model S", color="Red", for_sale=True
my_tesla = ElectricCar("85 kWh", 2026, "Model S", "Red", True)    

# 2. Add () to call the method
print(my_tesla.full_name())  # Output: Model S Red