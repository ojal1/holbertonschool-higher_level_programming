#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    if argc == 0:
        print(0)
    else:
        num = int(argv[1])
        for i in range(1, argc):
            num += int(argv[i + 1])
        print(num)