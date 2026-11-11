class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_car = ElectricCar("nissan", "leaf", 2024)

print(my_car.get_descriptive_name())

print("\nSebelum upgrade:")
my_car.battery.describe_battery()
my_car.battery.get_range()

print("\nSetelah upgrade:")
my_car.battery.upgrade_battery()
my_car.battery.describe_battery()
my_car.battery.get_range()