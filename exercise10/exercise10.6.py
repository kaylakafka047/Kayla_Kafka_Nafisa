try:
    number_1 = input("Give me a number: ")
    number_1 = int(number_1)

    number_2 = input("Give me another number: ")
    number_2 = int(number_2)

except ValueError:
    print("Sorry, I really needed a number.")

else:
    total = number_1 + number_2
    print(f"The sum of {number_1} and {number_2} is {total}.")