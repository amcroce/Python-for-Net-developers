def main():
    while True:
        text = input("Enter a number 1 -> 1.000 (blank to exit): ")
        ## Check if text has a value
        if not text or len(text.strip()) == 0:
            print("Later...")
            break
        ## Check if text is a number
        num = int(text)
        numClass = "small" if num < 100 else "huge!"
        print(f"The number {num} is {numClass}")

if __name__ == "__main__":
    main()