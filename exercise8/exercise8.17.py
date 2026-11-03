def hitung_luas_persegi(sisi):
    """Menghitung luas persegi berdasarkan panjang sisi."""
    return sisi ** 2

def tampilkan_pesan(pesan):
    """Menampilkan pesan teks ke layar."""
    print(f"Pesan: {pesan}")

# Contoh pemanggilan fungsi yang telah distyling rapi sesuai PEP 8
sisi_persegi = 5
luas = hitung_luas_persegi(sisi_persegi)
tampilkan_pesan(f"Luas persegi adalah {luas}")