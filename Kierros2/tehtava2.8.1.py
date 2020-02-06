def main():
    for i in range(1, 13):
        if i == 2:
            for j in range(1, 29):
                print(j, ".", i, ".", sep="")
        elif i == 4:
            for j in range(1, 31):
                print(j, ".", i, ".", sep="")
        elif i == 6:
            for j in range(1, 31):
                print(j, ".", i, ".", sep="")
        elif i == 9:
            for j in range(1, 31):
                print(j, ".", i, ".", sep="")
        elif i == 11:
            for j in range(1, 31):
                print(j, ".", i, ".", sep="")
        else:
            for j in range(1, 32):
                print(j, ".", i, ".", sep="")
main()
