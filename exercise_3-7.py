guest_list = [
    "Raisa Andriana",
    "Maudy Ayunda",
    "Dian Sastrowardoyo",
    "Najwa Shihab",
    "Nadiem Makarim",
    "Nicholas Saputra"
]

# Informasi perubahan jumlah tamu
print("Mohon maaf, meja makan tidak dapat digunakan.")
print("Saya hanya bisa mengundang dua orang untuk makan malam.\n")

# Menghapus tamu sampai tersisa dua orang
while len(guest_list) > 2:
    removed_guest = guest_list.pop()

    print(f"Maaf {removed_guest}, saya tidak bisa mengundang Anda untuk makan malam.")

# Memberikan pesan kepada dua tamu yang masih diundang
print("\nDua tamu yang tetap diundang:")

print(f"{guest_list[0]}, Anda tetap diundang untuk makan malam.")
print(f"{guest_list[1]}, Anda tetap diundang untuk makan malam.")

# Menghapus dua nama yang tersisa
del guest_list[0]
del guest_list[0]

# Memastikan list kosong
print("\nDaftar tamu setelah semua nama dihapus:")
print(guest_list)