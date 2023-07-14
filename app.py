# Computer chooses a number from 1 - 10 in the background
# Prompt the user to guess the number
# If user is not correct, claim false and show the correct number.

import random

def main():
    number = int(random.uniform(1, 11))
    if get_user() == number:
        print(f"That is correct! The answer was {number}.")
    else:
        print(f"Sorry, that is not correct. The correct answer is {number}.")


def get_user():
    while True:
        try:
            return int(input(">>> "))
        except ValueError:
            print("It must be an integer!")
    


print("The computer has a number, try to guess!")
main()