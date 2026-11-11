from pathlib import Path
import json

# Collect user information.
username = input("What is your username? ")
full_name = input("What is your full name? ")
city = input("Where do you live? ")

# Store information in a dictionary.
user_info = {
    "username": username,
    "full_name": full_name,
    "city": city
}

# Write the dictionary to a JSON file.
path = Path("user_dictionary.json")
contents = json.dumps(user_info)
path.write_text(contents)

# Read the dictionary from the JSON file.
contents = path.read_text()
stored_info = json.loads(contents)

# Display the stored information.
print("\nHere's what I know about you:")
print(f"Username: {stored_info['username']}")
print(f"Full name: {stored_info['full_name']}")
print(f"City: {stored_info['city']}")