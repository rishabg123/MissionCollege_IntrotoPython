for i in range(1, 10):
    print("i =", i, ":", end=" ")
    for j in range(1, 10):
        print("{:2d}".format(i * j), end=" ")
    print()
