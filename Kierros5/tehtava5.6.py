def main():
    tulokset = []
    total = 0
    for i in range(1, 6):
        tulokset.append(float
                        (input("Syötä " + str(i) + ". suorituksen aika: ")))
    tulokset.remove(max(tulokset))
    tulokset.remove(min(tulokset))

    for i in tulokset:
        total += i

    print("Virallinen kilpailutulos on {:.2f} sekuntia.".format(total/3))


main()
