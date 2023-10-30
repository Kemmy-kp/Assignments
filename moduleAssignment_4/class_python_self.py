#How to Define a Class in Python? What Is Self? Give An Example Of A Python Class

In Python, a class is a blueprint for creating objects (instances) that can have attributes (variables) and methods (functions). To define a class in Python, you use the class
keyword followed by the class name. The class definition typically includes attributes and methods. The self parameter is a reference to the instance of the class and is used to
access its attributes and methods.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start_engine(self):
        if not self.is_running:
            print(f"{self.year} {self.make} {self.model}'s engine is starting.")
            self.is_running = True
        else:
            print(f"{self.year} {self.make} {self.model}'s engine is already running.")

    def stop_engine(self):
        if self.is_running:
            print(f"{self.year} {self.make} {self.model}'s engine is stopping.")
            self.is_running = False
        else:
            print(f"{self.year} {self.make} {self.model}'s engine is already stopped.")

# Creating instances of the Car class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Accord", 2023)

# Accessing attributes and calling methods
print(car1.make)  # Output: Toyota
print(car2.model)  # Output: Accord

car1.start_engine()  # Output: 2022 Toyota Camry's engine is starting.
car2.start_engine()  # Output: 2023 Honda Accord's engine is starting.
car1.stop_engine()   # Output: 2022 Toyota Camry's engine is stopping.
car2.stop_engine()   # Output: 2023 Honda Accord's engine is stopping.
