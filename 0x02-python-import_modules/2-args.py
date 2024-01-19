#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    l = len(argv) - 1
    if l < 1:
        print("{} arguments.".format(l))
    elif l == 1:
        print("{} argument:".format(l))
    else:
        print("{} arguments:".format(l))
    for a in range(l):
        print("{}: {:s}".format(a + 1, argv[a + 1]))
