#!/usr/bin/python3
for l in range(100):
    print("{:02d}".format(l), end="\n" if l == 99 else", ")
