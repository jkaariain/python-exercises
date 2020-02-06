def main():
    luvut = []

    print("Anna 5 lukua:")
    for i in range(0, 5):
        syotetty_luku = int(input("Seuraava luku: "))
        if syotetty_luku > 0:
            luvut.append(syotetty_luku)

    print("Syöttämäsi nollaa suuremmat luvut olivat:")
    for i in luvut:
        print(i)

main()
