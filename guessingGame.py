import random
highest=10
answer = random.randint(1,highest)
while True:
    try:
        guess = int(input(f"Enter a number between 1 and {highest}"))
        if guess <1 or guess>highest:
            print(f"Your guess must be between 1 and {highest}")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number between 1 and 10.")


while guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())

print(f"Well done! You guessed it. The correct number is {answer}")
