#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    res1 = add(a, b)
    res2 = sub(a, b)
    res3 = mul(a, b)
    res4 = div(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, res1))
    print("{:d} - {:d} = {:d}".format(a, b, res2))
    print("{:d} * {:d} = {:d}".format(a, b, res3))
    print("{:d} / {:d} = {:d}".format(a, b, res4))
