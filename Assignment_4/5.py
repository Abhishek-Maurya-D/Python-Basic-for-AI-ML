class Vehicle():
    def __init__(self, brand, model):
        self.brand = brand;
        self.model = model;
    
class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model);
        self.seats = seats;

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model);
        self.engine_cc = engine_cc;

car1 = Car("Toyota", "Corolla", 5)
bike1 = Bike("Hero Splendor", "Xtech", 100)

# Print details
print(car1.brand, car1.model, car1.seats);
print(bike1.brand, bike1.model, bike1.engine_cc);