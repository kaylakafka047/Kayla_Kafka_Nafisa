from pathlib import Path
import json

path = Path("favorite_number.json")

try:
    contents = path.read_text()

except FileNotFoundError:
    favorite_number = input("What's your favorite number? ")

    contents = json.dumps(favorite_number)
    path.write_text(contents)

    print("Thanks! I'll remember that.")

else:
    favorite_number = json.loads(contents)

    print(
        f"I know your favorite number! "
        f"It's {favorite_number}."
    )