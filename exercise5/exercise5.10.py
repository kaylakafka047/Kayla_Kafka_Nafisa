current_users = ['john', 'alice', 'Bob', 'Charlie', 'admin']
new_users = ['ALICE', 'david', 'john', 'Eve', 'Frank']

# Membuat copy current_users dalam versi lowercase
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Maaf, nama pengguna '{new_user}' sudah digunakan. Silakan masukkan nama lain.")
    else:
        print(f"Nama pengguna '{new_user}' masih tersedia!")