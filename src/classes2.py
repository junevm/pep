# Goal: Create a simple system to manage different types of vehicles in a garage using inheritance.
# Step 1: Create the Parent Class
# Define a class named Vehicle with:
# Attributes: brand and model.
# Methods:
# **init**(self, brand, model): Initializes the attributes.
# start_engine(self): Prints "The [brand] [model] engine is now running!".
# Step 2: Create the Child Classes
# Class Car:
# Inherits from Vehicle.
# Extra Attribute: num_doors.
# Method Override: Use super() in the **init** method to handle brand and model.
# New Method: open_trunk() which prints "Trunk is open."
# Class Bike:
# Inherits from Vehicle.
# Extra Attribute: has_sidecar (a boolean).
# Method Override: Use super() in the **init** method.
# New Method: pop_wheelie() which prints "The bike is doing a wheelie!"
# Would you like me to generate the Python code based on these steps?

# Step 1: Create the Parent Class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"The {self.brand} {self.model} engine is now running!")

# Step 2: Create the Child Classes
class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        # Use super() to handle brand and model from the Parent class
        super().__init__(brand, model)
        self.num_doors = num_doors

    def open_trunk(self):
        print("Trunk is open.")

class Bike(Vehicle):
    def __init__(self, brand, model, has_sidecar):
        # Use super() to handle brand and model from the Parent class
        super().__init__(brand, model)
        self.has_sidecar = has_sidecar

    def pop_wheelie(self):
        print("The bike is doing a wheelie!")

# --- Testing the code ---
my_car = Car("Toyota", "Camry", 4)
my_car.start_engine()
my_car.open_trunk()

print("---")

my_bike = Bike("Harley-Davidson", "Iron 883", False)
my_bike.start_engine()
my_bike.pop_wheelie()