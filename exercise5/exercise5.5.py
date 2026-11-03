def check_alien_points(alien_color):
    if alien_color == 'green':
        print("Anda mendapatkan 5 poin!")
    elif alien_color == 'yellow':
        print("Anda mendapatkan 10 poin!")
    elif alien_color == 'red':
        print("Anda mendapatkan 15 poin!")

print("--- Versi 1 (Hijau) ---")
check_alien_points('green')

print("\n--- Versi 2 (Kuning) ---")
check_alien_points('yellow')

print("\n--- Versi 3 (Merah) ---")
check_alien_points('red')