#!/usr/bin/python3
for k in range(25, -1, -1):
    c = k + ord('A')
    if k % 2 == 1:
        c += 32
    print("{:c}".format(c), end="")
