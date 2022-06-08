#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == '+':
        print("{} {} {} = {}".format(a, argv[2], b, add(a, b)))
    elif argv[2] == '-':
        print("{} {} {} = {}".format(a, argv[2], b, sub(a, b)))
    elif argv[2] == '*':
        print("{} {} {} = {}".format(a, argv[2], b, mul(a, b)))
    elif argv[2] == '/':
        print("{} {} {} = {}".format(a, argv[2], b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
