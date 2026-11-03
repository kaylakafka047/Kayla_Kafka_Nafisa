prompt = "\nMasukkan topping pizza yang Anda inginkan"
prompt += "\n(Ketik 'selesai' jika sudah selesai): "

topping = ""
while topping != 'selesai':
    topping = input(prompt)
    
    if topping != 'selesai':
        print(f"Menambahkan {topping} ke pizza Anda!")