#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    arg_count = len(argv) - 1
    if arg_count == 0:
        print("0 arguments.")
    else:
        if arg_count == 1:
            arg_word = "argument:"
        else:
            arg_word = "arguments:"
        print(f"{arg_count} {argument_word}")

        for a in range(1, len(argv)):
            print("{}: {}".format(a, argv[a]))
