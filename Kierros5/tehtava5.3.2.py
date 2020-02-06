def main():
    luvut = []

    print("Anna 5 lukua:")
    for i in range(0, 5):
        syotetty_luku = int(input("Seuraava luku: "))
        luvut.append(syotetty_luku)

    print("Syöttämäsi luvut päinvastaisessa järjestyksessä:")
    for i in range(4, -1, -1):
        print(luvut[i])

main()
