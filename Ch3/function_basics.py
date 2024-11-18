import random

def main():
    show_header()

    # call python built-in random function
    the_number = random.randint(1, 100)
    count = 0

    while True:
        guess = get_guess()

        # if guess is None:
        # I first uses None to compare, but it's better to use the pythonic way
        if not guess:
            continue
        count += 1

        if evaluate_guess(guess, the_number):
            break

    print(f"You guessed it in {count} steps.")

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
    try:
        # I first used a print and then assigned the input to a variable
        # print("What number am I thinking of? ")
        # val = input()

        # But I can get print the message directly in the input
        text = input("What number am I thinking of? ")
        number = int(text)

        # It worked using the any typed val but I will use an exception
        # if not val.isnumeric():
        #     print("That's not a number!")
        #     return None

        if number < 1 or number > 100:
            print(f"{number} is not between 1 and 100.")
            return None

        return int(number)
    except:
        print("That's not a number!")
        return None

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