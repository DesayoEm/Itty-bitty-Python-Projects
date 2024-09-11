def calculate_average():
    print("You need to enter three numbers and I'll calculate the average")
    while True:
        try:
            num1=int(input("Enter the first number:"))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            num2=int(input("Enter the second number:"))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            num3=int(input("Enter the third number:"))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    average=(num1 + num2 + num3)//3
    print(f"The average of {num1}, {num2}, and {num3} is {average}")
calculate_average()
