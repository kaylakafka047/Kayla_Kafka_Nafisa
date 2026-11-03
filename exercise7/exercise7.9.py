sandwich_orders = ['tuna', 'pastrami', 'turkey', 'pastrami', 'club', 'pastrami', 'egg mayo']
finished_sandwiches = []

print("Mohon maaf, toko deli sedang kehabisan pastrami hari ini.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Saya sedang membuat sandwich {current_sandwich} Anda.")
    finished_sandwiches.append(current_sandwich)

print("\nDaftar sandwich yang berhasil dibuat:")
for sandwich in finished_sandwiches:
    print(f"- Sandwich {sandwich}")