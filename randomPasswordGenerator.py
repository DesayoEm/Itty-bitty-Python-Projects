import string
import random
peg=True
characters = list(string.ascii_letters + string.digits + "!@#$%&")
def generatePassword():
    while True:
        try:
            passwordLength = int(input("How long do you want your password to be?"))
            if passwordLength <= 0:
                print("Please enter a positive integer for the password length.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    random.shuffle(characters)

    password=[]

    for x in range (passwordLength):
        password.append(random.choice(characters))

    random.shuffle(password)
    password="".join(password)
    print(password)

while peg:
    action=input("Would you like me to generate a password?\n Answer 'Yes' or 'No'")
    if action == "Yes".casefold():
        generatePassword()
        peg = False
    elif action == "No".casefold():
        print("It appears you don't need help")
        peg = False
    else:
        print("Invalid input. Please answer 'Yes' or 'No'")


