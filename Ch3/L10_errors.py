from colorama import Fore

def main():
    values = list(range(1, 20)) + [None, 1, 1, 2, 3, 5, 8]

    for v in values:
        try:
            print(Fore.YELLOW + f"Calling stechy_method with {v}...", flush=True)
            sketchy_method(v)
        except ArithmeticError:
            print(Fore.LIGHTRED_EX + f"*** Cannot compute with {v}", flush=True)
        except BrokenPipeError:
            print(Fore.LIGHTRED_EX + f"*** Network error check connection", flush=True)
        except Exception as e:
            print(Fore.LIGHTRED_EX + f"*** Error: {type(e).__name__} ==> {str(e)}", flush=True)
        finally:
            print(Fore.LIGHTGREEN_EX + "Done.", flush=True)

def sketchy_method(value: int):
    import random

    if not value:
        raise ValueError(f'{value} is not valid.')
    elif value % 6 == 0:
        raise ArithmeticError()
    elif random.randint(1, 10) == 3:
        raise BrokenPipeError('Bad network!')

    print('sketchy_method() actually worked!')

if __name__ == "__main__":
    main()