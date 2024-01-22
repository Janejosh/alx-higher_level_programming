#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    i = len(argv)
    if i != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    if operator == '+':
        print("{a} {operator} {b}".format({add(a, b)))
    elif operator == '-':
        print("{a} {operator} {b}".format({sub(a, b)))
    elif operator == '*':
        print("{a} {operator} {b}".format({mul(a, b)))
    elif operator == '/':
        print("{a} {operator} {b}".format({div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
