def main():
    while True:
        text = input("Enter a number 1 -> 1.000 (blank to exit): ")
        ## Check if text has a value
        ## not evaluates as Ture if text is empty, because of the "falsy" concept
        if not text.strip():
            print("Later...")
            break
        ## Check if text is a number
        num = int(text)
        num_class = "small" if num < 100 else "huge!"
        print(f"The number {num} is {num_class}")

if __name__ == "__main__":
    main()