#!/usr/bin/python3
for a in range(0, 10):
    for b in range(a + 1, 10):
        print("{:02}".format(a * 10 + b), end=", "
              if (a != 8 or b != 9) else "\n")
