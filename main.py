from car import Car

car1 = Car("Toyota Camry", 2020, "Blue", True)

print(car1.model)  # Output: Toyota Camry
print(car1.year)   # Output: 2020
print(car1.color)  # Output: Blue
print(car1.for_sale)  # Output: True

car1.drive()  # Output: You drive the Toyota Camry.
car1.stop()   # Output: You stop the Toyota Camry.

car1.describe()  # Output: 2020 Blue Toyota Camry