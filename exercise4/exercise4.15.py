# Program 1: Menampilkan jenis pizza favorit sesuai standar PEP 8
favorite_pizzas = ["Pepperoni", "Cheese", "Beef", "Mushroom"]

for pizza in favorite_pizzas:
    print(f"I like {pizza} pizza.")

print("I really love pizza!")

# Program hewan dengan gaya PEP 8
animals = ["Cat", "Rabbit", "Hamster"]

for animal in animals:
    print(f"A {animal.lower()} would make a great pet.")

print("\nThese animals are cute and can be great pets!")

# Program 3: Membuat list kubus dari 1 hingga 10
cubes = [value**3 for value in range(1, 11)]

for cube in cubes:
    print(cube)