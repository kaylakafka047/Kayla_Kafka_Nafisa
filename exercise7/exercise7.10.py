responses = {}

polling_active = True

while polling_active:
    name = input("\nSiapa nama Anda? ")
    response = input("Jika Anda bisa mengunjungi satu tempat di dunia, ke mana Anda akan pergi? ")
    
    responses[name] = response
    
    repeat = input("Apakah ada orang lain yang ingin ikut polling? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

print("\n--- Hasil Polling Liburan Impian ---")
for name, location in responses.items():
    print(f"{name.title()} ingin sekali berkunjung ke {location.title()}.")