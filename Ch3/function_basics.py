import random

def main():
    show_header()

    # call python built-in random function
    the_number = random.randint(1, 100)
    count = 0

    while True:
        guess = get_guess()
        if guess is None:
            continue
        count += 1

        if evaluate_guess(guess, the_number):
            break

    print(f"You guessed it in {count} steps.")
    pass


def show_header():
    print("-------------------------------------------")
    print("|                                         |")
    print("|          Python High / Low Game         |")
    print("|                                         |")
    print("-------------------------------------------")
    print("")
    print("I'm thinking of a number between 1 and 100.")
    print("In how many steps can you guess it?")
    print("")
    pass

def get_guess():
    print("What number am I thinking of? ")
    # use pythong built in method to read the console input here into a variable
    val = input()

    if not val.isnumeric():
        print("That's not a number!")
        return None

    if int(val) < 1 or int(val) > 100:
        print(f"{val} is not between 1 and 100.")
        return None

    return int(val)

def evaluate_guess(guess, number):
    if guess == number:
        print(f"You got it! The number was {number}")
    elif guess < number:
        print("It's higher")
    else:
        print("It's lower")

    return guess == number


if __name__ == "__main__":
    main()