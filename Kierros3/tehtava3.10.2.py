EPSILON = 0.000000001


# määrittele tänne funktio vertailu tehtävänannon mukaisesti
def vertaile(x, y):
    return abs(x-y) < EPSILON


def main():
    a = float(input("Anna liukuluku A: "))
    b = float(input("Anna liukuluku B: "))

    if vertaile(a, b):
        print("Luvut ovat samat!")
    else:
        print("Luvut eivät ole samat!")


main()
