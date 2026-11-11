from random import choice

lottery = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    "A", "B", "C", "D", "E"
]

my_ticket = [7, "B", 3, "E"]

attempts = 0

while True:
    attempts += 1

    available_items = lottery.copy()
    winning_ticket = []

    for i in range(4):
        selected_item = choice(available_items)
        winning_ticket.append(selected_item)
        available_items.remove(selected_item)

    if set(winning_ticket) == set(my_ticket):
        break

print("My ticket:", my_ticket)
print("Winning ticket:", winning_ticket)
print(f"It took {attempts} attempts to win.")