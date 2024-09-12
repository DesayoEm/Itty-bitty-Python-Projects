import random
answer = random.randint(1,10)
while True:
    try:
        guess = int(input("Enter a number between 1 and 10"))
        if guess <1 or guess>10:
            print("Your guess must be between 1 and 10")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number between 1 and 10.")


if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print(f"Well done! You guessed it. The correct number is {answer}")
    else:
        print(f"Sorry, you have not guessed correctly, the correct number is {answer}")
else:
    print("Nailed it at first trial!")