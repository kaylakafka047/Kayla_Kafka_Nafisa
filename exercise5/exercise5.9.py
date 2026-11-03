usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, status laporan apa yang ingin Anda lihat hari ini?")
        else:
            print(f"Hello {username.title()}, terima kasih telah login kembali.")
else:
    print("Kita perlu mencari beberapa pengguna baru!")