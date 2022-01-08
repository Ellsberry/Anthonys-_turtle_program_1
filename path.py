"""Creates a set of x y coordinates between 2 points"""
# x1 = -20
# x2 = 30
# y1 = -20
# y2 = 50


def path(x1, y1, x2, y2):
    """ Given the beginning x, y coordinates and ending x, y coordinates return the path between them"""
    print("x1 = ", x1, "y1 = ", y1, "x2 = ", x2, "y2 = ", y2)
    e_path = set()                           # this creates an empty set
    print("I am in the path module")
    # create path when the x-axis is a larger part of the path
    if abs(x1 - x2) >= abs(y1 - y2):
        if x1 <= x2 and y1 >= y2:                    # case 1
            ydif = (y1-y2)/abs(x1-x2+1)
            print("case 1:  y diff = ", ydif)
            print("case 1 ", abs(x1 - x2 - 1))
            for i in range(abs(x1-x2-1)):
                print(int(x1), int(y1))

                e_path.add((int(x1), int(y1)))
                x1 += 1
                y1 -= ydif
        elif x1 > x2 and y1 >= y2:                  # case 2
            ydif = (y1 - y2) / abs(x1 - x2 - 1)
            print("case 2:  y diff = ", ydif)
            print("case 2 ", abs(x1 - x2 + 1))
            for i in range(abs(x1 - x2 + 1)):
                print(int(x2), int(y2))

                e_path.add((int(x2), int(y2)))
                x2 += 1
                y2 += ydif
        elif x1 >= x2 and y1 < y2:                 # case 3
            ydif = (y1 - y2) / abs(x1 - x2 - 1)
            print("case 3:  y diff = ", ydif)
            print("case 3 ", abs(x1 - x2 + 1))
            for i in range(abs(x1 - x2 + 1)):
                print(int(x1), int(y1))

                e_path.add((int(x1), int(y1)))
                x1 -= 1
                y1 -= ydif
        elif x1 < x2 and y1 < y2:                     # case 4
            ydif = (y1 - y2) / abs(x1 - x2 + 1)
            print("case 4:  y diff = ", ydif)
            print("case 4 ", abs(x1 - x2 - 1))
            for i in range(abs(x1 - x2 - 1)):
                print(int(x1), int(y1))

                e_path.add((int(x1), int(y1)))
                x1 += 1
                y1 -= ydif

    # create path when the x-axis is a larger part of the path
    else:
        if abs(x1 - x2) < abs(y1 - y2):                  # case 5
            if x1 >= x2 and y1 <= y2:
                xdif = (x1 - x2) / abs(y1 - y2 + 1)
                print("case 5:  x diff = ", xdif)
                print("case 5 ", abs(y1 - y2 - 1))
                for i in range(abs(y1 - y2 - 1)):
                    print(int(x1), int(y1))

                    e_path.add((int(x1), int(y1)))
                    x1 -= xdif
                    y1 += 1
            elif x1 >= x2 and y1 > y2:                    # case 6
                xdif = (x1 - x2) / abs(y1 - y2 - 1)
                print("case 6:  x diff = ", xdif)
                print("case 6 ", abs(y1 - y2 + 1))
                for i in range(abs(y1 - y2 + 1)):
                    print(int(x1), int(y1))

                    e_path.add((int(x1), int(y1)))
                    x1 -= xdif
                    y1 -= 1
            elif x1 < x2 and y1 > y2:                    # case 7
                xdif = (x1 - x2) / abs(y1 - y2 - 1)
                print("case 7:  x diff = ", xdif)
                print("case 7 ", abs(y1 - y2 + 1))
                for i in range(abs(y1 - y2 + 1)):
                    print(int(x1), int(y1))

                    e_path.add((int(x1), int(y1)))
                    x1 -= xdif
                    y1 -= 1
            elif x1 < x2 and y1 <= y2:                   # case 8
                xdif = (x1 - x2) / abs(y1 - y2 + 1)
                print("case 8:  x diff = ", xdif)
                print("case 8 ", abs(y1 - y2 - 1))
                for i in range(abs(y1 - y2 - 1)):
                    print(int(x1), int(y1))
                    e_path.add((int(x1), int(y1)))
                    x1 -= xdif
                    y1 += 1
        print("end of path")
    return e_path
