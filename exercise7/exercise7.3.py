number = input("Masukkan sebuah angka, dan saya akan beri tahu jika itu kelipatan 10: ")
number = int(number)

if number % 10 == 0:
    print(f"Angka {number} adalah kelipatan 10.")
else:
    print(f"Angka {number} bukan kelipatan 10.")