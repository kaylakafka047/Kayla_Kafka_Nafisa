books = [
    "Laskar Pelangi",
    "Bumi",
    "Hujan",
    "Laut Bercerita",
    "Negeri 5 Menara"
]

# Menampilkan list awal
print("Daftar buku awal:")
print(books)

# Mengakses elemen berdasarkan indeks
print("\nBuku pertama:")
print(books[0])

# Mengubah elemen dalam list
books[1] = "Bulan"

print("\nSetelah mengubah nama buku:")
print(books)

# Menambahkan elemen menggunakan append()
books.append("Pulang")

print("\nSetelah append():")
print(books)

# Menambahkan elemen menggunakan insert()
books.insert(2, "Dilan 1990")

print("\nSetelah insert():")
print(books)

# Menghapus elemen menggunakan remove()
books.remove("Hujan")

print("\nSetelah remove():")
print(books)

# Menghapus elemen menggunakan pop()
removed_book = books.pop()

print("\nBuku yang dihapus menggunakan pop():")
print(removed_book)
print(books)

# Menghapus elemen menggunakan del
del books[0]

print("\nSetelah menggunakan del:")
print(books)

# Mengurutkan list menggunakan sorted()
print("\nUrutan alfabetis menggunakan sorted():")
print(sorted(books))

# Mengurutkan list menggunakan sort()
books.sort()

print("\nSetelah menggunakan sort():")
print(books)

# Membalik urutan menggunakan reverse()
books.reverse()

print("\nSetelah menggunakan reverse():")
print(books)

# Menghitung jumlah buku menggunakan len()
print("\nJumlah buku:")
print(len(books))