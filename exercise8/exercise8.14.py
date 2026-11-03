def make_car(manufacturer, model, **car_info):
    """Menyimpan informasi tentang mobil dalam sebuah dictionary."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

# Pemanggilan fungsi yang benar menggunakan tanda '='
car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)