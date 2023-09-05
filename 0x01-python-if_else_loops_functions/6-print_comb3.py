#!/usr/bin/python3
for n in range(10):
    for k in range(n, 10):
        if n < k:
            print("{:d}{:d}".format(n, k),
                  end="\n" if n == 8 and k == 9 else ", ")
