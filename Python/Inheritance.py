"""Single level inheritance"""

class Phone:
    def make_call(self):
        print("Making a call")

class Smartphone(Phone):
    def send_message(self):
        print("Sending a message")

smartphone = Smartphone()
smartphone.make_call()
smartphone.send_message()

"""Multi level inheritance"""

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"The engine of {self.brand} {self.model} is starting.")

    def stop_engine(self):
        print(f"The engine of {self.brand} {self.model} is stopping.")

class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} {self.model} is now in motion.")

class SportsCar(Car):
    def accelerate(self):
        print(f"{self.brand} {self.model} is accelerating at high speed.")

vehicle = Vehicle("Swift", "Dezire")
car = Car("Ford", "Mustang")
sports_car = SportsCar("Renault", "Logan")

vehicle.start_engine()
vehicle.stop_engine()

car.start_engine()
car.stop_engine()
car.drive()

sports_car.start_engine()
sports_car.accelerate()
sports_car.stop_engine()