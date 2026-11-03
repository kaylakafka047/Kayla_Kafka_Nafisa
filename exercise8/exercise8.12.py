def make_sandwich(*toppings):
    """Mencetak ringkasan pesanan sandwich dengan berbagai topping."""
    print("\nMembuat sandwich dengan topping berikut:")
    for topping in toppings:
        print(f"- {topping}")

make_sandwich('keju')
make_sandwich('turkey', 'selada', 'tomat')
make_sandwich('daging sapi', 'keju cheddar', 'saus barbecue', 'bawang bombay')