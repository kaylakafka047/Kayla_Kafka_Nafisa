print("--- Metode 1: Kondisi di while statement ---")
topping = ""
while topping != 'quit':
    topping = input("Masukkan topping (ketik 'quit'): ")
    if topping != 'quit':
        print(f"Menambahkan {topping}.")

print("\n--- Metode 2: Menggunakan Variabel Aktif (Flag) ---")
active = True
while active:
    topping = input("Masukkan topping (ketik 'quit'): ")
    if topping == 'quit':
        active = False
    else:
        print(f"Menambahkan {topping}.")

print("\n--- Metode 3: Menggunakan break statement ---")
while True:
    topping = input("Masukkan topping (ketik 'quit'): ")
    if topping == 'quit':
        break
    print(f"Menambahkan {topping}.")