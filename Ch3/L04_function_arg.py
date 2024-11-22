def main():
    print("say_hello()")
    say_hello()
    print("")

    print("say_hello(name)")
    say_hello("Zoe")
    print("")

    print("say_hello(name, times)")
    say_hello("Zoe", 5)
    print("")

    print("say_hello(name, times, 1, 2, 3, 4)")
    say_hello("Zoe", 5, 1, 2, 3, 4)
    print("")

    print("say_hello(name, times, 1, 2, 3, 4, val=7, mode=prod)")
    say_hello("Zoe", 5, 1, 2, 3, 4, val=7, mode="prod")
    print("")

    # This kind of overrides are not possible with python
    # print("say_hello(int)")
    # say_hello(5)
    # print("")

    # print("say_hello(double)")
    # say_hello(5.5)
    # print("")

def say_hello(name='friend', times=1, *args, **kwargs):
    print(f"Hello there {name}, times: {times}, extras: {args}, keyword args: {kwargs}")
    return

# Python prints arrays, so I do not need this function
# def print_args(*args):
#     sb = "["
#     for arg in args:
#         sb += "\""
#         sb += f"{arg}"
#         sb += "\", "
#     sb += "]"
#     return sb

if __name__ == "__main__":
    main()