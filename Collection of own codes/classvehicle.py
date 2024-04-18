class Vehicle:
    def __init__(self, make, model):
        # Initialize a Vehicle object with make and model attributes
        self.make = make
        self.model = model

    def get_info(self):
        # Return a formatted string with the make and model information
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def start_engine(self):
        # Method to start the car's engine
        return "Engine started"

# Create a Car object with make "Toyota" and model "Corolla"
car = Car("Toyota", "Corolla")

# Print the vehicle information and start the engine
print(car.get_info())
print(car.start_engine())
