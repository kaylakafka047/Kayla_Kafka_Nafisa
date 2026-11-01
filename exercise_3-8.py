places = [
    "Kyoto",
    "Paris",
    "Swiss",
    "Seoul",
    "Bali",
    "London"
]

# Menampilkan urutan asli
print("Urutan asli:")
print(places)

# Mengurutkan sementara secara alfabetis
print("\nUrutan alfabetis:")
print(sorted(places))

# Membuktikan urutan asli tidak berubah
print("\nUrutan asli setelah sorted():")
print(places)

# Mengurutkan sementara secara alfabetis terbalik
print("\nUrutan alfabetis terbalik:")
print(sorted(places, reverse=True))

# Membuktikan urutan asli tetap sama
print("\nUrutan asli:")
print(places)

# Membalik urutan list
places.reverse()

print("\nUrutan setelah reverse() pertama:")
print(places)

# Mengembalikan urutan seperti semula
places.reverse()

print("\nUrutan setelah reverse() kedua:")
print(places)

# Mengurutkan list secara alfabetis
places.sort()

print("\nUrutan setelah sort() alfabetis:")
print(places)

# Mengurutkan list secara alfabetis terbalik
places.sort(reverse=True)

print("\nUrutan setelah sort() terbalik:")
print(places)