guest_list = [
   "Karina Aespa",
   "Haechan NCT",
   "Keonho Cortis"
]

# Menampilkan undangan awal
print("Undangan makan malam:")

print(f"Halo {guest_list[0]}, saya mengundang Anda untuk makan malam.")
print(f"Halo {guest_list[1]}, saya mengundang Anda untuk makan malam.")
print(f"Halo {guest_list[2]}, saya mengundang Anda untuk makan malam.")

# Menampilkan tamu yang tidak dapat hadir
print(f"\n{guest_list[1]} tidak dapat menghadiri makan malam.")

# Mengganti nama tamu
guest_list[1] = "Sion"

# Menampilkan undangan baru
print("\nUndangan terbaru:")

print(f"Halo {guest_list[0]}, saya mengundang Anda untuk makan malam.")
print(f"Halo {guest_list[1]}, saya mengundang Anda untuk makan malam.")
print(f"Halo {guest_list[2]}, saya mengundang Anda untuk makan malam.")