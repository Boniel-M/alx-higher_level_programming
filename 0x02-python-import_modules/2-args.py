#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    arg_count = len(argv) - 1

    if len(argv) == 0:
        print("0 arguments.")
    else:
        print(f"{arg_count} arguments:")

        for a in range(1, len(argv)):
            print("{}: {}".format(a, argv[a]))
