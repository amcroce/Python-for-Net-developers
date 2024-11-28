def main():
    for n in fibonacci():
        if n > 10000:
            break
        print(n, end=', ')

def fibonacci_num(count):
    current = 0
    # next is a function in python so lets try to avoid it as a variabe name
    nxt = 1
    nums = []
    for _ in range(count):
        current, nxt = nxt, current + nxt
        nums.append(current)
    return nums

def fibonacci():
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, current + nxt
        yield current

if __name__ == "__main__":
    main()