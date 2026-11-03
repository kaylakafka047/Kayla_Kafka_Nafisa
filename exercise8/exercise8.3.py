def make_shirt(size, message):
    """Mencetak ringkasan ukuran dan pesan pada kaos."""
    print(f"Membuat kaos ukuran {size.upper()} dengan tulisan: '{message}'.")

# 1. Memanggil fungsi menggunakan positional arguments
make_shirt('m', 'Python is Fun!')

# 2. Memanggil fungsi menggunakan keyword arguments
make_shirt(size='l', message='Belajar Coding itu Seru!')