def main():
    data = [55, 987, 86, -233, 8, 13, -377, 3, 1, -34, 610, 144, 5, 21, 2, 1]
    data.sort(key=lambda n: abs(n))
    print(data)

    ## Here is how the data.Select(n => n * 2) looks in Python
    ## For lazy evaluation, instead of a list, use a generator with () instead of []
    doubled = [2 * n for n in data]
    print(doubled)

if __name__ == "__main__":
    main()