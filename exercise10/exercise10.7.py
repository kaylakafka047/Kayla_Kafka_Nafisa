print("Enter 'q' at any time to quit.")

while True:
    try:
        number_1 = input("\nGive me a number: ")

        if number_1.lower() == "q":
            break

        number_1 = int(number_1)

        number_2 = input("Give me another number: ")

        if number_2.lower() == "q":
            break

        number_2 = int(number_2)

    except ValueError:
        print("Sorry, I really needed a number.")

    else:
        total = number_1 + number_2
        print(f"The sum of {number_1} and {number_2} is {total}.")