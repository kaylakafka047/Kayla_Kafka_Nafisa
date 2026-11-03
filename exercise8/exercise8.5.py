def describe_city(city, country='islandia'):
    """Menampilkan informasi kota dan negaranya."""
    print(f"{city.title()} berada di negara {country.title()}.")

# Pemanggilan menggunakan default country
describe_city('reykjavik')
describe_city('akureyri')

# Pemanggilan dengan negara yang berbeda
describe_city('jakarta', country='indonesia')