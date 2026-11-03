# 1. Tests for equality and inequality with strings
fruit = 'Apple'
print("Is fruit == 'Apple'? I predict True.")
print(fruit == 'Apple')
print("Is fruit != 'Apple'? I predict False.")
print(fruit != 'Apple')

# 2. Tests using the lower() method
name = 'JOHN'
print("\nIs name.lower() == 'john'? I predict True.")
print(name.lower() == 'john')
print("Is name.lower() == 'JOHN'? I predict False.")
print(name.lower() == 'JOHN')

# 3. Numerical tests
score = 85
print("\nIs score == 85? I predict True.")
print(score == 85)
print("Is score != 85? I predict False.")
print(score != 85)
print("Is score > 90? I predict False.")
print(score > 90)
print("Is score < 100? I predict True.")
print(score < 100)
print("Is score >= 85? I predict True.")
print(score >= 85)
print("Is score <= 80? I predict False.")
print(score <= 80)

# 4. Tests using 'and' and 'or'
age = 25
has_license = True
print("\nIs age > 18 and has_license == True? I predict True.")
print(age > 18 and has_license)
print("Is age > 30 and has_license == True? I predict False.")
print(age > 30 and has_license)
print("Is age > 30 or has_license == True? I predict True.")
print(age > 30 or has_license)
print("Is age < 18 or has_license == False? I predict False.")
print(age < 18 or not has_license)

# 5. Test whether an item is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print("\nIs 'mushrooms' in requested_toppings? I predict True.")
print('mushrooms' in requested_toppings)
print("Is 'pepperoni' in requested_toppings? I predict False.")
print('pepperoni' in requested_toppings)

# 6. Test whether an item is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
print("\nIs 'marie' not in banned_users? I predict True.")
print(user not in banned_users)
print("Is 'andrew' not in banned_users? I predict False.")
print('andrew' not in banned_users)