#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    arg_count = len(argv) - 1

    if arg_count == 0:
        print("0")
    else:
        results = sum(int(args) for args in argv[1:])
        print(results)
