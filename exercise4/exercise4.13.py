# Menu awal restoran
buffet_menu = (
    "Fried rice",
    "Chicken satay",
    "Meatball soup",
    "Fried chicken",
    "Gado-gado"
)

# Menampilkan menu awal
print("Original buffet menu:")

for food in buffet_menu:
    print(food)

# Mencoba mengubah salah satu menu
print("\nTrying to change the menu:")

try:
    buffet_menu[0] = "Grilled fish"
except TypeError:
    print("Python does not allow changing tuple items.")

# Mengganti menu restoran
buffet_menu = (
    "Fried rice",
    "Grilled fish",
    "Meatball soup",
    "Beef steak",
    "Gado-gado"
)

# Menampilkan menu terbaru
print("\nRevised buffet menu:")

for food in buffet_menu:
    print(food)