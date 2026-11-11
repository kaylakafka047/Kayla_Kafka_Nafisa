import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Generate a random number.
print("Random number:", random.randint(1, 10))

# Choose one random element.
print("Random choice:", random.choice(numbers))

# Choose four different elements.
print("Random sample:", random.sample(numbers, 4))

# Shuffle the list.
random.shuffle(numbers)
print("Shuffled list:", numbers)