#!/usr/bin/python3

"""prints all the names defined by the compiled module hidden_4.pyc"""

if __name__ == "__main__":
    import hidden_4
    names = [name for name in dir(hidden_4) if not name.startswith('__')]
    for name in names:
        print(name)
