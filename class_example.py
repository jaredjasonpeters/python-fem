class Vehicle:

    num_of_wheels = 4

    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

    def __str__(self):
        return f"I drive {self.make} {self.model}. It runs on {self.fuel}!"


class Car(Vehicle):

    num_of_wheels = 4


class Truck(Vehicle):

    num_of_wheels = 8

    def __init__(self, make, model, fuel="diesel"):
        super().__init__(make, model, fuel)


my_truck = Truck('Ford', 'F-150', 'corn oil')

truck = Car('Toyota', 'Tundra')

daily = Vehicle('Subaru', 'Outback')

# print(daily)
print(daily)
print(my_truck)
print(truck)

# python interactive
# python -i <filePath>
