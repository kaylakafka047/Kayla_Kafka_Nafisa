favorite_pizzas = [
    "Pepperoni",
    "Cheese",
    "Beef"
]

# Menyalin list pizza
friend_pizzas = favorite_pizzas[:]

# Menambahkan pizza ke list asli
favorite_pizzas.append("Mushroom")

# Menambahkan pizza berbeda ke list teman
friend_pizzas.append("Tuna")

# Menampilkan pizza favorit
print("My favorite pizzas are:")

for pizza in favorite_pizzas:
    print(pizza)

# Menampilkan pizza favorit teman
print("\nMy friend's favorite pizzas are:")

for pizza in friend_pizzas:
    print(pizza)