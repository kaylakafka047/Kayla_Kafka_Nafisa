class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}")


restaurant1 = Restaurant("Pagi Sore", "Masakan Padang")
restaurant2 = Restaurant("HokBen", "Masakan Jepang")
restaurant3 = Restaurant("KFC", "Makanan Cepat Saji")

restaurant1.describe_restaurant()
print()

restaurant2.describe_restaurant()
print()

restaurant3.describe_restaurant()