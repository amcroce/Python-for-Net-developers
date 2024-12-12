def main():
    counter1 = create_counter(14, 1)
    counter2 = create_counter(-100, 2)
    counter1()
    counter2()
    counter1()
    counter2()
    counter1()
    counter2()
    pass

def create_counter(starter_val, counter_id):
    start = starter_val
    print(f"Creating a counter with start value {starter_val}...")
    def counter():
        nonlocal start
        start += 1
        print(f"#{counter_id}: Counting {starter_val}\t-->\t{start}")
    return counter

if __name__ == "__main__":
    main()