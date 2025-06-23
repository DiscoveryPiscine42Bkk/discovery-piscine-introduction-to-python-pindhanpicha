user_input = input("Please enter a number: ")
try:
    number = float(user_input)

    if number % 1 !=0:
        print("The number is an decimal.")
    else:
        print("The number is an integer.")
except ValueError:
    print("That's not a valid number!")
