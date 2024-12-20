def main():

    while True:
        text = input("Enter a number between 1 and 4, (blank to exit):")
        if not text:
            print("Exiting...")
            break
        num = int(text)
        switcher = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four"
        }
        print(switcher.get(num, "Invalid number!"))

if __name__ == "__main__":
    main()