#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1  # Excluyendo el nombre del script
    print("{} argument{}:".format(num_args, "" if num_args == 1 else "s"))

    if num_args > 0:
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
