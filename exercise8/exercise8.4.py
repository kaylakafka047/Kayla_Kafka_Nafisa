def make_shirt(size='large', message='I love Python'):
    """Membuat kaos dengan nilai default ukuran L dan pesan khusus."""
    print(f"Membuat kaos ukuran {size.title()} dengan cetakan: '{message}'.")

# Kaos Large dengan pesan default
make_shirt()

# Kaos Medium dengan pesan default
make_shirt(size='medium')

# Kaos Small dengan pesan kustom
make_shirt(size='small', message='Python Developer')