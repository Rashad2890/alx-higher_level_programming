for l in range(10):
    for k in range(l, 10):
        if l < k:
            print("{:d}{:d}".format(l, k),
                  end="\n" if l == 8 and k == 9 else ", ")
