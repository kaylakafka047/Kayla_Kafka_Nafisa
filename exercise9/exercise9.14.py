from random import choice

lottery = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    "A", "B", "C", "D", "E"
]

winning_ticket = []

# Select 4 different elements.
available_items = lottery.copy()

for i in range(4):
    selected_item = choice(available_items)
    winning_ticket.append(selected_item)
    available_items.remove(selected_item)

print("The winning ticket is:")
print(winning_ticket)

print(
    f"Any ticket matching {winning_ticket} "
    "wins a prize!"
)