usernames = ['admin', 'jaden', 'eric', 'sarah', 'budi']

for username in usernames:
    if username == 'admin':
        print("Hello admin, status laporan apa yang ingin Anda lihat hari ini?")
    else:
        print(f"Hello {username.title()}, terima kasih telah login kembali.")