from pathlib import Path

guests = []

while True:
    name = input("Enter your name (or 'quit' to finish): ")

    if name.lower() == "quit":
        break

    guests.append(name)
    print(f"Hello, {name}! You have been added to the guest book.")

# Write all names to the file.
path = Path("guest_book.txt")

contents = ""
for guest in guests:
    contents += guest + "\n"

path.write_text(contents)

print("Guest book has been saved.")