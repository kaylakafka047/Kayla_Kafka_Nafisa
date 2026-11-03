def city_country(city, country):
    """Mengembalikan string berformat kota dan negara."""
    return f"{city.title()}, {country.title()}"

# Memanggil fungsi dan mencetak nilai yang dikembalikan
city1 = city_country('santiago', 'chile')
city2 = city_country('tokyo', 'jepang')
city3 = city_country('paris', 'perancis')

print(city1)
print(city2)
print(city3)